from sys import exit as ex
from random import random
from asyncio import sleep, run

async def main() :
    for sa in range(3, -1, -1):
        print(f"{sa}...", end = '   ', flush=True)
        await sleep(1)
    rnd = random()
    choix = input("Est ce que tu veux faire un tirage de cartes? o/n : ").strip().lower()
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
        run(main())
              
run(main())
