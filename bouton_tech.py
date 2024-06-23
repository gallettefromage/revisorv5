from tkinter import *
import os
from PIL import ImageTk, Image
import technologie
from tkinter import ttk


class init:
    def __init__(self, fenetre, boite):

                chemin_actuel = os.path.abspath(__file__)
                chemin_actuel = chemin_actuel.replace("bouton_tech.py", "image/image_prin/tech.png")
                image = Image.open(chemin_actuel)
                image = image.resize((int(image.width//1), int(image.height//1)))
                self.image = ImageTk.PhotoImage(image)
                self.fond = Button(boite, image = self.image, command=lambda:self.technologie(fenetre, boite))
                self.fond.image = self.image 
                self.fond.place(x = 1200, y=150)
    
    def technologie(self, fenetre, boite):
            boite.destroy()
            run= technologie.Code(fenetre)