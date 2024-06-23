from tkinter import *
import random


class Code:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.titre_mth = Label(self.fenetre, text = "Technologie", font = ("French Script MT",80))
        self.titre_mth.place(x=420,y=0)
        self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
        self.parti_qts.place(x=0,y=125)
        self.fenetre.geometry("2000x780")

        self.choisir_question_aléatoirement()


    def choisir_question_aléatoirement(self):
        self.parti_qts.destroy()
        self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
        self.parti_qts.place(x=0,y=125)
        qts = random.randint(0,0)
        match qts:
            case 0:
                qts = random.randint(0,0)
                match qts:
                    case 0:
                        self.question.Algorigrame.Feu_tricolore(self)
    class question:
        def valider(self, réponse, réponse_donner, taille = 80):
           text = réponse_donner
           self.parti_qts.destroy()
           self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
           self.parti_qts.place(x=0,y=100)
           if  text in réponse:
               self.question.bonne_réponse(self, réponse, taille)
           else:
                self.question.mauvaise_réponse(self, réponse, taille)
                
        def bonne_réponse(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Bien jouer,\nla bonne réponse\nétait effectivement :\n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)

        def mauvaise_réponse(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Dommage,\n la bonne réponse\nétait : \n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)  

        class Algorigrame:
            def robinet(self):
                
                self.énoncer = Label(self.parti_qts, text = ("Faite l'algorigrame d'un robinet automatique qui : "+
                                                             "   - lorsqu'il détecte une main s'ouvre pendant 3 secondes puis se referme."), font = ("", 40))
                self.énoncer.place(x=20,y=20)

                self.image = Canvas(self.parti_qts, width=300, height=300)
                self.image.place(x = 300, y = 100)
                points = [0,280, 280, 280, 280, 10]
                self.image.create_polygon(points, fill='white', outline='black')

                self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20))
                self.Valider.place(x=100, y=500)
 



