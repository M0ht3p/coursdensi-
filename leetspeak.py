ENCODE_MAP = {
    'a': '4', 'b': '8', 'e': '3', 'g': '9', 'i': '|',
    'l': '1', 'o': '0', 's': '$', 't': '7', 'z': '2',
    'A': '4', 'B': '8', 'E': '3', 'G': '9', 'I': '|',
    'L': '1', 'O': '0', 'S': '$', 'T': '7', 'Z': '2'
}

DECODE_MAP = {
    '4': 'a', '8': 'b', '3': 'e', '9': 'g', '|': 'i',
    '1': 'l', '0': 'o', '$': 's', '7': 't', '2': 'z'
}

def encode_leet(text):
    return "".join(ENCODE_MAP[char] if char in ENCODE_MAP else char for char in text)

def decode_leet(text):
    return "".join(DECODE_MAP[char] if char in DECODE_MAP else char for char in text)

if __name__ == "__main__":
    sample_text = "Hello World!"
    encoded = encode_leet(sample_text)
    decoded = decode_leet(encoded)

print(f"Originale : {sample_text} ")
print(f"Encodé: {encoded} ")
print(f"Décodé: {decoded}")

choix = input("Est ce que vous voulez (E)ncoder du texte ou (D)écoder?: ").strip().upper()

if choix == 'E':
    user_input = input("Veuillez entrer le texte à encoder: ")
    print(f"Résultat: {encode_leet(user_input)}")
elif choix == 'D':
    user_input = input("Veuillez entrer le texte à décoder: ")
    print(f"Résultat: {decode_leet(user_input)}")
else:
    print("Choix invalide. ")
