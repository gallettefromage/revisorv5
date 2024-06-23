from tkinter import *
import random

class code:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.titre_mth = Label(self.fenetre, text = "Physique Chimie", font = ("Algerian",40))
        self.titre_mth.place(x=320,y=20)
        self.parti_qts = Frame(self.fenetre, height= 720, width= 1080)
        self.parti_qts.place(x=0,y=100)

        self.choisir_question_aléatoirement()


    def choisir_question_aléatoirement(self):
        self.parti_qts.destroy()
        self.parti_qts = Frame(self.fenetre, height= 720, width= 1080)
        self.parti_qts.place(x=0,y=100)
        qts = random.randint(0,0)
        match qts:
            case 0:
                self.question.qts_cour.étape1(self)

    class question:
        def valider(self, réponse, réponse_donner, taille = 80):
           text = réponse_donner
           self.parti_qts.destroy()
           self.parti_qts = Frame(self.fenetre, height= 720, width= 1080)
           self.parti_qts.place(x=0,y=100)
           if  text in réponse:
               self.question.bonne_réponse(self, réponse, taille)
           else:
                self.question.mauvaise_réponse(self, réponse, taille)
                
        def bonne_réponse(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Bravo :\n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)

        def mauvaise_réponse(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Dommage :\n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00) 
        

        class qts_cour:

            
            def étape1(self):
                self.compteur = -1
                base_de_donné = [[["-Un atome est constitué d'un ", "noyaux", " au centre"], [",autour duquel gravitent des ", "électrons", " situés dans le nuage électronique (ou cortège électronique)."]],
                                    [["-L'électron possède une charge ", "négative", " . "], ["Le noyau de l'atome est constitué de particules appelées les ", "nucléons", " ."], ["Il s'agit des ", "neutrons", ", électriquement neutres"], [", et des ", "protons", ", chargés positivement." ]],
                                    [["-Le nombre de protons de l'atome, caractérisé par le numéro atomique noté Z, est égal au nombre d'", "électrons", " . "], [" La charge électrique totale d'un atome est nulle, on dit qu'il est ", "électriquement neutre", " ."]],
                                    [["-La dimension du noyau de l'atome est de l'ordre de ", "1E-15 m", " . "], ["Elle est environ 1E5 (= 10 puissance 5) fois ", "inférieure", " à celle de l'atome : 1E10 m."], ["L'atome est donc essentiellement constitué de vide : on dit qu'il a une structure ,", "lacunaire", " ."]],
                                    [["-Pour identifier les ions chlorures Cl-, cuivre II Cu²+, fer Fe²+ et fer Fe3+, on utilise des ", "test de reconnaissance", " ."], ["-Lorsqu'on mélange avec certaines subtances, il se forme des ", "précipités", "  de différentes couleurs."]],
                                    [["-Le pH est une grandeur qui mesure l'","acidité",""], [" ou la ", "basicité", " d'une solution"], ["; il n'a pas d'", "unité", " ."]],
                                    [["-Une solution acide a un pH ", "inférieur" , " à 7."], ["-Une solution basique a un pH ","supérieur", " à 7."], [" Une solution neutre a un pH ","égal"," à 7."]],
                                    [["- L'ion responsable de l'acidité d'une solution est l'ion ","hydrogène H+",";"],[" l'ion responsable de la basicité d'une solution est l'ion ","hydroxyde HO-"," ."]],
                                    [["- Les acides et les bases sont des produits ","corrosifs", " ( ils rongent )"],[" ; pour l'indiquer on utilise un ","pictogramme"," de sécurité."]],
                                    [["- Le pH d'une solution acide ","augmente"," lorsqu'on la dilue (il se rapproche de 7)"], [" ; le pH d'une solution basique ","diminue"," lorsqu'on la dilue (il se rapproche de 7)."]],
                                    [["-ATTENTION !! Il faut toujours verser l'acide dans l'eau pour éviter les ","éclaboussures"," ."]],
                                    [["- Une source d'énergie est dite ","renouvelable"," si elle est inépuisable à l'échelle de la vie humaine. Exemples : le Soleil, le vent."],["- Une source d'énergie est dite ","non renouvelable"," si elle s'épuise à l'échelle de la vie humaine. Exemples : le pétrole, le charbon, le gaz naturel, l'uranium."]],
                                    [["- L'énergie peut être ","convertie"," (ou être transformée) d'une forme dans une autre."],[" La conversion s'effectue dans un objet ou un système que l'on nomme un ","convertisseur"," ."]],
                                    [["- Au cours d'une chute, un objet gagne de l'énergie ","cinétique", ""],[" ; elle dépend de la ","vitesse"," notée v"],[" et de la ","masse",""],[" : elle augmente si la masse de l'objet ","augmente",""],[" et ou si la vitesse de l'objet ","augmente"," ."]],
                                    [["-La puissance nominale d'un appareil électrique est la puissance électrique reçue par un appareil pour qu'il fonctionne","normalement", ""],[" ; son unité est le ","Watt"," de symbole W"], [" ; la puissance est notée ","P"," ."],["Plus la puissance nominale est élevée, plus l'effet produit par l'appareil sera ","important"," (éclairage, aspiration, chauffage…)."]],
                                    [["- L'expression de l'énergie cinétique est : Ec = ","1/2xmxv²",""], ["- La vitesse moyenne est : v =","d/t", ""], ["avec :Ec en ","Joule", " (J)"],["avec :m (masse) en ","kilogramme", " (Kg)"],["avec :v en ","mètre par seconde", " (m/s)"],["avec :d en ","mètre", " (m)"],["avec :t en ","seconde", " (s)"]]
                                    ]
                self.qts = base_de_donné[random.randint(0, ((len(base_de_donné))-1))]
                self.compteur_max = len(self.qts)-1
                self.cadre = Frame(self.parti_qts, background='black')
                self.cadre.place(x=0, y=490, width=800, height=60)

                self.interface = Entry(self.cadre, width=20, font=("Elephant", 30), bg='white')
                self.interface.place(x=5, y=5, width=790, height=50)

                self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20))
                self.Valider.place(x=805, y=490)

                self.text_final = ""
                self.vrai_réponse = Label(self.parti_qts)
                self.bouton_suivant = Button(self.parti_qts)
                self.noite2 = Frame(self.parti_qts)
                self.question.qts_cour.étape2(self)
                
                
            def étape2(self):
                self.interface.delete(0, 'end')
                self.noite2.destroy()
                if not self.compteur == self.compteur_max:
                    self.compteur +=1
                    if not self.compteur == 0:
                        self.text_final += "\n"
                    self.question.qts_cour.étape3(self)
                else:
                    self.choisir_question_aléatoirement(self)
            
            def étape3(self):

                self.parti_qts.place(x=0,y=100)
                
                text_à_trou = self.qts[self.compteur][0]
                for i in range(1, (len(self.qts[self.compteur][1]))):
                    text_à_trou += "."
                text_à_trou += self.qts[self.compteur][2]
                cpteur = 0
                for i in text_à_trou:
                    self.text_final += i
                    if i == "\n":
                        cpteur = 0
                    if cpteur == 80:
                        self.text_final += "\n"
                        cpteur = 0
                    cpteur+=1
                réponse = [self.qts[self.compteur][1].lower()]
                self.question_posé = Label(self.parti_qts, text = self.text_final, font = ("", 20))
                self.question_posé.place(x = 0, y = 0)
                self.Valider.config(command = lambda : self.question.qts_cour.valider(self, réponse =réponse, réponse_donner=self.interface.get().lower()))

            def valider(self, réponse, réponse_donner, taille = 80):
                for i in range(20):
                    self.text_final = self.text_final.replace("..", ".")
                self.text_final = self.text_final.replace(".", réponse[0])
                self.parti_qts.place_forget()

                self.noite2 = Frame(self.fenetre, height= 720, width= 1080)
                self.noite2.place(x=0,y=100)
                text = réponse_donner
                if  text in réponse:
                    self.question.qts_cour.bonne_réponse(self, réponse, taille)
                else:
                        self.question.qts_cour.mauvaise_réponse(self, réponse, taille)
                        
            def bonne_réponse(self, réponse, taille):

                self.vrai_réponse = Label(self.noite2, text = f'Bravo :\n{réponse[0]}', font=("", taille))
                self.vrai_réponse.pack(expand=YES)
                self.bouton_suivant = Button(self.noite2, text = "Suivant", font = ("", 20),command=lambda:self.question.qts_cour.étape2(self))
                self.bouton_suivant.place(x = 00, y = 00)

            def mauvaise_réponse(self, réponse, taille):
                self.vrai_réponse.destroy()
                self.bouton_suivant.destroy()
                self.vrai_réponse = Label(self.noite2, text = f'Dommage :\n{réponse[0]}', font=("", taille))
                self.vrai_réponse.pack(expand=YES)
                self.bouton_suivant = Button(self.noite2, text = "Suivant", font = ("", 20),command=lambda:self.question.qts_cour.étape2(self))
                self.bouton_suivant.place(x = 00, y = 00) 
                
                    

