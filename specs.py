import platform
import psutil

def afficher_specs():
    print("=" * 40)
    print("INFORMATIONS SUR LE SYSTÈME")
    print("=" * 40)
    
    print(f"Système : {platform.system()} {platform.release()}")
    print(f"Version : {platform.version()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Nom de l'ordinateur : {platform.node()}")
    
    print("\n" + "=" * 40)
    print("PROCESSEUR (CPU)")
    print("=" * 40)
    print(f"Processeur : {platform.processor()}")
    print(f"Cœurs physiques : {psutil.cpu_count(logical=False)}")
    print(f"Cœurs logiques : {psutil.cpu_count(logical=True)}")
    print(f"Fréquence actuelle : {psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else "Fréquence : Non disponible")
    print(f"Utilisation globale du CPU : {psutil.cpu_percent(interval=1)}%")

    print("\n" + "=" * 40)
    print("MÉMOIRE (RAM)")
    print("=" * 40)
    memoire = psutil.virtual_memory()
    print(f"Mémoire totale : {memoire.total / (1024**3):.2f} Go")
    print(f"Mémoire disponible : {memoire.available / (1024**3):.2f} Go")
    print(f"Mémoire utilisée : {memoire.percent}%")

    print("\n" + "=" * 40)
    print("STOCKAGE")
    print("=" * 40)
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"Lecteur : {partition.device} ({partition.mountpoint})")
            print(f"  - Total : {usage.total / (1024**3):.2f} Go")
            print(f"  - Utilisé : {usage.used / (1024**3):.2f} Go ({usage.percent}%)")
            print(f"  - Libre : {usage.free / (1024**3):.2f} Go")
        except PermissionError:
            continue
    print("=" * 40)

if __name__ == "__main__":
    afficher_specs()
