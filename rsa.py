import math
import random


def extended_gcd(a, b):
  if a == 0:
    return b, 0, 1
  gcd, x1, y1 = extended_gcd(b % a, a)
  x = y1 - (b // a) * x1
  y = x1
  return gcd, x, y


def mod_inverse(e, phi):
  gcd, x, _ = extended_gcd(e, phi)
  if gcd != 1:
    raise Exception("L'inverse modulaire n'existe pas.")
  return (x % phi + phi) % phi


def is_prime(n, k=5):
  if n < 2:
    return False
  for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
    if n % p == 0:
      return n == p

  r, s = 0, n - 1
  while s % 2 == 0:
    r += 1
    s //= 2

  for _ in range(k):
    a = random.randrange(2, n - 1)
    x = pow(a, s, n)
    if x == 1 or x == n - 1:
      continue
    for _ in range(r - 1):
      x = pow(x, 2, n)
      if x == n - 1:
        break
    else:
      return False
  return True


def generate_prime(bits=256):
  while True:
    p = random.getrandbits(bits)
    p |= (1 << (bits - 1)) | 1
    if is_prime(p):
      return p


def generate_keypair(bits=256):
  print("Génération des nombres premiers p et q...")
  p = generate_prime(bits)
  q = generate_prime(bits)
  while p == q:
    q = generate_prime(bits)

  n = p * q
  phi = (p - 1) * (q - 1)

  e = 65537
  if math.gcd(e, phi) != 1:
    e = 3
    while math.gcd(e, phi) != 1:
      e += 2

  d = mod_inverse(e, phi)

  return ((e, n), (d, n))


def encrypt(public_key, plaintext):
  e, n = public_key
  m_int = int.from_bytes(plaintext.encode("utf-8"), "big")

  if m_int >= n:
    raise ValueError(
        "Le message est trop long pour la taille de la clé actuelle."
    )

  ciphertext = pow(m_int, e, n)
  return ciphertext


def decrypt(private_key, ciphertext):
  d, n = private_key
  m_int = pow(ciphertext, d, n)

  byte_length = (m_int.bit_length() + 7) // 8
  plaintext_bytes = m_int.to_bytes(byte_length, "big")
  return plaintext_bytes.decode("utf-8")


if __name__ == "__main__":
  print("--- Démonstration RSA ---")

  public_key, private_key = generate_keypair(bits=256)

  print(f"\nClé Publique (e, n) : \n{public_key}")
  print(f"\nClé Privée (d, n) : \n{private_key}")

  message = "Bonjour, ceci est un test de chiffrement RSA en pur Python !"
  print(f"\nMessage d'origine : {message}")

  encrypted_msg = encrypt(public_key, message)
  print(f"\nMessage chiffré (entier) :\n{encrypted_msg}")

  decrypted_msg = decrypt(private_key, encrypted_msg)
  print(f"\nMessage déchiffré : {decrypted_msg}")
