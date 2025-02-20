import json
import os


annotations_file = r"C:\Users\Asus\PycharmProjects\TextToImage\coco_data\annotations\captions_train2017.json"


if not os.path.exists(annotations_file):
    raise FileNotFoundError(f"The specified JSON file was not found: {annotations_file}")

with open(annotations_file, 'r') as f:
    coco_data = json.load(f)


existing_image_ids = {img['id'] for img in coco_data['images']}
existing_annotation_ids = {ann['id'] for ann in coco_data['annotations']}


def add_new_image_and_annotation(coco_data, file_name, caption, height, width):

    new_image_id = max(existing_image_ids) + 1 if existing_image_ids else 1
    if new_image_id in existing_image_ids:
        print(f"This image ID is already in use: {new_image_id}")
        return


    new_image = {
        "id": new_image_id,
        "file_name": file_name,
        "height": height,
        "width": width
    }
    coco_data['images'].append(new_image)
    existing_image_ids.add(new_image_id)


    new_annotation_id = max(existing_annotation_ids) + 1 if existing_annotation_ids else 1
    if new_annotation_id in existing_annotation_ids:
        print(f"This description ID is already in use: {new_annotation_id}")
        return


    new_annotation = {
        "id": new_annotation_id,
        "image_id": new_image_id,
        "caption": caption
    }
    coco_data['annotations'].append(new_annotation)
    existing_annotation_ids.add(new_annotation_id)

    print(f"New image and description successfully added!\nResim ID: {new_image_id}\nDescription ID: {new_annotation_id}")


new_data = [
{"file_name": "AaronPaul.jpg", "caption": "Aaron Paul", "height": 168, "width": 299},
{"file_name": "AdeleExarchopoulos.jpg", "caption": "Adele Exarchopoulos", "height": 183, "width": 275},
{"file_name": "AhmetKaya.jpg", "caption": "Ahmet Kaya", "height": 168, "width": 299},
{"file_name": "AjdaPekkan.jpg", "caption": "Ajda Pekkan", "height": 225, "width": 225},
{"file_name": "AlexandraDaddario.jpg", "caption": "Alexandra Daddario", "height": 183, "width": 275},
{"file_name": "AliciaVikander.jpg", "caption": "Alicia Vikander", "height": 231, "width": 218},
{"file_name": "AmberHeard.jpg", "caption": "Amber Heard", "height": 225, "width": 225},
{"file_name": "AmyAdams.jpg", "caption": "Amy Adams", "height": 225, "width": 225},
{"file_name": "AnaDeArmas.jpg", "caption": "Ana De Armas", "height": 225, "width": 225},
{"file_name": "AndrewGarfield.jpg", "caption": "Andrew Garfield", "height": 225, "width": 225},
{"file_name": "AngelinaJolie.jpg", "caption": "Angelina Jolie", "height": 168, "width": 300},
{"file_name": "AnnaKendrick.jpg", "caption": "Anna Kendrick", "height": 260, "width": 194},
{"file_name": "AnneHathaway.jpg", "caption": "Anna Hathaway", "height": 171, "width": 295},
{"file_name": "ArabanınÖnündeDuranAdam.jpg", "caption": "Man standing in front of a car", "height": 183, "width": 275},
{"file_name": "Ati242.jpg", "caption": "Ati242", "height": 225, "width": 225},
{"file_name": "BarışManço.jpg", "caption": "Barış Manço", "height": 168, "width": 299},
{"file_name": "BatuFlex.jpg", "caption": "BatuFlex", "height": 168, "width": 299},
{"file_name": "BenAffleck.jpg", "caption": "Ben Affleck", "height": 201, "width": 251},
{"file_name": "BenFero.jpg", "caption": "Ben Fero", "height": 259, "width": 194},
{"file_name": "BerkcanGüven.jpg", "caption": "Berkcan Güven", "height": 183, "width": 275},
{"file_name": "BillGates.jpg", "caption": "Bill Gates", "height": 168, "width": 300},
{"file_name": "BlackFerrari.jpg", "caption": "Black Ferrari", "height": 183, "width": 275},
{"file_name": "BlakeLively.jpg", "caption": "Blake Lively", "height": 225, "width": 225},
{"file_name": "Blok3.jpg", "caption": "Blok3", "height": 162, "width": 311},
{"file_name": "BlueFerrari.jpg", "caption": "BlueFerrari", "height": 194, "width": 259},
{"file_name": "Bmw.jpg", "caption": "Bmw", "height": 155, "width": 325},
{"file_name": "BradPitt.jpg", "caption": "Brad Pitt", "height": 900, "width": 600},
{"file_name": "BrieLarson.jpg", "caption": "Brie Larson", "height": 259, "width": 194},
{"file_name": "Bugatti.jpg", "caption": "Bugatti", "height": 134, "width": 375},
{"file_name": "CameronDiaz.jpg", "caption": "Cameron Diaz", "height": 183, "width": 275},
{"file_name": "CandanErçetin.jpg", "caption": "Candan Erçetin", "height": 225, "width": 225},
{"file_name": "CateBlanchett.jpg", "caption": "Cate Blanchett", "height": 248, "width": 203},
{"file_name": "EsterExposito.jpg", "caption": "Ester Exposito", "height": 251, "width": 201},
{"file_name": "UrsulaCorbero.jpg", "caption": "Ursula Corbero", "height": 251, "width": 201},
{"file_name": "CemKaraca.jpg", "caption": "Cem Karaca", "height": 168, "width": 300},
{"file_name": "CentralCee.jpg", "caption": "Central Cee", "height": 277, "width": 182},
{"file_name": "Ceza.jpg", "caption": "Ceza", "height": 225, "width": 225},
{"file_name": "CharlizeTheron.jpg", "caption": "Charlize Theron", "height": 183, "width": 275},
{"file_name": "ChloeGraceMoretz.jpg", "caption": "Chloe Grace Moretz", "height": 168, "width": 300},
{"file_name": "ChrisHemsworth.jpg", "caption": "Chris Hemsworth", "height": 163, "width": 310},
{"file_name": "AnnaKendrick.jpg", "caption": "Chris Rock", "height": 159, "width": 318},
{"file_name": "ChristianBale.jpg", "caption": "Christian Bale", "height": 168, "width": 299},
{"file_name": "ChristopherNolan.jpg", "caption": "Christopher Nolan", "height": 168, "width": 300},
{"file_name": "ChristophWaltz.jpg", "caption": "Christoph Waltz", "height": 168, "width": 300},
{"file_name": "CillianMurphy.jpg", "caption": "CillianMurphy", "height": 251, "width": 201},
{"file_name": "Çakal.jpg", "caption": "Emirhan Çakal", "height": 251, "width": 201},
{"file_name": "DenzelWashington.jpg", "caption": "Denzel Washington", "height": 170, "width": 296},
{"file_name": "DonToliver.jpg", "caption": "Don Toliver", "height": 225, "width": 225},
{"file_name": "Drake.jpg", "caption": "Drake", "height": 225, "width": 225},
{"file_name": "DwayneJohnson.jpg", "caption": "Dwayne Johnson", "height": 245, "width": 205},
{"file_name": "ElizabethOlsen.jpg", "caption": "Elizabeth Olsen", "height": 257, "width": 196},
{"file_name": "ElonMusk.jpg", "caption": "Elon Musk", "height": 260, "width": 194},
{"file_name": "EmilyBlunt.jpg", "caption": "Emily Blunt", "height": 183, "width": 275},
{"file_name": "EmmaStone.jpg", "caption": "Emma Stone", "height": 275, "width": 183},
{"file_name": "EmmaWatson.jpg", "caption": "Emma Watson", "height": 183, "width": 275},
{"file_name": "EmmyRossum.jpg", "caption": "Emmy Rossum", "height": 259, "width": 194},
{"file_name": "Era7Capone.jpg", "caption": "Era7Capone", "height": 225, "width": 225},
{"file_name": "ErkinKoray.jpg", "caption": "Erkin Koray", "height": 168, "width": 300},
{"file_name": "EvaGreen.jpg", "caption": "Eva Green", "height": 225, "width": 225},
{"file_name": "EvaMendes.jpg", "caption": "Eva Mendes", "height": 259, "width": 194},
{"file_name": "Ezhel.jpg", "caption": "Ezhel", "height": 178, "width": 283},
{"file_name": "FerdiTayfur.jpg", "caption": "Ferdi Tayfur", "height": 177, "width": 284},
{"file_name": "Ferrari.jpg", "caption": "Ferrari", "height": 168, "width": 299},
{"file_name": "GaryOldman.jpg", "caption": "Gary Oldman", "height": 193, "width": 259},
{"file_name": "GeorgeClooneyjpg", "caption": "George Clooney", "height": 174, "width": 290},
{"file_name": "GözlüklüAdam.jpg", "caption": "a man with a eyeglasses", "height": 183, "width": 275},
{"file_name": "GreenFerrari.jpg", "caption": "Green Ferrari", "height": 183, "width": 275},
{"file_name": "Gunna.jpg", "caption": "Gunna", "height": 225, "width": 225},
{"file_name": "Güneş.jpg", "caption": "Güneş", "height": 251, "width": 201},
{"file_name": "HaileeSteinfeld.jpg", "caption": "Hailee Steinfeld", "height": 183, "width": 275},
{"file_name": "HandeYener.jpg", "caption": "Hande Yener", "height": 183, "width": 275},
{"file_name": "HenryCavill.jpg", "caption": "Henry Cavill", "height": 201, "width": 251},
{"file_name": "Honda.jpg", "caption": "Elon Musk", "height": 177, "width": 285},
{"file_name": "HughJackman.jpg", "caption": "Hugh Jackman", "height": 223, "width": 226},
{"file_name": "İremDerici.jpg", "caption": "İrem Derici", "height": 168, "width": 299},
{"file_name": "JackNicholson.jpg", "caption": "Jack Nicholson", "height": 164, "width": 308},
{"file_name": "JasonStatham.jpg", "caption": "Jason Statham", "height": 159, "width": 318},
{"file_name": "JeffRedd.jpg", "caption": "Jeff Redd", "height": 225, "width": 225},
{"file_name": "JenneferAnsiton.jpg", "caption": "Jennefer Aniston", "height": 259, "width": 194},
{"file_name": "JenneferConnely.jpg", "caption": "Jennefer Connely", "height": 273, "width": 184},
{"file_name": "JenniferLawrence.jpg", "caption": "Jennifer Lawrence", "height": 275, "width": 183},
{"file_name": "JenniferLoveHewitt.jpg", "caption": "Jennifer Love Hewitt", "height": 225, "width": 225},
{"file_name": "JessicaAlba.jpg", "caption": "Jessica Alba", "height": 259, "width": 194},
{"file_name": "JessicaChastain.jpg", "caption": "Jessica Chastain", "height": 194, "width": 259},
{"file_name": "JohnnyDepp.jpg", "caption": "Johnny Depp", "height": 183, "width": 275},
{"file_name": "JonFavreau.jpg", "caption": "Jon Favreau", "height": 168, "width": 300},
{"file_name": "JosephGordonLevitt.jpg", "caption": "Joseph Gordon Levitt", "height": 188, "width": 268},
{"file_name": "JulianneMoore.jpg", "caption": "Julianne Moore", "height": 259, "width": 194},
{"file_name": "JuliaRoberts.jpg", "caption": "Julia Roberts", "height": 181, "width": 278},
{"file_name": "KateWinslet.jpg", "caption": "Kate Winslet", "height": 183, "width": 275},
{"file_name": "KatherynWinnick.jpg", "caption": "Katheryn Winnick", "height": 259, "width": 194},
{"file_name": "KayaScodelario.jpg", "caption": "Kaya Scodelario", "height": 259, "width": 194},
{"file_name": "KeanuReeves.jpg", "caption": "Keanu Reeves", "height": 171, "width": 294},
{"file_name": "KeiraKnightley.jpg", "caption": "Keira Knightley", "height": 225, "width": 225},
{"file_name": "KemalSunal.jpg", "caption": "Kemal Sunal", "height": 168, "width": 300},
{"file_name": "KenanDoğulu.jpg", "caption": "Kenan Doğulu", "height": 168, "width": 300},
{"file_name": "KendrickLamar.jpg", "caption": "Kendrick Lamar", "height": 225, "width": 225},
{"file_name": "KevinHart.jpg", "caption": "Kevin Hart", "height": 205, "width": 246},
{"file_name": "Khontkar.jpg", "caption": "Khontkar", "height": 189, "width": 267},
{"file_name": "KırmızıAraba.jpg", "caption": "Red Car", "height": 168, "width": 300},
{"file_name": "KirstenDunst.jpg", "caption": "Kirsten Dunst", "height": 269, "width": 187},
{"file_name": "KoşanAdam.jpg", "caption": "The running man", "height": 183, "width": 275},
{"file_name": "KristenStewart.jpg", "caption": "Kristen Stewart", "height": 201, "width": 251},
{"file_name": "Lamborghini.jpg", "caption": "Lamborghini", "height": 168, "width": 300},
{"file_name": "LaurenCohan.jpg", "caption": "Lauren Cohan", "height": 259, "width": 194},
{"file_name": "LeaSeydoux.jpg", "caption": "Lea Seydoux", "height": 168, "width": 299},
{"file_name": "LebronJames.jpg", "caption": "Lebron James", "height": 242, "width": 209},
{"file_name": "LeonardoDiCaprio.jpg", "caption": "Leonardo Di Caprio", "height": 159, "width": 317},
{"file_name": "LucyHale.jpg", "caption": "Lucy Hale", "height": 263, "width": 192},
{"file_name": "LvbelC5.jpg", "caption": "LvbelC5", "height": 168, "width": 299},
{"file_name": "Mabel Matiz.jpg", "caption": "Mabel Matiz", "height": 198, "width": 255},
{"file_name": "MaggieGyllenhaal.jpg", "caption": "Maggie Gyllenhaal", "height": 259, "width": 194},
{"file_name": "MargotRobbie.jpg", "caption": "Margot Robbie", "height": 265, "width": 190},
{"file_name": "MarilynMonroe.jpg", "caption": "Marilyn Monroe", "height": 183, "width": 275},
{"file_name": "MattDamon.jpg", "caption": "Matt Damon", "height": 194, "width": 259},
{"file_name": "MatthewMcConaughey.jpg", "caption": "Matthew McConaughey", "height": 183, "width": 275},
{"file_name": "MaviAraba.jpg", "caption": "Blue car", "height": 168, "width": 300},
{"file_name": "MeganFox.jpg", "caption": "Megan Fox", "height": 173, "width": 292},
{"file_name": "MelanieLaurent.jpg", "caption": "Melanie Laurent", "height": 275, "width": 183},
{"file_name": "Mercedes.jpg", "caption": "Mercedes", "height": 168, "width": 299},
{"file_name": "MetroBoomin.jpg", "caption": "Metro Boomin", "height": 182, "width": 276},
{"file_name": "MichaelJackson.jpg", "caption": "Michael Jackson", "height": 159, "width": 318},
{"file_name": "MichaelJordan.jpg", "caption": "Michael Jordan", "height": 168, "width": 299},
{"file_name": "MilaKunis.jpg", "caption": "Mila Kunis", "height": 225, "width": 225},
{"file_name": "Mitsubishi.jpg", "caption": "Mitsubishi", "height": 168, "width": 300},
{"file_name": "MLisa.jpg", "caption": "M Lisa", "height": 183, "width": 275},
{"file_name": "Motive.jpg", "caption": "Motive", "height": 244, "width": 207},
{"file_name": "Murda.jpg", "caption": "Murda", "height": 166, "width": 303},
{"file_name": "MüslümGürses.jpg", "caption": "Müslüm Gürses", "height": 168, "width": 300},
{"file_name": "NaomiWatts.jpg", "caption": "Naomi Watts", "height": 275, "width": 183},
{"file_name": "NataliePortman.jpg", "caption": "Natalie Portman", "height": 259, "width": 194},
{"file_name": "NicholasCage.jpg", "caption": "Nicholas Cage", "height": 168, "width": 300},
{"file_name": "NicholeKidman.jpg", "caption": "Nichole Kidman", "height": 183, "width": 275},
{"file_name": "NilKaraibrahimgil.jpg", "caption": "Nil Karaibrahimgil", "height": 168, "width": 300},
{"file_name": "No1.jpg", "caption": "No1", "height": 205, "width": 245},
{"file_name": "Opel.jpg", "caption": "Opel", "height": 168, "width": 300},
{"file_name": "ÖzdemirErdoğan.jpg", "caption": "Özdemir Erdoğan", "height": 179, "width": 282},
{"file_name": "PaulWalker.jpg", "caption": "Paul Walker", "height": 183, "width": 275},
{"file_name": "PenelopeCruz.jpg", "caption": "Penelope Cruz", "height": 258, "width": 190},
{"file_name": "PlayboiCarti.jpg", "caption": "Playboi Carti", "height": 251, "width": 201},
{"file_name": "RachelMcadams.jpg", "caption": "Rachel Mcadams", "height": 201, "width": 251},
{"file_name": "RachelWeisz.jpg", "caption": "Rachel Weisz", "height": 259, "width": 194},
{"file_name": "Reynmen.jpg", "caption": "Reynmen", "height": 167, "width": 301},
{"file_name": "RobertDeNiro.jpg", "caption": "Robert De Niro", "height": 168, "width": 300},
{"file_name": "RobertDowneyJr.jpg", "caption": "Robert Downey Jr", "height": 159, "width": 318},
{"file_name": "RobertPattinson.jpg", "caption": "Robert Pattinson", "height": 259, "width": 194},
{"file_name": "RosamundPike.jpg", "caption": "Rosamund Pike", "height": 259, "width": 194},
{"file_name": "RyanGosling.jpg", "caption": "Ryan Gosling", "height": 225, "width": 225},
{"file_name": "RyanReynolds.jpg", "caption": "Ryan Reynolds", "height": 168, "width": 299},
{"file_name": "SagopaKajmer.jpg", "caption": "Sagopa Kajmer", "height": 225, "width": 225},
{"file_name": "SamuelLJackson.jpg", "caption": "Samuel L Jackson", "height": 168, "width": 300},
{"file_name": "SaoirseRonan.jpg", "caption": "Saoirse Ronan", "height": 259, "width": 194},
{"file_name": "ScarlettJohanssson.jpg", "caption": "Scarlett Johansson", "height": 247, "width": 204},
{"file_name": "Sefo.jpg", "caption": "Sefo", "height": 222, "width": 227},
{"file_name": "Semicenk.jpg", "caption": "Semicenk", "height": 164, "width": 307},
{"file_name": "SertabErener.jpg", "caption": "Sertab Erener", "height": 168, "width": 300},
{"file_name": "SezenAksu.jpg", "caption": "Sezen Aksu", "height": 225, "width": 225},
{"file_name": "SharonStone.jpg", "caption": "Sharon Stone", "height": 268, "width": 188},
{"file_name": "SnoopDogg.jpg", "caption": "Snoop Dogg", "height": 275, "width": 183},
{"file_name": "StephCurry.jpg", "caption": "Steph Curry", "height": 168, "width": 299},
{"file_name": "SteveJobs.jpg", "caption": "Steve Jobs", "height": 225, "width": 225},
{"file_name": "SylvesterStallone.jpg", "caption": "Sylvester Stallone", "height": 168, "width": 299},
{"file_name": "Tarkan.jpg", "caption": "Tarkan", "height": 168, "width": 300},
{"file_name": "Tesla.jpg", "caption": "Tesla", "height": 168, "width": 300},
{"file_name": "TobeyMaguire.jpg", "caption": "Tobey Maguire", "height": 194, "width": 259},
{"file_name": "TomHardy.jpg", "caption": "Tom Hardy", "height": 168, "width": 300},
{"file_name": "TravisScott.jpg", "caption": "Travis Scott", "height": 172, "width": 293},
{"file_name": "Tupac.jpg", "caption": "Tupac", "height": 186, "width": 271},
{"file_name": "UziElChavo.jpg", "caption": "Uzi El Chavo", "height": 193, "width": 261},
{"file_name": "VinDiesel.jpg", "caption": "Vin Diesel", "height": 164, "width": 308},
{"file_name": "WagnerMoura.jpg", "caption": "Wagner Moura", "height": 245, "width": 206},
{"file_name": "WillSmith.jpg", "caption": "Will Smith", "height": 168, "width": 300},
{"file_name": "Yalın.jpg", "caption": "Yalın", "height": 168, "width": 300},
{"file_name": "Yeat.jpg", "caption": "Yeat", "height": 225, "width": 225},
{"file_name": "YeşilAraba.jpg", "caption": "Green Car", "height": 183, "width": 275},
{"file_name": "ZacEfron.jpg", "caption": "Zac Efron", "height": 173, "width": 292},
{"file_name": "NewYork.jpg", "caption": "New York", "height": 183, "width": 275},
{"file_name": "LasVegas.jpg", "caption": "Las Vegas", "height": 133, "width": 380},
{"file_name": "Miami.jpg", "caption": "Miami", "height": 183, "width": 275},
{"file_name": "Chicago.jpg", "caption": "Chicago", "height": 164, "width": 308},
{"file_name": "Washington.jpg", "caption": "Washington", "height": 159, "width": 318},
{"file_name": "SanFrancisco.jpg", "caption": "San Francisco", "height": 188, "width": 267},
{"file_name": "Boston.jpg", "caption": "Boston", "height": 183, "width": 275},
{"file_name": "USA.jpg", "caption": "United States Of America", "height": 176, "width": 286},
{"file_name": "İtalya.jpg", "caption": "Italy", "height": 168, "width": 299},
{"file_name": "Roma.jpg", "caption": "Rome", "height": 188, "width": 268},
{"file_name": "Napoli.jpg", "caption": "Napoli", "height": 194, "width": 259},
{"file_name": "Venedik.jpg", "caption": "Venice", "height": 159, "width": 318},
{"file_name": "Milano.jpg", "caption": "Milano", "height": 186, "width": 271},
{"file_name": "Türkiye.jpg", "caption": "Turkey", "height": 165, "width": 306},
{"file_name": "İstanbul.jpg", "caption": "İstanbul", "height": 128, "width": 279},
{"file_name": "İzmir.jpg", "caption": "İzmir", "height": 183, "width": 275},
{"file_name": "Antalya.jpg", "caption": "Antalya", "height": 178, "width": 283},
{"file_name": "Muğla.jpg", "caption": "Muğla", "height": 182, "width": 277},
{"file_name": "Ankara.jpg", "caption": "Ankara", "height": 159, "width": 318},
{"file_name": "Eskişehir.jpg", "caption": "Eskişehir", "height": 168, "width": 299},
{"file_name": "Almanya.jpg", "caption": "Germany", "height": 159, "width": 318},
{"file_name": "Berlin.jpg", "caption": "Berlin", "height": 175, "width": 287},
{"file_name": "frankfurt.jpg", "caption": "Frankfurt", "height": 172, "width": 292},
{"file_name": "Münih.jpg", "caption": "Munich", "height": 168, "width": 299},
{"file_name": "İngiltere.jpg", "caption": "England", "height": 168, "width": 300},
{"file_name": "Londra.jpg", "caption": "London", "height": 183, "width": 275},
{"file_name": "Liverpool.jpg", "caption": "Liverpool", "height": 183, "width": 275},
{"file_name": "Manchester.jpg", "caption": "Manchester", "height": 183, "width": 275},
{"file_name": "Oxford.jpg", "caption": "Oxford", "height": 155, "width": 326},
{"file_name": "Fransa.jpg", "caption": "France", "height": 166, "width": 303},
{"file_name": "Paris.jpg", "caption": "Paris", "height": 188, "width": 268},
{"file_name": "Lyon.jpg", "caption": "Lyon", "height": 183, "width": 275},
{"file_name": "Monaco.jpg", "caption": "Monaco", "height": 167, "width": 301},
{"file_name": "Marsilya.jpg", "caption": "Marseille", "height": 194, "width": 259},
{"file_name": "İspanya.jpg", "caption": "Spain", "height": 154, "width": 327},
{"file_name": "Madrid.jpg", "caption": "Madrid", "height": 201, "width": 251},
{"file_name": "Barcelona.jpg", "caption": "Barcelona", "height": 148, "width": 340},
{"file_name": "Sevilla.jpg", "caption": "Sevilla", "height": 180, "width": 270},
{"file_name": "Belcika.jpg", "caption": "Belgium", "height": 183, "width": 275},
{"file_name": "Brugge.jpg", "caption": "Brugge", "height": 175, "width": 288},
{"file_name": "Gent.jpg", "caption": "Gent", "height": 177, "width": 270},

]


for data in new_data:
    add_new_image_and_annotation(
        coco_data,
        file_name=data["file_name"],
        caption=data["caption"],
        height=data["height"],
        width=data["width"]
    )


with open(annotations_file, 'w') as f:
    json.dump(coco_data, f)

print("JSON file updated successfully.")
