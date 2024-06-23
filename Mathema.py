from tkinter import *

import subprocess
import sys
try:
    print("importation de random")
    import random
except ImportError:
    print(f"Le module random n'est pas installé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "random"])
    print(f"Le module random a été installé avec succès.")
    import random
try:
    print("importation de sympy")
    from sympy import symbols, solve, Eq, sympify, simplify, expand, factor
except ImportError:
    print(f"Le module sympy n'est pas installé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"])
    print(f"Le module sympy a été installé avec succès.")
    from sympy import symbols, solve, Eq, sympify, simplify, expand, factor
try:
    print("importation de statistics")
    from statistics import mean, median
except ImportError:
    print(f"Le module statistics n'est pas installé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "statistics"])
    print(f"Le module statistics a été installé avec succès.")
    from statistics import mean, median
class Code:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.titre_mth = Label(self.fenetre, text = "Mathematiques", font = ("Algerian",40))
        self.titre_mth.place(x=320,y=20)
        self.parti_qts = Frame(self.fenetre, height= 720, width= 1080)
        self.parti_qts.place(x=0,y=100)

        self.choisir_question_aléatoirement()


    def choisir_question_aléatoirement(self):
        self.parti_qts.destroy()
        self.parti_qts = Frame(self.fenetre, height= 720, width= 1080)
        self.parti_qts.place(x=0,y=100)
        qts = random.randint(0,11)
        match qts:
            case 0:
                self.question.gémoétrie.triangle.rectangle(self)
            case 1:
                self.question.calcul.calcul_literral.expression_avec_x(self)
            case 2:
                self.question.calcul.calcul_literral.factotisation(self)
            case 3:
                self.question.calcul.calcul_literral.identité_remarquable.identité_remarquable_1(self)
            case 4:
                self.question.calcul.statistique.moyenne(self)
            case 5:
                self.question.calcul.statistique.étendu(self)
            case 6:
                self.question.calcul.statistique.médiane(self)
            case 7:
                self.question.calcul.equation.produit_nul(self)
            case 8:
                self.question.calcul.statistique.probabilité(self)
            case 9:
                self.question.calcul.calcul_literral.double_disributivité(self)
            case 10:
                self.question.calcul.fonction.afine_touver_a_et_b(self)
            case 11:
                self.question.calcul.calcul_literral.identité_remarquable.identité_remarquable_2(self)


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
            vrai_réponse = Label(self.parti_qts, text = f'Bien jouer,\nla bonne réponse\nétait effectivement :\n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)

        def mauvaise_réponse(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Dommage,\n la bonne réponse\nétait : \n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)  
            
        class gémoétrie:
            class triangle:

                def rectangle(self):
                    self.énoncer = Label(self.parti_qts, text = "Le triangle ABC est-il rectangle en A ?(répondre par Vrai ou Faux)", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    self.image = Canvas(self.parti_qts, width=300, height=300)
                    self.image.place(x = 300, y = 100)
                    points = [0,280, 280, 280, 280, 10]
                    self.image.create_polygon(points, fill='white', outline='black')
                    Point_A = Label(self.parti_qts, text = "A", font = ("Elephant", 20))
                    Point_A.place(x = 580, y = 385)
                    Point_B = Label(self.parti_qts, text = "B", font = ("Elephant", 20))
                    Point_B.place(x = 570, y = 70)
                    Point_C = Label(self.parti_qts, text = "C", font = ("Elephant", 20))
                    Point_C.place(x = 270, y = 360)
                    aléa = random.randint(1,2)
                    if aléa == 1:
                        self.longeur_1 = random.randint(1,40)
                        self.longeur_2 = random.randint(1, 40)
                        if self.longeur_1 > self.longeur_2:  
                            self.hypotenuse = self.longeur_1 + random.randint(1,10)
                        else:  
                            self.hypotenuse = self.longeur_2 + random.randint(1,10)
                    else:
                        liste= [[3, 4, 5],[5, 12, 13],[6, 8, 10], [7, 24, 25],[8, 15, 17],[9, 12, 15],[9, 40, 41], [10, 24, 26], [12, 16, 20],[12, 35, 37],[15, 20, 25], [15, 36, 39], [16, 30, 34], [18, 24, 30], [20, 21, 29], [20, 48, 52], [21, 28, 35], [24, 32, 40], [27, 36, 45], [30, 40, 50]]
                        alea = random.choice(liste)
                        self.longeur_1 = alea[0]
                        self.longeur_2 = alea[1]
                        self.hypotenuse = alea[2]
                    self.longeur_1_text = Label(self.parti_qts, text = self.longeur_1, font = ("Elephant", 30))
                    self.longeur_1_text.place(x = 600, y = 240)
                    self.longeur_2_text = Label(self.parti_qts, text = self.longeur_2, font = ("Elephant", 30))
                    self.longeur_2_text.place(x = 425, y = 385)
                    self.hypotenuse_text = Label(self.parti_qts, text = self.hypotenuse, font = ("Elephant", 30))
                    self.hypotenuse_text.place(x = 385, y = 175)

                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=400, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=390, height=50)

                    if (self.longeur_1 * self.longeur_1) + (self.longeur_2 * self.longeur_2) == self.hypotenuse*self.hypotenuse:
                        réponse = ["Vrai", "vrai", "VRAI"]
                    else:
                        réponse = ["Faux", "faux", "FAUX"]
                    
                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=self.interface.get()))
                    self.Valider.place(x=405, y=490)
                
                class trigo:
                    def trouver_longeur(self):
                        pass
                        
                    def trouver_angle(self):
                        pass
        
        class calcul:
            class calcul_literral:
                def expression_avec_x(self):
                    self.énoncer = Label(self.parti_qts, text = "Quel est le resultat déveloper et réduit de l'expression ?\n(répondre avec des lettres en minuscules et respecter l'ordre : y² --> y --> nombre))", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    expression = str(random.randint(1, 10)) + random.choice(["", "y", "y²"])
                    for i in range(random.randint(2,4)):
                        aléa = random.randint(0,1)
                        if aléa == 0:
                            expression += "("+str(random.randint(1,10))+random.choice(["", "y"])+random.choice([" + "," - "])+str(random.randint(1,10))+random.choice(["", "y"])+")"
                        else: 
                            expression += random.choice([" + "," - "," x "])
                            expression += str(random.randint(1, 10)) + random.choice(["", "y", "y²"])
                    self.question_posé = Label(self.parti_qts, text = expression, font = ("", 70))
                    self.question_posé.place(x = 50, y = 250)

                    y = symbols('y')
                    expression = sympify(expression.replace("²", "**2").replace("x", "*").replace("y", "*y").replace("(", "*("))
                    expression = simplify(expression)
                    expression = expand(expression)
                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[expression]
                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=expand(simplify(sympify(self.interface.get().replace("²", "**2").replace("x", "*").replace("y", "*y").replace("(", "*(").replace(",",".")))), taille = 70))
                    self.Valider.place(x=805, y=490)

                def factotisation(self):
                    self.énoncer = Label(self.parti_qts, text = "Quel est le resultat factoriser et réduit de l'expression ?\n(répondre avec des lettres en minuscules et respecter l'ordre : y² --> y --> nombre)", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    expression_commune = random.choice(["( "+str(random.randint(3,20)) + random.choice(["", "y" ,"y²"])+random.choice([" + "," - "," x "])+str(random.randint(3,20)) + random.choice(["", "y" ,"y²"])+" )", str(random.randint(3,20)) + random.choice(["", "y" ,"y²"])])
                    expression = (random.choice(
                                                ["( "+str(random.randint(3,20)) + 
                                                random.choice(["", "y" ,"y²"])+
                                                random.choice([" + "," - "])+
                                                str(random.randint(3,20)) +
                                                random.choice(["", "y" ,"y²"])+" )", 
                                                ####################################
                                                #             Ou                   #
                                                ####################################
                                                str(random.randint(3,20)) + 
                                                random.choice(["", "y" ,"y²"])])+
                                                " x "+
                                                expression_commune + 
                                                random.choice([" + "," - "])+
                                                random.choice(["( "+str(random.randint(3,20)) + 
                                                random.choice(["", "y" ,"y²"])+
                                                random.choice([" + "," - "])+
                                                str(random.randint(3,20)) + random.choice(["", "y" ,"y²"])+" )", 
                                                str(random.randint(3,20)) + 
                                                random.choice(["", "y" ,"y²"])])+
                                                " x "+
                                                expression_commune)

                    self.question_posé = Label(self.parti_qts, text = expression, font = ("", 30))
                    self.question_posé.place(x = 50, y = 250)
                    y = symbols('y')
                    expression = sympify(expression.replace("²", "**2").replace("x", "*").replace("y", "*y"))
                    
                    expression = factor(expression)
                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[expression]
                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=(factor(sympify(self.interface.get().replace("²", "**2").replace("x", "*").replace("y", "*y").replace(",",".")))), taille = 50))
                    self.Valider.place(x=805, y=490)    

                def double_disributivité(self):
                    self.énoncer = Label(self.parti_qts, text = "Quel est le resultat factoriser et réduit de l'expression ?\n(répondre avec des lettres en minuscules et respecter l'ordre : y² --> y --> nombre))", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    a = ("( "+str(random.randint(3,20)) + 
                            random.choice(["", "y" ,"y²"])+
                            random.choice([" + "," - "])+
                            str(random.randint(3,20)) + 
                            random.choice(["", "y" ,"y²"])+
                            " )")
                    b = ("( "+str(random.randint(3,20)) + 
                            random.choice(["", "y" ,"y²"])+
                            random.choice([" + "," - "])+
                            str(random.randint(3,20)) + 
                            random.choice(["", "y" ,"y²"])+
                            " )")
                    
                    expression =a + " x " + b

                    self.question_posé = Label(self.parti_qts, text = expression, font = ("", 30))
                    self.question_posé.place(x = 50, y = 250)
                    expression = sympify(expression.replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y"))
                    
                    expression = expand(simplify(expression))
                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[expression]
                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=(expand(simplify(sympify(self.interface.get().replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y").replace(",","."))))), taille = 50))
                    self.Valider.place(x=805, y=490)
                

                class identité_remarquable:
                    def identité_remarquable_1(self):
                        self.énoncer = Label(self.parti_qts, text = "Quel est le resultat déveloper et réduit de l'expression ?\n(répondre avec des lettres en minuscules et respecter l'ordre : y² --> y --> nombre))", font = ("", 20))
                        self.énoncer.place(x=20,y=20)
                        a = str(random.randint(2, 15)**2) + random.choice(["y²", "y²" ""])
                        if a .count("y²"): 
                            b = str(random.randint(2, 15)**2)
                        else:
                            b = str(random.randint(2, 15)**2) + "y²"
                        expression =a + "-" + b

                        self.question_posé = Label(self.parti_qts, text = expression, font = ("", 30))
                        self.question_posé.place(x = 50, y = 250)
                        y = symbols('y')
                        expression = sympify(expression.replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y"))
                        
                        expression = factor(expression)
                        cadre = Frame(self.parti_qts, background='black')
                        cadre.place(x=0, y=490, width=800, height=60)

                        self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                        self.interface.place(x=5, y=5, width=790, height=50)
                        réponse=[expression]
                        self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=(factor(sympify(self.interface.get().replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y").replace(",",".")))), taille = 50))
                        self.Valider.place(x=805, y=490)
                    
                    
                    def identité_remarquable_2(self):
                        self.énoncer = Label(self.parti_qts, text = "Quel est le resultat déveloper et réduit de l'expression ?\n(répondre avec des lettres en minuscules et respecter l'ordre : y² --> y --> nombre))", font = ("", 20))
                        self.énoncer.place(x=20,y=20)
                        a = str(random.randint(2, 15)**2) + random.choice(["y²", "y²" ""])
                        if a .count("y²"): 
                            b = str(random.randint(2, 15)**2)
                        else:
                            b = str(random.randint(2, 15)**2) + "y²"
                        expression =a + "-" + b

                        self.question_posé = Label(self.parti_qts, text = expression, font = ("", 30))
                        self.question_posé.place(x = 50, y = 250)
                        y = symbols('y')
                        expression = sympify(expression.replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y"))
                        
                        expression = factor(expression)
                        cadre = Frame(self.parti_qts, background='black')
                        cadre.place(x=0, y=490, width=800, height=60)

                        self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                        self.interface.place(x=5, y=5, width=790, height=50)
                        réponse=[expression]
                        self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=(factor(sympify(self.interface.get().replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y").replace(",",".")))), taille = 50))
                        self.Valider.place(x=805, y=490)
                    
                    
            class statistique:
                def moyenne(self):
                    self.énoncer = Label(self.parti_qts, text = "Quelle est la moyenne de cette suite de nombre: ?\n(répondre soit par une fraction, soit la valeur exacte)", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    suite = []
                    text = ""
                    for i in range(random.randint(5,10)):
                        suite.append(random.randint(1,random.randint(20,200)))
                        text = text + str(suite[i])+" ; "
                    text = text + "#end"
                    text = text.replace(" ; #end", "")
                    self.question_posé = Label(self.parti_qts, text = text, font = ("", 30))
                    self.question_posé.place(x = 50, y = 250)

                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[mean(suite)]

                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=eval(self.interface.get()) , taille = 80))
                    self.Valider.place(x=805, y=490)
                
                def étendu(self):
                    self.énoncer = Label(self.parti_qts, text = "Quelle est l'étendu de cette suite de nombre: ?\n(répondre soit par une fraction, soit la valeur exacte)", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    suite = []
                    text = ""
                    for i in range(random.randint(5,10)):
                        suite.append(random.randint(1,random.randint(20,200)))
                        text = text + str(suite[i])+" ; "
                    text = text + "#end"
                    text = text.replace(" ; #end", "")
                    self.question_posé = Label(self.parti_qts, text = text, font = ("", 30))
                    self.question_posé.place(x = 50, y = 250)

                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[(max(suite)-min(suite))]

                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=eval(self.interface.get()) , taille = 80))
                    self.Valider.place(x=805, y=490)

                def médiane(self):
                    self.énoncer = Label(self.parti_qts, text = "Quelle est la médiane de cette suite de nombre ?\n(répondre soit par une fraction, soit la valeur exacte, si le nombre de nombre est pair,\n mettre la moyenne des deux nombre du milieux )", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    suite = []
                    text = ""
                    for i in range(random.randint(5,10)):
                        suite.append(random.randint(1,random.randint(20,200)))
                        text = text + str(suite[i])+" ; "
                    text = text + "#end"
                    text = text.replace(" ; #end", "")
                    self.question_posé = Label(self.parti_qts, text = text, font = ("", 30))
                    self.question_posé.place(x = 50, y = 250)

                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[median(suite)]


                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=eval(self.interface.get()) , taille = 80))
                    self.Valider.place(x=805, y=490)

                def probabilité(self):
                    self.énoncer = Label(self.parti_qts, text = "On lance un dés trucqué è six faces, on obtiens ces resultats :", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    suite = []
                    text = ""
                    compteur = 0
                    for i in range(random.randint(15,20)):
                        suite.append(random.randint(1,6))
                        text = text + str(suite[i])+" ; "
                        compteur +=1
                        if compteur == 5:
                            compteur = 0
                            text = text + "\n"
                        
                    text = text + "#end"
                    text = text.replace(" ; #end", "").replace(" ; \n#end", "")
                    probabilité_recherché = random.randint(1,6)
                    réponse = suite.count(probabilité_recherché)/len(suite)
                    self.question_posé = Label(self.parti_qts, text = text, font = ("", 30))
                    self.question_posé.place(x = 200, y = 150)

                    self.énoncer_2 = Label(self.parti_qts, text = "Quelle est la probabilité de tombé sur : "+str(probabilité_recherché)+"\n(répondre soit par une fraction, soit la valeur exacte)", font = ("", 20))
                    self.énoncer_2.place(x=20,y=350)

                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[réponse]


                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=eval(self.interface.get()) , taille = 80))
                    self.Valider.place(x=805, y=490)

            class equation:
                def produit_nul(self):
                    self.énoncer = Label(self.parti_qts, text = "Quel est le resultat de l'équation?\n(séparer par un point virgule les solutions et écrire tous les résultat du plus petit\nau plus grand, pour finir, ne par écrire 0)", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    equation = (" ( " +
                                str(random.randint(1,10)) + 
                                "y" + random.choice([" + ", " - "]) + 
                                str(random.randint(1,100)) + 
                                " ) x ( " + 
                                str(random.randint(1,10)) + 
                                "y" + 
                                random.choice([" + ", " - "]) + 
                                str(random.randint(1,100))+
                                " )")
                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=0, y=490, width=800, height=60)

                    y = symbols("y")

                    self.question_posé = Label(self.parti_qts, text = equation + " = 0", font = ("", 30))
                    self.question_posé.place(x = 50, y = 250)
                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=790, height=50)
                    réponse=[solve(sympify(equation.replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y")))]

                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20),command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=sympify(self.interface.get().replace("²", "**2").replace("x", "*").replace(" y", "z").replace("y", "*y").replace("z", "y").replace(",",".").split(";")) , taille = 80))
                    self.Valider.place(x=805, y=490)
                
            class fonction:
                
                def afine_touver_a_et_b(self):
                    self.énoncer = Label(self.parti_qts, text = "fonction affine : Trouver A et trouver B?\n(répondre soit par une fraction, soit la valeur exacte)", font = ("", 20))
                    self.énoncer.place(x=20,y=20)
                    af1 = random.randint(1,20)
                    bf1 = random.randint(1,20)
                    f1 = "F("+str(af1)+") = " + str(bf1)
                    af2 =af1 +  random.randint(1,10)
                    bf2 = random.randint(1,30)
                    f2 = "F("+str(af2)+") = " + str(bf2)
                    self.question_posé = Label(self.parti_qts, text = f1 + "\n" + f2, font = ("", 30))
                    self.question_posé.place(x = 50, y = 250)

                    self.A = Label(self.parti_qts, text = "A : ", font = ("Elephant", 30))
                    self.A.place(x=0, y=490)
                    cadre = Frame(self.parti_qts, background='black')
                    cadre.place(x=60, y=490, width=200, height=60)

                    réponse_a = (bf1-bf2)/(af1-af2)
                    réponse_b = bf1-(af1*réponse_a)
                    réponse = [[réponse_a, réponse_b]]

                    self.interface = Entry(cadre, width=20, font=("Elephant", 30), bg='white')
                    self.interface.place(x=5, y=5, width=190, height=50)

                    self.B = Label(self.parti_qts, text = "B : ", font = ("Elephant", 30))
                    self.B.place(x=280, y=490)
                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=350, y=490, width=200, height=60)

                    
                    self.interface2 = Entry(cadre2, width=20, font=("Elephant", 30), bg='white')
                    self.interface2.place(x=5, y=5, width=190, height=50)


                    self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20),command = lambda : self.question.valider(self, réponse =réponse, réponse_donner=[eval(self.interface.get()),eval(self.interface2.get()) ] , taille = 80))
                    self.Valider.place(x=805, y=490)
