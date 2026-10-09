from time import sleep

"""
Projet de NSI numéro 2

"""

liste_matières = [
    "écrit de français", "oral de français", "maths", "spé1", "spé2",
    "philo", "grand oral", "spé3", "HG1", "HGT", "LV11", "LV1T",
    "LV21", "LV2T", "ES1", "EST", "EPST", "EMC1", "EMCT"
]

liste_coefs = [5, 5, 2, 16, 16, 8, 8, 8, 3, 3, 3, 3, 3, 3, 3, 3, 6, 1, 1]

def recupnote(liste1) :
    """
    Demande à l'utilisateur de rentrer ses 19 notes
    
    """
    notes = []
    for matiere in liste1:
        note = float(input(f"Ta note en {matiere} : "))
        notes.append(note)
        sleep(0.2)

notes = recupnote(liste_matières)

def calcul_notedebac(liste_notes, liste_coefs) :
    somme = 0
    somme_coefs = 0
    for i in range(19) :
        somme = somme + liste_notes[i] * liste_coefs[i]
        somme_coefs = somme_coefs + liste_coefs[i]
    return somme / somme_coefs

calcul_notedebac(notes, liste_coefs)
