import time

def calculer_temps_jeu(debut):
    fin = time.time()
    temps_total = fin - debut
    minutes = int(temps_total // 60)
    secondes = int(temps_total % 60)
    return f"{minutes}m{secondes:02d}s"

temps_debut = time.time()

a = "bonjour,"
b = input("Quel est votre prénom? ")
c = a + ' ' + b
print(f"{a} votre prénom est {b}")

d = int(input("Quel est votre âge? "))
if d > 18:
    print("Vous êtes majeur")
elif d < 18:
    print("Vous êtes mineur")
else:
    print("Vous avez 18 ans")

time.sleep(1)
print(f"Vous vous appelez donc {b}, et vous avez {d} ans")
time.sleep(0.5)

e = input("Avez-vous le code? o/n ")
if e == "o":
    f = input("Avez-vous commencé la conduite? o/n ")
    if f == "o":
        print("Ok, je ne sors plus de chez moi")
    elif f == "n":
        print("Tant mieux, je vais pouvoir sortir")
    else:
        print("Lettre invalide, veuillez entrer o ou n")
else:
    time.sleep(0.6)
    print(f"Il faut vous y mettre, {b}.")

time.sleep(3)

duree = calculer_temps_jeu(temps_debut)
print(f"script réalisé en {duree}")
