from random import randint
nombre_a_deviner = random.randint(0, 100)
essais = 0
print("Devinez le nombre entre 0 et 100 !")
while True:
    proposition = int(input("Ton essai : "))
    essais += 1
    if proposition < nombre_a_deviner:
        print("Trop petit !")
    elif proposition > nombre_a_deviner:
        print("Trop grand !")
    else:
        print(f"Vous avez trouvé le nombre mystère en {essais} essais.")
