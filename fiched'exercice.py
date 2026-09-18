import time

#Script no.1 
annee = int(input("Entrez une année : ")) # année prise en compte poar le script

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0): # <--- calcul si année bissextile ou non
    print(f"{annee} est une année bissextile.")
else:
    print(f"{annee} n'est pas une année bissextile.") # retourne "n'est pas une année bissextile" si les critères des calcul ne sont pas rencontrés


time.sleep(10)

#Script no.2
mot_de_passe = input("Veuillez saisir votre mot de passe : ")
confirmation = input("Veuillez confirmer votre mot de passe : ")

if mot_de_passe == confirmation:
    if len(mot_de_passe) >= 8:
        print("Succès : Le mot de passe a été créé avec succès !")
    else:
        print("Erreur : Le mot de passe doit contenir au moins 8 caractères.")
else:
    print("Erreur : Les deux saisies ne sont pas identique.")
