from PIL import Image
from PIL.ExifTags import TAGS

def identifier_appareil(chemin_image):
    try:
        image = Image.open(chemin_image)
        exif_data = image._getexif()
        
        if not exif_data:
            print("Aucune métadonnée EXIF trouvée dans cette image.")
            return

        fabricant = "Inconnu"
        modele = "Inconnu"
        
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            
            if tag_name == "Make":
                fabricant = str(value).strip()
            elif tag_name == "Model":
                modele = str(value).strip()

        if fabricant == "Inconnu" and modele == "Inconnu":
            print("Les informations sur l'appareil ne sont pas disponibles.")
        else:
            print(f"Marque : {fabricant}")
            print(f"Modèle : {modele}")
            
    except FileNotFoundError:
        print("Erreur : Le fichier spécifié est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

identifier_appareil('photo.jpg')
