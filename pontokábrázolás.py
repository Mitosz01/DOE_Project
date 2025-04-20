import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# CSV fájl beolvasása
df = pd.read_csv("python/csv making.csv")  # elérési útvonal

max = df["Y"].max()

# 3D pontdiagram készítése X1, X4 és Y alapján
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df["X1"], df["X4"], df["Y"], c='blue', marker='o')

ax.set_xlabel("X1")
ax.set_ylabel("X4")
ax.set_zlabel("Y")
ax.set_title("3D pontdiagram: X1 - X4 - Y")
# Példa: csak X1 = 50 és 300 között, X4 = 200 és 1000 között jelenjenek meg az adatok
ax.set_xlim(50, 300)
ax.set_ylim(200, 1000)
ax.set_zlim(1200, 1500)
plt.show()


# Ábra inicializálása
plt.figure(figsize=(8, 6))

# Külön kezeljük a Terv és Gradiens adatokat
for osztaly, marker in [('Terv', 'o'), ('Gradiens', 'x')]:
    subset = df[df["Osztály"] == osztaly]
    
    plt.scatter(
        subset["X1"], subset["X4"],
        c=subset["Y"],
        cmap='viridis',
        vmin=900,
        vmax=max,
        s=100,
        marker=marker,
        label=osztaly
    )

# Ábra címkék és színtér
plt.xlabel("X1")
plt.ylabel("X4")
plt.title("Mérési pontok elhelyezkedése a tervek és gradiensek esetén, továbbá Y értékek szemléltetése")
cbar = plt.colorbar()
cbar.set_label("Y érték")
plt.legend(title="Osztály")
plt.grid(True)
plt.tight_layout()
plt.show()