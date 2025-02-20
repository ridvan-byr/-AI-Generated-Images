import os
import json
import pickle
from pycocotools.coco import COCO
from PIL import Image
from sentence_transformers import SentenceTransformer, util
import torch
from torch.utils.data import DataLoader, Dataset
import numpy as np


train_images_path = r"C:\Users\Asus\PycharmProjects\YapayZeka\coco_data\train2017\train2017"
annotations_file = r"C:\Users\Asus\PycharmProjects\YapayZeka\coco_data\annotations\captions_train2017.json"
embedding_cache_file = r"C:\Users\Asus\PycharmProjects\YapayZeka\caption_embeddings.pkl"


coco = COCO(annotations_file)


device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = SentenceTransformer('clip-ViT-B-32', device=device)


prompt = input("Resim oluşturmak için bir açıklama girin: ")


if os.path.exists(embedding_cache_file):
    print("Önbellekten embedding'ler yükleniyor...")
    with open(embedding_cache_file, 'rb') as f:
        caption_embeddings, captions, image_ids = pickle.load(f)
else:
    print("Embedding'ler hesaplanıyor...")
    captions = [coco.anns[ann_id]['caption'] for ann_id in coco.anns]
    image_ids = [coco.anns[ann_id]['image_id'] for ann_id in coco.anns]


    class CaptionDataset(Dataset):
        def __init__(self, captions):
            self.captions = captions

        def __len__(self):
            return len(self.captions)

        def __getitem__(self, idx):
            return self.captions[idx]


    def batch_process_embeddings(captions, batch_size=256):
        dataset = CaptionDataset(captions)
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False, num_workers=4)

        caption_embeddings = []
        for batch in dataloader:
            embeddings = model.encode(batch, convert_to_tensor=False, device=device)
            caption_embeddings.append(embeddings)

        return np.vstack(caption_embeddings)

    caption_embeddings = batch_process_embeddings(captions, batch_size=256)


    with open(embedding_cache_file, 'wb') as f:
        pickle.dump((caption_embeddings, captions, image_ids), f)


print("Sorgu metni işleniyor...")
query_embedding = model.encode(prompt, convert_to_tensor=True, device=device).cpu().numpy()


caption_embeddings_cpu = caption_embeddings.cpu().numpy()


print("Benzerlikler hesaplanıyor...")
cosine_scores = np.dot(caption_embeddings_cpu, query_embedding) / (
    np.linalg.norm(caption_embeddings_cpu, axis=1) * np.linalg.norm(query_embedding)
)




best_match_idx = np.argmax(cosine_scores)
best_image_id = image_ids[best_match_idx]
best_caption = captions[best_match_idx]


image_info = coco.loadImgs(best_image_id)[0]
image_path = os.path.join(train_images_path, image_info['file_name'])

if os.path.exists(image_path):
    image = Image.open(image_path)
    output_path = r"C:\Users\Asus\Desktop\ResimlerinCiktisi\sonuc_resmi.png"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)

    print(f"En iyi eşleşen açıklama: {best_caption}")
    print(f"Resim başarıyla kaydedildi: {output_path}")
    image.show()
else:
    print(f"Resim bulunamadı: {image_path}")
