#########################################
# groupe MI TD3
# Basile Lauriola
# Camilia Boukebouche
# Julien Hrelja
# https://github.com/uvsq22107694/projet_tas_de_sable
# https://github.com/uvsq-info/l1-python
#########################################

# import des librairies

from lib2to3.pgen2 import grammar
import tkinter as tk
import random
from turtle import width

# définition d'une constante (cap)

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
GRILLE_WIDTH, GRILLE_HEIGHT = 20, 20

# définition des variables globales

global grille_aleatoire
grille_aleatoire = []

for i in range(GRILLE_WIDTH):
    grille_aleatoire.append([])
    for h in range(GRILLE_HEIGHT):
        grille_aleatoire[i].append(0)

# définition des fonctions (docstring)

def affiche():
    
    global grille_aleatoire

    coul = ["#FFFFFF", "#FF3200", "#FF4B00",
            "#FF6400", "#FF7D00", "#FF9600",
            "#FFAF00", "#FFC800", "#FFE100"]

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            valeurs = grille_aleatoire[i][h]

            couleur=coul[valeurs]

            canvas.create_rectangle(
                i*(CANVAS_WIDTH//GRILLE_WIDTH),
                h*(CANVAS_WIDTH//GRILLE_WIDTH),
                (i*(CANVAS_WIDTH//GRILLE_WIDTH))+CANVAS_WIDTH//GRILLE_WIDTH,
                (h*(CANVAS_WIDTH//GRILLE_WIDTH))+CANVAS_WIDTH//GRILLE_WIDTH,
                fill=couleur,
                width=1,
                outline="black"
            )

def aleatoire():

    global grille_aleatoire

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            grille_aleatoire[i][h] = random.randint(0,3)

    affiche()

def vide():
    
    global grille_aleatoire

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            grille_aleatoire[i][h] = 0

    affiche()

def algo_principale():

    global grille_aleatoire

    for i in range(GRILLE_WIDTH):
    
        for h in range(GRILLE_HEIGHT):

            if(grille_aleatoire[i][h] >= 4):
                grille_aleatoire[i-1][h-1] += 1
                grille_aleatoire[i-1][h+1] += 1
                grille_aleatoire[i+1][h-1] += 1
                grille_aleatoire[i+1][h+1] += 1
            


# programme principal définition des widgets/événements

root = tk.Tk()
root.title("Mon dessin")

# gestion des événements

bouton1 = tk.Button(root, text="Aléatoire", font = ("helvetica", "10"), bg="pink",command=aleatoire
                  ) # création du widget
bouton1.grid(row=2, column=0) # positionnement du widget

bouton2 = tk.Button(root, text="Vider", font = ("helvetica", "10"), bg="pink",command=vide
                  ) # création du widget
bouton2.grid(row=2, column=1) # positionnement du widget

bouton3 = tk.Button(root, text="Commencer", font = ("helvetica", "10"), bg="pink",command=algo_principale
                  ) # création du widget
bouton3.grid(row=2, column=2) # positionnement du widget

canvas = tk.Canvas(root, bg="black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT, borderwidth=0)

canvas.grid(row=1, column=0,columnspan=3)

# Fin de votre code


root.mainloop()
