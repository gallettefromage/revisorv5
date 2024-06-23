from tkinter import *
import random


class Code:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.titre_mth = Label(self.fenetre, text = "Français", font = ("French Script MT",80))
        self.titre_mth.place(x=420,y=0)
        self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
        self.parti_qts.place(x=0,y=125)
        self.fenetre.geometry("2000x780")
        self.btn_ex = Button(self.parti_qts, text = "Mode exercice", font = ("", 40),command= lambda:self.choisir_question_aléatoirement())
        self.btn_ex.place(x=0, y=0)
        self.btn_qcm = Button(self.parti_qts, text = "Mode QCM", font = ("", 40),command= lambda:self.choisir_qcm_aléa())
        self.btn_qcm.place(x=0, y=200)
        self.score = 0
        self.score_sur = 0



    def choisir_question_aléatoirement(self):
        self.parti_qts.destroy()
        self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
        self.parti_qts.place(x=0,y=125)
        qts = random.randint(0,0)
        match qts:
            case 0:
                self.question.ortographe.réécriture(self)
    
    def choisir_qcm_aléa(self):
        self.parti_qts.destroy()
        self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
        self.parti_qts.place(x=0,y=125)
        qts = random.randint(0,10)
        match qts:
            case 0:
                self.question.QCM.text(self)
            case 1:
                self.question.QCM.Le_discours(self)
            case 2:
                self.question.QCM.limage(self)
            case 3:
                self.question.QCM.Le_verbe(self)
            case 4:
                self.question.QCM.Les_valeur_des_temps(self)
            case 5:
                self.question.QCM.laphrase(self)
            case 6:
                self.question.QCM.autour_du_mot(self)
            case 7:
                self.question.QCM.class_gramm(self)
            case 8:
                self.question.QCM.fonction_gramm(self)
            case 9:
                self.question.QCM.nom_et_gr_nom(self)
            case 10:
                self.question.QCM.les_figure_de_style(self)

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
            vrai_réponse = Label(self.parti_qts, text = f'Bien joué,\nla bonne réponse\nétait effectivement :\n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)

        def mauvaise_réponse(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Dommage,\n la bonne réponse\nétait : \n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)  
        
        def bonne_réponse_qcm(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Bien joué,\nla bonne réponse\nétait effectivement :\n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_qcm_aléa())
            bouton_suivant.place(x = 00, y = 00)
            self.score +=1
            self.score_sur +=1

        def mauvaise_réponse_qcm(self, réponse, taille):
            vrai_réponse = Label(self.parti_qts, text = f'Dommage,\n la bonne réponse\nétait : \n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_qcm_aléa())
            bouton_suivant.place(x = 00, y = 00)  
            self.score_sur +=1

        class ortographe:
            def réécriture(self):
                base_de_donné = [['en mettant "meurtrier" au pluriel.', 
                                    "Si le meurtrier se dénonce lui-même, il ne lui sera fait aucun mal, et il ne sera comdamné qu'a quitter le pays. Si l'un de ces complices le dénonce, il gagnera l'impunité.",
                                    "Si les meurtriers se dénoncent eux-mêmes, il ne leur sera fait aucun mal, et ils ne seront condamnés qu'à quitter le pays. Si l'un de leurs complices les dénonce, il gagnera l'impunité."],
                                 ['au passé composé.',
                                    "Ce soir-là, en sortant du travail, je cours me réfugier dans le premier bar, en face de la gare. Je m'assoie devant le baby-foot et je commande un whisky pour fêter mes trente-trois ans. Je tente de joindre Ana sur son portable, elle ne répond pas. Je m'acharne, compose son numéro à plusieurs reprises.",
                                    "Ce soir-là, en sortant du travail, je me suis réfugié dans le premier bar, en face de la gare. Je me suis assis devant le baby-foot et j'ai commandé un whisky pour fêter mes trente-trois ans. J'ai tenté de joindre Ana sur son portable, elle n'a pas répondu. Je me suis acharné, j'ai composé son numéro à plusieurs reprises."],
                                 ['en passant du discour direct au discour indirect.\n Vous commencerez le texte par "Il déclara aux policiers :"',
                                     "Une fois dans sa vie Akaki Akakiévitch fit preuve de fermeté; il declara aux policiers qu'ils n'avaient pas le droit de l'empê"]]
                
                réécriture_à_faire = base_de_donné[random.randint(0, 1)]
                
                texte = réécriture_à_faire[1]
                text_final = ""
                compteur = 0
                for index, char in enumerate(texte):
                    text_final += char
                    if compteur >= 40:
                        if texte[index + 1] == " ":

                            text_final += "\n"
                            compteur = 0

                    compteur += 1


                self.énoncer = Label(self.parti_qts, text = "Réécrivez ce passage " + réécriture_à_faire[0], font = ("", 40))
                self.énoncer.place(x=20,y=20)

                self.question_posé = Label(self.parti_qts, text = text_final, font = ("", 30))
                self.question_posé.place(x = 0, y = 100)

                cadre = Frame(self.parti_qts, background='black')
                cadre.place(x=1000, y=100, width=800, height=498)
                self.interface = Text(cadre, width=20,height=10, font=("Elephant", 30), bg='white')
                self.interface.place(x=5, y=5, width=790)
                réponse=réécriture_à_faire[2].lower().replace("\n", "")

                self.Valider = Button(self.parti_qts, text = "Valider", font = ("", 20), command = lambda : self.question.ortographe.valider_réécriture(self, réponse =réponse, réponse_donner=self.interface.get(1.0, END).replace("\n", "").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").lower() ))
                self.Valider.place(x=100, y=500)
            
            def valider_réécriture(self, réponse_donner, réponse):
                self.parti_qts.destroy()
                self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
                self.parti_qts.place(x=0,y=100)
                score = 1
                verif = [réponse_donner.split(" "), réponse.split(" ")]
                faute = []
                for i in range(0, len(verif[0])-1):
  
                    try:
                        if verif[0][i]== verif[1][i]:
                            score+=1
                        else:
                            faute.append([verif[0][i]," au lieu de ",verif[1][i]])

                    except:
                        print(str(i)+ "sur" + str(len(verif[1])))
                        break
                print(faute)
                text_faute = ""
                compteur = 0
                for i in range(len(faute)):
                    text_faute+=faute[i][0]
                    text_faute+=faute[i][1]
                    text_faute+=faute[i][2]
                    text_faute += "   "
                    if compteur == 3:
                        text_faute += "\n"
                        compteur = 0
                    compteur +=1
                score = str(score*100//len(verif[1]))
                vrai_réponse = Label(self.parti_qts, text = "           Score : "+score+ " %\n" + text_faute, font=("", 20))
                vrai_réponse.place(x = 0, y = 100)
                bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
                bouton_suivant.place(x = 00, y = 00)


        class QCM:
            def création_qts(self, base_de_donné):
                    qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                    self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                    self.énoncer.place(x=20,y=20)
                    réponse = [qts[1]]
                    self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                    self.score_affichage.place(x= 0, y=0)
                    aléa = random.randint(1,4)

                    cadre1 = Frame(self.parti_qts, background='black')
                    cadre1.place(x=60, y=100, width=80, height=80)
                    bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse_qcm(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse_qcm(self, réponse, 50))
                    bouton1.place(x=5, y=5, height=70, width=70)
                    text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                    text_1.place(x= 200, y=aléa*100)

                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=60, y=200, width=80, height=80)
                    bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse_qcm(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse_qcm(self, réponse , 50))
                    bouton2.place(x=5, y=5, height=70, width=70)
                    text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                    text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
                
                    cadre3 = Frame(self.parti_qts, background='black')
                    cadre3.place(x=60, y=300, width=80, height=80)
                    bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse_qcm(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse_qcm(self,réponse , 50))
                    bouton3.place(x=5, y=5, height=70, width=70)
                    text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                    text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
                
                    cadre4 = Frame(self.parti_qts, background='black')
                    cadre4.place(x=60, y=400, width=80, height=80)
                    bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse_qcm(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse_qcm(self,réponse , 50))
                    bouton4.place(x=5, y=5, height=70, width=70)
                    text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                    text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)
                    self.cache = Button(self.parti_qts,text = "Montrer", font= ("", 80), background='beige', activebackground='beige', command=lambda: self.cache.destroy())
                    self.cache.place(x=0, y=100, height=680, width= 2000)

            def text(self):
 
                    base_de_donné = [
                        # Partie 1 : Les questions sur les concepts littéraires (8 questions)
                        ["Qu'est-ce qu'un auteur ?", 
                        "La personne qui écrit un texte", 
                        "Le personnage principal d'une histoire", 
                        "La personne qui lit le texte", 
                        "Un critique littéraire"],

                        ["Quelle information doit donner la source d'un document ?", 
                        "L'auteur, le titre, la date et le lieu de publication", 
                        "Le résumé du document", 
                        "L'opinion de l'auteur", 
                        "Le nombre de pages"],

                        ["Qu'est-ce qu'un narrateur ?", 
                        "La voix qui raconte l'histoire", 
                        "Le personnage principal", 
                        "L'auteur du livre", 
                        "Le lecteur"],

                        ["Qu'est-ce qu'un protagoniste ?", 
                        "Le personnage principal d'une histoire", 
                        "L'antagoniste de l'histoire", 
                        "Le narrateur", 
                        "L'auteur"],

                        ["Qu'appelle-t-on un point de vue ?", 
                        "La perspective à partir de laquelle l'histoire est racontée", 
                        "La description des personnages", 
                        "Le résumé de l'histoire", 
                        "L'opinion de l'auteur"],

                        ["Savez-vous définir un point de vue omniscient ?", 
                        "Un narrateur qui sait tout sur les personnages et les événements", 
                        "Un narrateur qui est un personnage de l'histoire", 
                        "Un narrateur qui ne connaît que les pensées d'un personnage", 
                        "Un narrateur qui donne son opinion personnelle"],

                        ["Quel est le point de vue dans un récit à la première personne ?", 
                        "Le narrateur est un personnage de l'histoire", 
                        "Le narrateur sait tout sur les personnages", 
                        "Le narrateur n'est pas un personnage de l'histoire", 
                        "Le narrateur est un observateur extérieur"],

                        ["Qu'appelle-t-on une reprise nominale ?", 
                        "L'utilisation d'un nom pour désigner un personnage déjà mentionné", 
                        "Le changement de narrateur dans une histoire", 
                        "L'introduction d'un nouveau personnage", 
                        "La répétition d'une même idée"],
                    ]
                    self.question.QCM.création_qts(self,base_de_donné)
            
            def limage(self):
                    base_de_donné = [
                        # Partie 1 : Les documents iconographiques (2 questions)
                        ["Qu'est-ce qu'un document iconographique ?", 
                        "Un document visuel comme une image ou une photo", 
                        "Un document écrit comme un livre", 
                        "Un document sonore comme un enregistrement audio", 
                        "Un document numérique comme un fichier PDF"],
                        
                        ["Citez quatre types de documents iconographiques", 
                        "Photographies, affiches, peintures, cartes postales", 
                        "Livres, articles, essais, journaux", 
                        "Enregistrements audio, podcasts, chansons, discours", 
                        "Tableaux numériques, fichiers PDF, feuilles de calcul, présentations PowerPoint"]
                    ]

                    self.question.QCM.création_qts(self,base_de_donné)

            def Le_discours(self):
                    base_de_donné = [
                        # Partie 2 : Discours direct (3 questions)
                        ["Comment reconnaît-on le discours direct ?", 
                        "Par l'utilisation de guillemets et de verbes introducteurs", 
                        "Par l'utilisation de phrases au passé simple", 
                        "Par l'utilisation de descriptions détaillées", 
                        "Par l'utilisation de pronoms personnels"],
                        
                        ["Donnez cinq exemples de verbes introducteurs de parole", 
                        "dire, répondre, demander, s'exclamer, murmurer", 
                        "courir, sauter, manger, dormir, lire", 
                        "penser, croire, imaginer, réfléchir, supposer", 
                        "chanter, danser, jouer, écouter, écrire"],
                        
                        ["Qu'appelle-t-on les signes typographiques ?", 
                        "Les symboles utilisés pour structurer et ponctuer un texte", 
                        "Les lettres de l'alphabet", 
                        "Les chiffres et nombres", 
                        "Les couleurs utilisées dans un texte"]
                    ]
                    self.question.QCM.création_qts(self,base_de_donné)

            def Le_verbe(self):
                base_de_donné = [
                        # Partie 1 : Analyse d'un verbe (1 question)
                        ["Quelle information doit-on donner quand on analyse un verbe ?", 
                        "Le temps, le mode, la personne, la voix", 
                        "Le temps, le sujet, l'objet, la voix", 
                        "Le mode, le sujet, l'objet, la voix", 
                        "Le temps, le mode, l'objet, la voix"],
                        
                        # Partie 2 : Pronoms personnels sujets (1 question)
                        ["Citez les pronoms personnels sujets", 
                        "Je, tu, il/elle, nous, vous, ils/elles", 
                        "Me, te, le/la, nous, vous, les", 
                        "Moi, toi, lui/elle, nous, vous, eux/elles", 
                        "Le mien, le tien, le sien, le nôtre, le vôtre, le leur"],

                        # Partie 3 : Temps simples de l'indicatif (1 question)
                        ["Citez les temps simples de l'indicatif", 
                        "Présent, imparfait, passé simple, futur simple", 
                        "Présent, passé composé, plus-que-parfait, futur antérieur", 
                        "Imparfait, passé composé, passé simple, plus-que-parfait", 
                        "Présent, passé antérieur, futur simple, plus-que-parfait"],

                        # Partie 4 : Passé composé (1 question)
                        ["Qu'appelle-t-on le passé composé ?", 
                        "Un temps composé exprimant une action achevée", 
                        "Un temps simple exprimant une action en cours", 
                        "Un temps composé exprimant une action habituelle", 
                        "Un temps simple exprimant une action future"],

                        # Partie 5 : Construction des temps composés (1 question)
                        ["Comment se construit un temps composé par rapport à son temps simple correspondant ?", 
                        "Avec l'auxiliaire être ou avoir au temps simple et le participe passé du verbe", 
                        "Avec l'auxiliaire être ou avoir au présent et le participe présent du verbe", 
                        "Avec l'auxiliaire avoir et le participe passé du verbe", 
                        "Avec l'auxiliaire être au passé et le participe passé du verbe"],

                        # Partie 6 : Auxiliaires de conjugaison (1 question)
                        ["Citez les deux auxiliaires de conjugaison", 
                        "Être et avoir", 
                        "Être et faire", 
                        "Avoir et aller", 
                        "Être et aller"],

                        # Partie 7 : Voix d'un verbe (1 question)
                        ["Qu'appelle-t-on la voix d'un verbe ?", 
                        "La manière dont l'action est réalisée par le sujet ou subie par lui", 
                        "La tonalité avec laquelle le verbe est prononcé", 
                        "Le temps et le mode du verbe", 
                        "Le genre et le nombre du verbe"],

                        # Partie 8 : Voix passive (1 question)
                        ["Comment se caractérise la voix passive ?", 
                        "Le sujet subit l'action plutôt que de la faire", 
                        "Le sujet fait l'action plutôt que de la subir", 
                        "Le verbe est conjugué avec l'auxiliaire avoir", 
                        "Le verbe est au passé composé"],

                        # Partie 9 : Complément d'agent (1 question)
                        ["Qu'appelle-t-on un complément d'agent ?", 
                        "Le complément qui indique qui fait l'action dans une phrase à la voix passive", 
                        "Le complément qui indique où se passe l'action", 
                        "Le complément qui indique quand se passe l'action", 
                        "Le complément qui indique comment se passe l'action"],

                        # Partie 10 : Subjonctif présent (1 question)
                        ["Comment reconnaissez-vous un verbe au subjonctif présent ?", 
                        "Il est souvent précédé de 'que' et a une terminaison en -e, -es, -e, -ions, -iez, -ent", 
                        "Il a une terminaison en -ai, -as, -a, -ons, -ez, -ont", 
                        "Il a une terminaison en -ais, -ais, -ait, -ions, -iez, -aient", 
                        "Il est précédé de 'si' et a une terminaison en -rai, -ras, -ra, -rons, -rez, -ront"],

                        # Partie 11 : Mode impératif (1 question)
                        ["Quelles sont les caractéristiques du mode impératif ?", 
                        "Il exprime un ordre, un conseil ou une demande, et se conjugue sans pronom sujet", 
                        "Il exprime une action hypothétique ou future, et se conjugue avec des pronoms sujets", 
                        "Il exprime une action passée ou habituelle, et se conjugue sans pronom sujet", 
                        "Il exprime une action continue ou progressive, et se conjugue avec des pronoms sujets"]
                    ]       
                self.question.QCM.création_qts(self,base_de_donné)
            
            def Les_valeur_des_temps(self):
                base_de_donné = [
                    # Question 1 : Qu'appelle-t-on la valeur d'emploi d'un temps ?
                    ["Qu'appelle-t-on la valeur d'emploi d'un temps ?", 
                    "La fonction que le temps verbal remplit dans la phrase", 
                    "La conjugaison correcte d'un verbe dans un temps donné", 
                    "Le moment précis où une action se produit", 
                    "La durée pendant laquelle une action se déroule"],
                    
                    # Question 2 : Quelle est la valeur d'emploi du plus-que-parfait ?
                    ["Quelle est la valeur d'emploi du plus-que-parfait ?", 
                    "Exprimer une action antérieure à une autre action déjà passée", 
                    "Indiquer une action qui se produit régulièrement dans le passé", 
                    "Marquer une action passée et définitive", 
                    "Relater une action passée sans notion de continuité"],
                    
                    # Question 3 : Citez au moins trois valeurs d'emploi du présent de l'indicatif
                    ["Citez au moins deux valeurs d'emploi du présent de l'indicatif ?", 
                    "Indiquer une action habituelle ou répétée", 
                    "Exprimer une vérité générale ou une loi scientifique", 
                    "Situer une action dans le présent de l'énonciation", 
                    "Raconter une action qui se déroule au moment de l'énonciation"],
                    
                    # Question 4 : Quelles peuvent être les valeurs d'emplois de l'imparfait de l'indicatif ?
                    ["Quelles peuvent être les valeurs d'emplois de l'imparfait de l'indicatif ?", 
                    "Décrire une action ou une situation habituelle dans le passé", 
                    "Situer une action dans un passé révolu par rapport à une autre action passée", 
                    "Marquer une action passée et complètement achevée", 
                    "Exprimer une action passée proche de l'énonciation"],
                    
                    # Question 5 : Quelles peuvent être les valeurs d'emplois du passé simple ?
                    ["Quelles peuvent être les valeurs d'emplois du passé simple ?", 
                    "Narrer une action ponctuelle et brève dans le passé", 
                    "Relater une action passée avec des effets dans le présent", 
                    "Indiquer une action passée répétée ou habituelle", 
                    "Décrire une action passée en cours de réalisation"],
                ]

                self.question.QCM.création_qts(self,base_de_donné)

            def laphrase(self):
                base_de_donné = [
                            # Question 1 : Comment définit-on une phrase ?
                            ["Comment définit-on une phrase ?", 
                            "Une phrase est un ensemble de mots qui a un sens complet.", 
                            "Une phrase est une suite de mots sans ponctuation.", 
                            "Une phrase est une suite de mots qui commence par une majuscule.", 
                            "Une phrase est un groupe de mots séparés par des virgules."],
                            
                            # Question 2 : Quels sont les quatre types de phrases ?
                            ["Quels sont les quatre types de phrases ?", 
                            "Déclarative, interrogative, exclamative, impérative", 
                            "Déclarative, exclamative, conditionnelle, impérative", 
                            "Interrogative, négative, conditionnelle, impérative", 
                            "Déclarative, interrogative, conditionnelle, exclamative"],
                            
                            # Question 3 : Rappelez les 3 formes de phrases ?
                            ["Rappelez les 3 formes de phrases ?", 
                            "Affirmative, négative, interrogative", 
                            "Active, passive, pronominale", 
                            "Simple, complexe, composée", 
                            "Affirmative, négative, exclamative"],
                            
                            # Question 4 : À quoi reconnaît-on une proposition ?
                            ["À quoi reconnaît-on une proposition ?", 
                            "Une proposition est un groupe de mots organisé autour d'un verbe conjugué.", 
                            "Une proposition est un groupe de mots qui contient une virgule.", 
                            "Une proposition est une phrase entière.", 
                            "Une proposition est un groupe de mots sans verbe conjugué."],
                            
                            # Question 5 : Quels sont les liens possibles entre deux propositions ?
                            ["Quels sont les liens possibles entre deux propositions ?", 
                            "Coordination, subordination, juxtaposition", 
                            "Coordination, addition, subordination", 
                            "Juxtaposition, apposition, subordination", 
                            "Coordination, juxtaposition, opposition"],
                            
                            # Question 6 : Comment se nomme une proposition subordonnée qui complète un verbe ?
                            ["Comment se nomme une proposition subordonnée qui complète un verbe ?", 
                            "Proposition subordonnée complétive", 
                            "Proposition subordonnée relative", 
                            "Proposition subordonnée conjonctive", 
                            "Proposition subordonnée circonstancielle"]
                        ]
                self.question.QCM.création_qts(self,base_de_donné)

            def class_gramm(self):
                base_de_donné = [
                    # Partie 1 : Questions sur les classes grammaticales
                    ["Dans quel ouvrage trouve-t-on la classe grammaticale d'un mot ?", 
                    "Dans un dictionnaire", 
                    "Dans une grammaire", 
                    "Dans un manuel de conjugaison", 
                    "Dans un thesaurus"],
                    
                    ["Citez 5 classes grammaticales.", 
                    "Nom, verbe, adjectif, adverbe, pronom", 
                    "Nom, verbe, adjectif, pronom, surnom", 
                    "Nom, verbe, adverbe, surnom, interjection", 
                    "Nom, verbe, mot, déterminant, préposition"],
                    
                    ["Comment définit-on simplement ce qu'est une classe grammaticale ?", 
                    "Une classe grammaticale est un groupe de mots ayant des caractéristiques grammaticales similaires.", 
                    "Une classe grammaticale est un groupe de mots ayant le même sens.", 
                    "Une classe grammaticale est un groupe de mots utilisés dans les mêmes contextes.", 
                    "Une classe grammaticale est un groupe de mots ayant la même origine étymologique."],
                    
                    ["Quelles sont les classes grammaticales variables ?", 
                    "Nom, verbe, adjectif, déterminant, pronom", 
                    "Nom, verbe, adverbe, déterminant, pronom", 
                    "Nom, verbe, adjectif, adverbe, pronom", 
                    "Nom, verbe, adjectif, déterminant, conjonction"],
                    
                    ["Quelles sont les classes grammaticales invariables ?", 
                    "Adverbe, préposition, conjonction, interjection", 
                    "Adjectif, préposition, conjonction, interjection", 
                    "Adverbe, préposition, conjonction, pronom", 
                    "Adverbe, préposition, déterminant, interjection"]
                ]
                self.question.QCM.création_qts(self,base_de_donné)

            def fonction_gramm(self):
                base_de_donné = [
                    ["Quelle fonction grammaticale commande l'accord du verbe ?", 
                    "Le sujet", 
                    "L'objet", 
                    "Le complément", 
                    "L'attribut"],
                    
                    ["Un verbe à l'infinitif peut-il être sujet d'un verbe conjugué ?", 
                    "Oui", 
                    "Non", 
                    "Seulement avec un auxiliaire", 
                    "Seulement à la voix passive"],
                    
                    ["Qu'est-ce qu'un attribut du sujet ?", 
                    "Un mot ou groupe de mots qui donne une information sur le sujet", 
                    "Un mot ou groupe de mots qui complète le verbe", 
                    "Un mot ou groupe de mots qui précise le complément d'objet", 
                    "Un mot ou groupe de mots qui est toujours précédé d'une préposition"],
                    
                    ["Comment reconnaît-on une épithète ?", 
                    "C'est un adjectif qualificatif directement lié au nom qu'il décrit", 
                    "C'est un complément qui suit le verbe", 
                    "C'est un groupe nominal introduit par une préposition", 
                    "C'est un pronom qui remplace le nom"],
                    
                    ["Comment distinguer l'attribut du sujet du COD ?", 
                    "L'attribut du sujet est lié au sujet par un verbe d'état, le COD par un verbe d'action", 
                    "L'attribut du sujet est introduit par une préposition, le COD non", 
                    "L'attribut du sujet décrit le verbe, le COD décrit le sujet", 
                    "L'attribut du sujet est toujours au pluriel, le COD peut être au singulier"],
                    
                    ["Qu'appelle-t-on un complément circonstanciel ?", 
                    "Un complément qui précise les circonstances de l'action", 
                    "Un complément qui désigne la personne qui fait l'action", 
                    "Un complément qui remplace un nom", 
                    "Un complément qui est introduit par un adjectif"]
                ]
                self.question.QCM.création_qts(self,base_de_donné)
            
            def nom_et_gr_nom(self):
                base_de_donné = [
                    ["Qu'appelle-t-on un groupe minimal ?", 
                    "Un groupe de mots qui peut se réduire à un seul mot", 
                    "Un groupe de mots qui inclut au moins deux prépositions", 
                    "Un groupe de mots qui ne peut jamais se réduire", 
                    "Un groupe de mots qui contient au moins un adjectif"],
                    
                    ["Quelles sont les trois expansions minimales possibles pour un GN ?", 
                    "Adjectif, complément du nom, proposition subordonnée relative", 
                    "Adjectif, verbe, préposition", 
                    "Adjectif, conjonction, adverbe", 
                    "Adjectif, pronom, interjection"],
                    
                    ["Que complète une proposition subordonnée relative ?", 
                    "Un nom ou un pronom", 
                    "Un verbe", 
                    "Un adjectif", 
                    "Un adverbe"],
                    
                    ["Par quoi est introduite une proposition subordonnée relative ?", 
                    "Un pronom relatif", 
                    "Une conjonction de coordination", 
                    "Un adverbe", 
                    "Un verbe à l'infinitif"]
                ]
                self.question.QCM.création_qts(self,base_de_donné)
            
            def autour_du_mot(self):
                base_de_donné = [
                    ["Qu'est-ce qu'un synonyme ?", 
                    "Un mot ayant le même sens ou un sens proche d'un autre mot", 
                    "Un mot ayant un sens opposé à celui d'un autre mot", 
                    "Un mot qui appartient à la même famille qu'un autre mot", 
                    "Un mot dérivé d'un autre mot"],
                    
                    ["Qu'est-ce qu'un antonyme ?", 
                    "Un mot ayant un sens opposé à celui d'un autre mot", 
                    "Un mot ayant le même sens qu'un autre mot", 
                    "Un mot dérivé d'un autre mot", 
                    "Un mot appartenant au même champ lexical qu'un autre mot"],
                    
                    ["Définissez ce qu'est un champ lexical ?", 
                    "Ensemble de mots qui se rapportent à un même thème ou à une même idée", 
                    "Ensemble de mots ayant la même racine", 
                    "Ensemble de mots ayant des sens opposés", 
                    "Ensemble de mots ayant des sens identiques"],
                    
                    ["À quoi reconnaît-on une famille de mots ?", 
                    "À la présence d'une racine commune", 
                    "À la présence de préfixes identiques", 
                    "À la même longueur de mot", 
                    "À des sens identiques"],
                    
                    ["Quels éléments peuvent entrer dans la construction (la formation) d'un mot ?", 
                    "Préfixes, suffixes et racines", 
                    "Adverbes et adjectifs", 
                    "Conjonctions et prépositions", 
                    "Pronoms et interjections"]
                ]
                self.question.QCM.création_qts(self,base_de_donné)

            def les_figure_de_style(self):
                base_de_donné = [
                    ["Qu'appelle-t-on une figure de style ?", 
                    "Une expression littéraire qui crée un effet particulier en jouant sur la langue", 
                    "Une règle de grammaire qui doit être suivie dans les phrases", 
                    "Un type de texte littéraire spécifique", 
                    "Un schéma narratif utilisé dans les récits"],
                    
                    ["Donnez un exemple de comparaison.", 
                    "Il est fort comme un lion", 
                    "Il est un lion", 
                    "Il court vite", 
                    "Il est très fort"],
                    
                    ["Combien d'éléments composent une comparaison ?", 
                    "Trois éléments : le comparé, le comparant et l'outil de comparaison", 
                    "Deux éléments : le comparé et le comparant", 
                    "Quatre éléments : le comparé, le comparant, l'outil de comparaison et l'intensificateur", 
                    "Un seul élément : le comparant"],
                    
                    ["Quelle est la différence entre une comparaison et une métaphore ?", 
                    "La comparaison utilise un outil de comparaison tandis que la métaphore n'en utilise pas", 
                    "La métaphore utilise un outil de comparaison tandis que la comparaison n'en utilise pas", 
                    "La comparaison est plus imagée que la métaphore", 
                    "Il n'y a pas de différence, ce sont des synonymes"]
                ]
                self.question.QCM.création_qts(self,base_de_donné)
