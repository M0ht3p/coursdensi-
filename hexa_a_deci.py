def decimal_vers_hexadecimal(nombre: int) -> str:
    if nombre < 0:
        raise ValueError("Veuillez saisir un entier positif ou nul.")
    return hex(nombre)[2:].upper()


def hexadecimal_vers_decimal(nombre_hex: str) -> int:
    return int(nombre_hex, 16)


choix = input("Choisissez la conversion (1 = décimal vers hexadécimal, 2 = hexadécimal vers décimal) : ")

if choix == "1":
    nombre = int(input("Entrez un entier décimal : "))
    print("Résultat hexadécimal :", decimal_vers_hexadecimal(nombre))
elif choix == "2":
    nombre_hex = input("Entrez un nombre hexadécimal : ").strip()
    print("Résultat décimal :", hexadecimal_vers_decimal(nombre_hex))
else:
    print("Choix invalide.")
