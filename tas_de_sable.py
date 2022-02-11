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
from turtle import width

# définition d'une constante (cap)

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
GRILLE_WIDTH, GRILLE_HEIGHT = 100, 100

# définition des variables globales


# définition des fonctions (docstring)

def aleatoire():

    coul = ["#FF1900", "#FF3200", "#FF4B00",
            "#FF6400", "#FF7D00", "#FF9600",
            "#FFAF00", "#FFC800", "#FFE100"]

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            couleur=coul[random.randint(0,8)]
            
            canvas.create_rectangle(i*(CANVAS_WIDTH//GRILLE_WIDTH),h*(CANVAS_WIDTH//GRILLE_WIDTH),i*(CANVAS_WIDTH//GRILLE_WIDTH)+5,h*(CANVAS_WIDTH//GRILLE_WIDTH)+5,fill=couleur,width=0)
            


# programme principal définition des widgets/événements

root = tk.Tk()
root.title("Mon dessin")

# gestion des événements

bouton1 = tk.Button(root, text="Aléatoire", font = ("helvetica", "10"), bg="pink",command=aleatoire
                  ) # création du widget
bouton1.grid(row=2, column=0) # positionnement du widget

canvas = tk.Canvas(root, bg="black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT, borderwidth=0)

canvas.grid(row=1, column=0)

# Fin de votre code


root.mainloop()
