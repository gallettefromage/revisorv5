from tkinter import *
import os
from PIL import ImageTk, Image
import Mathema
from tkinter import ttk


class init:
    def __init__(self, fenetre, boite):

                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("bouton_math.py", "image/image_prin/math.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(image.width//1), int(image.height//1)))
                self.image = ImageTk.PhotoImage(image)
                self.fond = Button(boite, image = self.image, command=lambda:self.mathématique(fenetre, boite))
                self.fond.image = self.image 
                self.fond.place(x = 50, y=150)
    
    def mathématique(self, fenetre, boite):
            boite.destroy()
            run= Mathema.Code(fenetre)