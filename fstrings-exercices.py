import time

enseignant = "M.Martin"
salle = 204
effectif = 24
# réponse :
print(f"{enseignant} fera cours à {effectif} élèves en salle {salle}")

time.sleep(2)

prix_ht = 45.5
prix_ttc = prix_ht * 1.20
print(f"Le prix en TTC sera donc de {prix_ttc}€ ")

time.sleep(2)

notes = [12, 15, 8]
moyenne = sum(notes) / len(notes)
print(f"La moyenne arondie est de {moyenne:.1f}")
