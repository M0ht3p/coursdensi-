from sys import exit as ex
from random import random
import asyncio

async def main() :
    for x in range(3, -1, -1):
        print(f"{x}...", end = '   ', flush=True)
        await asyncio.sleep(1)
    rnd = random()
    choix = input("Est ce que tu veux faire un tirage de cartes? o/n : ")
    if choix == "n" :
        ex()
    elif choix == "o" :
        if rnd < 0.01 :
            print("Carte légendaire")
        elif rnd < 0.04 :
            print("Carte épique")
        elif rnd < 0.23 :
            print("Carte rare")
        else :
            print("Carte commune")
    else :
        print(choix)

asyncio.run(main())
