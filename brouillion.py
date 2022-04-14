from tkinter import *
import time
import random


def xy(event): # unused...
    xm, ym = event.x, event.y

def task():
    w=random.randint(1,1000)
    h=random.randint(1,1000)
    canvas.create_rectangle(w,h,w+150,h+150)
    tk.after_id = tk.after(1000,task)           

def callback(event):
    print("clicked2")    
    if tk.after_id:
        tk.after_cancel(tk.after_id)
        tk.after_id = None

if __name__ == '__main__':
    tk = Tk()
    tk.after_id = None
    canvas = Canvas(tk, width=200, height=200, background="grey")
    canvas.pack()
    canvas.bind("<Button-1>", callback)        
    task() # tk.after(1000,task)

    tk.mainloop()   