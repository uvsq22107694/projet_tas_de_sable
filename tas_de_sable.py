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
from tkinter import filedialog as fd
import tkinter as tk
import os
import random
import pickle
import marshal
from turtle import width

# définition d'une constante (cap)

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
GRILLE_WIDTH, GRILLE_HEIGHT = 100, 100
NOMBRE_GRAIN_MAX = 100

# définition des variables globales

global grille_aleatoire,arret,idduafter,afficherchiffre
grille_aleatoire = []
idduafter = None
arret = True
afficherchiffre = False

for i in range(GRILLE_WIDTH):
    grille_aleatoire.append([])
    for h in range(GRILLE_HEIGHT):
        grille_aleatoire[i].append(0)

# définition des fonctions (docstring)

def affiche(affchiffre):
    
    global grille_aleatoire,afficherchiffre

    if(affchiffre):
        
        if(afficherchiffre):
            afficherchiffre = False
        else:
            afficherchiffre = True

    coul = ["#FFFFFF", "#FFE100", "#FFC800", 
            "#FFAF00", "#FF9600", "#FF7D00", 
            "#FF6400", "#FF4B00", "#FF3200",
            "#000000"]

    canvas.delete("all")

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            valeurs = grille_aleatoire[i][h]

            if(valeurs > 8):
                couleur = coul[9]
            else:
                couleur = coul[valeurs]

            canvas.create_rectangle(
                h*(CANVAS_WIDTH/GRILLE_WIDTH),
                i*(CANVAS_WIDTH/GRILLE_WIDTH),
                (h*(CANVAS_WIDTH/GRILLE_WIDTH))+CANVAS_WIDTH//GRILLE_WIDTH,
                (i*(CANVAS_WIDTH/GRILLE_WIDTH))+CANVAS_WIDTH//GRILLE_WIDTH,
                fill=couleur,
                width=0,
            )
            if(afficherchiffre):
                if(valeurs > 8):
                    coultext = "white" 
                else: 
                    coultext = "black"

                canvas.create_text(
                    (CANVAS_WIDTH/GRILLE_WIDTH)/2 + (CANVAS_WIDTH/GRILLE_WIDTH)*h,
                    (CANVAS_HEIGHT/GRILLE_HEIGHT)/2 + (CANVAS_HEIGHT/GRILLE_HEIGHT)*i,
                    text=str(valeurs),
                    width=50,
                    fill=coultext
                )

def aleatoire():

    global grille_aleatoire

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            grille_aleatoire[h][i] = random.randint(0,NOMBRE_GRAIN_MAX)

    affiche(False)
    stop()

def vide():
    
    global grille_aleatoire

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            grille_aleatoire[i][h] = 0

    affiche(False)
    stop()

def algo_principale(para = True):

    global grille_aleatoire,idduafter,arret

    arret = True

    if(not para):
        
        while(arret):
            
            arret = False

            for i in range(GRILLE_WIDTH):
            
                for h in range(GRILLE_HEIGHT):

                    if(grille_aleatoire[i][h]>=4):
                        if(i != 0):
                            grille_aleatoire[i-1][h] += 1
                        if(i != GRILLE_WIDTH-1):
                            grille_aleatoire[i+1][h] += 1
                        if(h != 0):
                            grille_aleatoire[i][h-1] += 1
                        if(h != GRILLE_HEIGHT-1):
                            grille_aleatoire[i][h+1] += 1
                            
                        grille_aleatoire[i][h] -= 4
                        arret = True
        
        affiche(False)

    else:
        grille_temp = marshal.loads(marshal.dumps(grille_aleatoire))  

        for i in range(GRILLE_WIDTH):
        
            for h in range(GRILLE_HEIGHT):

                if(grille_aleatoire[i][h]>=4):
                    if(i != 0):
                        grille_temp[i-1][h] += 1
                    if(i != GRILLE_WIDTH-1):
                        grille_temp[i+1][h] += 1
                    if(h != 0):
                        grille_temp[i][h-1] += 1
                    if(h != GRILLE_HEIGHT-1):
                        grille_temp[i][h+1] += 1
                        
                    grille_temp[i][h] -= 4
                    arret = False

        grille_aleatoire = marshal.loads(marshal.dumps(grille_temp))  

       
        if(arret):
            stop()

        idduafter = root.after(10,algo_principale)

  
    if(para):
        affiche(False)
    
    

def stop():
    global idduafter

    root.after_cancel(idduafter)


def sauvegarde():
    global grille_aleatoire

    filetypes = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]

    file = fd.asksaveasfile(
            mode="wb",
            filetypes = filetypes,
            defaultextension = filetypes
            )

    pickle.dump(grille_aleatoire, file)

    file.close()

    affiche(False)

def charger():

    global grille_aleatoire

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
                initialdir=os.getcwd()+"/Grilles",
                filetypes=filetypes
                )

    with open(filename, "rb") as data:

        grille_aleatoire = pickle.load(data)

    data.close()

    affiche(False)

    
def max_stab():
    """Met des 3 dans la grille"""
    global grille_aleatoire

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            grille_aleatoire[h][i] = 6

    affiche(False)
    stop()

def addition():
    """addition la grille actuelle avec une grille sauvegarder"""
    global grille_aleatoire

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
                initialdir=os.getcwd()+"/Grilles",
                filetypes=filetypes
                )

    with open(filename, "rb") as data:

        grille_aleatoire_add = pickle.load(data)

    data.close()

    affiche(False)

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            grille_aleatoire[h][i] = grille_aleatoire[h][i] + grille_aleatoire_add[h][i]

    affiche(False)
    stop()

def identity():

    """identité"""

    global grille_aleatoire

    for i in range(GRILLE_WIDTH):

        for h in range(GRILLE_HEIGHT):

            grille_aleatoire[h][i] = 6

    grille_aleatoire = marshal.loads(marshal.dumps(grille_aleatoire))

    algo_principale(False)


    
    

# programme principal définition des widgets/événements

root = tk.Tk()
root.title("Mon dessin")


# gestion des événements

bouton_aleatoire = tk.Button(root, text="Aléatoire", font = ("helvetica", "10"), bg="pink",command=aleatoire
                  ) # création du widget
bouton_aleatoire.grid(row=2, column=0) # positionnement du widget

bouton_vider = tk.Button(root, text="Vider", font = ("helvetica", "10"), bg="pink",command=vide
                  ) # création du widget
bouton_vider.grid(row=2, column=1) # positionnement du widget

bouton_algo = tk.Button(root, text="Commencer", font = ("helvetica", "10"), bg="pink",command=lambda: algo_principale(True)
                  ) # création du widget
bouton_algo.grid(row=2, column=2) # positionnement du widget

bouton_stop = tk.Button(root, text="Stop", font = ("helvetica", "10"), bg="pink",command=stop
                  ) # création du widget
bouton_stop.grid(row=2, column=3) # positionnement du widget

bouton_sauvegarde = tk.Button(root, text="Sauvegarde", font = ("helvetica", "10"), bg="pink",command=sauvegarde
                  ) # création du widget
bouton_sauvegarde.grid(row=2, column=4) # positionnement du widget

bouton_charger = tk.Button(root, text="Charger", font = ("helvetica", "10"), bg="pink",command=charger
                  ) # création du widget
bouton_charger.grid(row=2, column=5) # positionnement du widget

bouton_chiffre = tk.Button(root, text="Afficher chiffre", font = ("helvetica", "10"), bg="pink",command=lambda: affiche(True)
                  ) # création du widget
bouton_chiffre.grid(row=2, column=6) # positionnement du widget

bouton_chiffre = tk.Button(root, text="addition", font = ("helvetica", "10"), bg="pink",command=addition
                  ) # création du widget
bouton_chiffre.grid(row=2, column=7) # positionnement du widget

bouton_chiffre = tk.Button(root, text="max stab", font = ("helvetica", "10"), bg="pink",command=max_stab
                  ) # création du widget
bouton_chiffre.grid(row=2, column=8) # positionnement du widget

bouton_chiffre = tk.Button(root, text="identity", font = ("helvetica", "10"), bg="pink",command=identity
                  ) # création du widget
bouton_chiffre.grid(row=2, column=9) # positionnement du widget

canvas = tk.Canvas(root, bg="white", width = CANVAS_WIDTH*1.5, height = CANVAS_HEIGHT, borderwidth=0)

canvas.grid(row=1, column=0,columnspan=10)

# Fin de votre code


root.mainloop()
