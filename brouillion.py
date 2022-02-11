import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
TAILLE_REC_X,TAILLE_REC_Y = 400, 400

root = tk.Tk()
root.title("Mon dessin")
global coul,objets
coul,freeze = False,False
objets = []

# Début de votre code

def clic_rec(event):
    global coul,freeze
    
    if(event.x < CANVAS_WIDTH-TAILLE_REC_X or event.y < CANVAS_HEIGHT-TAILLE_REC_Y \
            or event.x > TAILLE_REC_X or event.y > TAILLE_REC_Y or freeze == True):

        freeze=True
    else:
        if(coul == False):
            canvas.itemconfigure(1,fill="blue")
            coul = True
        else:
            canvas.itemconfigure(1,fill="red")
            coul = False

def reset():
    global freeze,coul
    freeze,coul = False,False
    canvas.itemconfigure(1,fill="red")
    print("test")

bouton1 = tk.Button(root, text="Recommencer", font = ("helvetica", "10"), bg="pink", command=reset
                  ) # création du widget
bouton1.grid(row=2, column=0) # positionnement du widget

root.bind("<Button-1>", clic_rec)

canvas = tk.Canvas(root, bg="black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

canvas.create_rectangle(100,100,400,400,fill="red")

canvas.grid(row=1, column=0, rowspan=1, columnspan=1)

# Fin de votre code


root.mainloop()