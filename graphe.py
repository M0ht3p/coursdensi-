import matplotlib.pylot as plt
import numpy as np

def sa(x) :
  return np.sqrt(x)

x = np.linspace(0,100, 400)
y = sa(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label="sa(x) = sqrt(x)", color="purple", linewidth=2)

plt.title("Graphique de la fonction racine carrée sa(x)", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("sa(x)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12)

plt.show
