from tkinter import *
import os
from PIL import ImageTk, Image
import physique_chimie
from tkinter import ttk


class init:
    def __init__(self, fenetre, boite):

                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("bouton_pch.py", "image/image_prin/phis.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(image.width//1), int(image.height//1)))
                self.image = ImageTk.PhotoImage(image)
                self.fond = Button(boite, image = self.image, command=lambda:self.physique(fenetre, boite))
                self.fond.image = self.image 
                self.fond.place(x = 350, y=150)
    
    def physique(self, fenetre, boite):
            boite.destroy()
            run= physique_chimie.code(fenetre)