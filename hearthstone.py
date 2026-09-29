from time import sleep
from random import random

rnd = random()

for x in range(3, -1, -1) :
    print(f"{x}...", end = "    ", flush=True)
    sleep(1)
    
if rnd < 0.01 :
    print("Carte légendaire")
elif rnd < 0.04 :
    print("Carte épique")
elif rnd < 0.23 :
    print("Carte rare")
else :
    print("Carte commune")
