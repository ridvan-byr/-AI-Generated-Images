# -AI-Generated-Images
Python was used for this project. It includes a project in which we can generate images from text with machine learning.


Requirements to use the project effectively

-Download the COCO dataset. Link:https://cocodataset.org/#download

-Download 2017 Train images [118K/18GB] and 2017 Train/Val annotations [241MB] from here.

-In Python code, replace output_path = r “C:\Users\Asus\Desktop\ResimlerinCiktisi\sonuc_resmi.png” with the path to the file you want to output the image to.

-In DataAdd.py 
annotations_file = r “C:\Users\Asus\PycharmProjects\Artificial Intelligence\coco_data\annotations\captions_train2017.json” replace this part with the path to the annotations file you downloaded.
-train_images_path = r “C:\Users\Asus\PycharmProjects\TextToImage\coco_data\train2017\train2017”
annotations_file = r “C:\Users\Asus\PycharmProjects\TextToImage\coco_data\annotations\captions_train2017.json”
embedding_cache_file = r “C:\Users\Asus\PycharmProjects\TextToImage\caption_embeddings.pkl”

 Don't forget to replace these file paths in main.py with the file path you specified.

-In DataAdd.py, throw the images you downloaded to add data into the images in the train folder and make sure that the naming of the image you throw is done properly.

-To add the image to the dataset, put the name of the jpg file in the “file_name”: field, the text you want this image to appear when the text is entered in the “caption”: field, and the values you want in the “height”: and “width”: fields to set the width and height of the image.

Warning

-When you run main.py after adding data, it may take a while. If there is no data insertion or the data has already been processed once, the code will run fast and smoothly.
