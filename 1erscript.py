import time
a = "bonjour,"
b = input("Quelle est votre prénom? ")
c=a+' '+b
print(f"{a} votre prénom est {b}")
d = int(input("Quel est votre age? "))
if d > 18 :
    print("Vous êtes majeur")
elif d < 18 :
    print("Vous êtes mineur")
else :
    print("Vous avez 18 ans")
time.sleep(1)
print(f"Vous vous appelez donc {b}, et vous avez {d} ans")
time.sleep(0.5)
e = input("Avez vous le code? o/n ")
if e == "o" :
    f = input("Avez vous commencé la conduite? o/n ")
    if f == "o" :
        print("Ok, je ne sors plus de chez moi ")
    elif f == "n" :
        print("Tant mieux, je vais pouvoir sortir")
    else :
        print("Lettre invalide, veuillez entrer o ou n")
else :
    time.sleep(0.6)
    print(f"Il faut vous y mettre, {b}. ")
time.sleep(3)
print("script réalisé en 7m36s")
