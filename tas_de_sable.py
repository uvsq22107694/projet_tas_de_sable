#########################################
# groupe MI TD3
# Basile Lauriola
# Camilia Boukebouche
# Julien Hrelja
# https://github.com/uvsq22107694/projet_tas_de_sable
# https://github.com/uvsq-info/l1-python
#########################################

# import des librairies

import tkinter as tk
import random

# définition d'une constante (cap)

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

# définition des variables globales


# définition des fonctions (docstring)


# programme principal définition des widgets/événements

root = tk.Tk()
root.title("Mon dessin")

# gestion des événements

bouton1 = tk.Button(root, text="Aléatoire", font = ("helvetica", "10"), bg="pink"
                  ) # création du widget
bouton1.grid(row=2, column=0) # positionnement du widget

canvas = tk.Canvas(root, bg="black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

canvas.grid(row=1, column=0)

# Fin de votre code


root.mainloop()
