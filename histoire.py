from tkinter import *
import random


class Code:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.titre_mth = Label(self.fenetre, text = "Histoire", font = ("French Script MT",80))
        self.titre_mth.place(x=420,y=0)
        self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
        self.parti_qts.place(x=0,y=125)

        self.fenetre.geometry("2000x780")
        self.score = 0
        self.score_sur = 0
        self.choisir_question_aléatoirement()


    def choisir_question_aléatoirement(self):
        self.parti_qts.destroy()
        self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
        self.parti_qts.place(x=0,y=125)
        qts = random.randint(0,6)
        match qts:
            case 0:
                self.question.histoire.front_pop.QCM(self)
            case 1:
                self.question.EMC.QCM(self)
            case 2:
                self.question.histoire.post_guerre_foide.QCM(self)
            case 3:
                self.question.histoire.guerre_froide.QCM(self)
            case 4:
                self.question.histoire.hitler.QCM(self)
            case 5:
                self.question.histoire.d2eme_guerre.QCM(self)
            case 6:
                self.question.histoire.d1er_guerre.QCM(self)

    class question:
        def valider(self, réponse, réponse_donner, taille = 80):
           text = réponse_donner

           if  text in réponse:
               self.question.bonne_réponse(self, réponse, taille)
           else:
                self.question.mauvaise_réponse(self, réponse, taille)
                
        def bonne_réponse(self, réponse, taille):
            self.parti_qts.destroy()
            self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
            self.parti_qts.place(x=0,y=100)
            vrai_réponse = Label(self.parti_qts, text = f'Bien joué,\nla bonne réponse\nétait effectivement :\n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)
            self.score+=1
            self.score_sur+=1

        def mauvaise_réponse(self, réponse, taille):
            self.parti_qts.destroy()
            self.parti_qts = Frame(self.fenetre, height= 780, width= 2000)
            self.parti_qts.place(x=0,y=100)
            vrai_réponse = Label(self.parti_qts, text = f'Dommage,\n la bonne réponse\nétait : \n{réponse[0]}', font=("", taille))
            vrai_réponse.pack(expand=YES)
            bouton_suivant = Button(self.parti_qts, text = "Suivant", font = ("", 20),command=lambda:self.choisir_question_aléatoirement())
            bouton_suivant.place(x = 00, y = 00)  
            self.score_sur+=1

        class histoire:
            class front_pop:
                def QCM(self):
                    base_de_donné = [["Quelles sont les causes de l'arrivée au pouvoir du front populaire en France ?",
                                            "Crise économique, social, politique", 
                                            "Crise économique, démographique, industriel",
                                            "Crise politique, social, démographique",
                                            "Crise démographique, industriel, politique"],
                                    ["Qu'est-ce qu'une crise économique ?",
                                            "Baisse de la production",
                                            "Augmentation du chômage",
                                            "Augmentation de la misère",
                                            "Une cohabitation"],
                                    ["Qu'est-ce qu'une crise social ?",
                                            "Augmentation du chômage",
                                            "Baisse de la production",
                                            "Une cohabitation",
                                            "Augmentation de la misère"],
                                    ["Quelle est la cause de l'augmentation du chômage ?",
                                            "Augmentation de la misère",
                                            "Baisse de la production",
                                            "Une cohabitation",
                                            "Augmentation de la production"],
                                    ["Quelle pays est à l'origine de la crise économique de 1929",
                                            "Les états-unis",
                                            "L'Angleterre",
                                            "L'Allemagne",
                                            "La Russie"],
                                    ["Comment se manifeste la crise politique en France ?",
                                            "De nombreux gouvernements se succèdent",
                                            "Le gouvernement est en cohabitation",
                                            "Le peuple déteste le gouvernement",
                                            "De nombreuses tentatives tentatives d'assassinats des dirigents"],
                                    ["Quelle est la réaction de la gauche suite à le manifestation du 6 février 1934 ?",
                                            "Les partis de gauche forment le front populaire ",
                                            "Les partis de gauche ne font rien",
                                            "Les partis de gauche abendonnent",
                                            "Les partis de gauche se dissouent",],
                                    ["Quelle sont les trois partis formant le front populaire ?",
                                            "communiste, socialiste, radicaux",
                                            "nationaliste, communiste, soviétique",
                                            "fasciste, nationaliste, radicaux",
                                            "nationaliste, fasciste, soviétique"],
                                    ["Quand et comment le front populaire arrive-t-il au pouvoir ?",
                                            "Par les élections législatives en mai 1936",
                                            "Par un coup d'état en mai 1936",
                                            "Par un coup d'état en mai 1940",
                                            "Suite à la chute de l'allemagne nazi, par les élections législatives"],
                                    ["Que sont les éléctions legislatives?",
                                            "L'élection des députés",
                                            "L'élection du président",
                                            "Le choix d'une loi",
                                            "L'élection des maires"],
                                    ["Qu'est-ce qu'un président du conseil ?",
                                            "Le chef du gouvernement",
                                            "Le premier ministre",
                                            "Celui qui dirige l'assemblé national",
                                            "Le maire d'une ville"],
                                    ["Que sont les accords de Matignon (du front populaire) ?",
                                            "augmentation du salaire, convention collectives, liberté syndicale dans les \nentreprises, délégué personnel",
                                            "congé payés, augmentation du salaire, convention colléctives,\naugmentation de la production",
                                            "création de syndicat, congé payé, création du smic,\naugmentation de la production",
                                            "communiste, radicaux, socialiste"],
                                    ["Quelle sont les deux autres lois social autre que les accord de Matignon de 1936 ?",
                                            "Semaine de 40 heure au lieu de 48 heure --> 2 jours de repos\ncongé payé",
                                            "Semaine de 48 heure au lieu de 40 --> retirement des 2 jours de repos\n retirement des congés payés",
                                            "création de la 5ème république et de l'ssemblé national",
                                            "Aucune"],
                                    ["Qui sont les bénéficiaire de l'ensemble des mesures social prises par le front populaire ?",
                                            "Les salariés",
                                            "Les chefs d'entreprise",
                                            "Les hauts gradés",
                                            "Les nobles"],
                                    ["Quelles mesures économiques prends le front populaire ?",
                                            "nationalisation des compagnies de chemin de fer (SNCF)\n et des industries d'armements",
                                            "création de centrale nucléaire et d'usine a charbon",
                                            "création du PIB et de nombreuses banques",
                                            "congés payés et semaine de 40 heures au lieu de 48 heures"],
                                    ["Qu'est-ce que la nationalisation ?",
                                            "Une entreprise privé qui devient publique et donc appartient à l'état",
                                            "Gagné la nationalité française",
                                            "Travailler en France",
                                            "Mettre en valeur son pays"]]

                    qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                    self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                    self.énoncer.place(x=20,y=20)
                    réponse = [qts[1]]
                    self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                    self.score_affichage.place(x= 0, y=0)
                    aléa = random.randint(1,4)

                    cadre1 = Frame(self.parti_qts, background='black')
                    cadre1.place(x=60, y=100, width=80, height=80)
                    bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse(self, réponse, 50))
                    bouton1.place(x=5, y=5, height=70, width=70)
                    text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                    text_1.place(x= 200, y=aléa*100)

                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=60, y=200, width=80, height=80)
                    bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse(self, réponse , 50))
                    bouton2.place(x=5, y=5, height=70, width=70)
                    text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                    text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
                
                    cadre3 = Frame(self.parti_qts, background='black')
                    cadre3.place(x=60, y=300, width=80, height=80)
                    bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton3.place(x=5, y=5, height=70, width=70)
                    text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                    text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
                
                    cadre4 = Frame(self.parti_qts, background='black')
                    cadre4.place(x=60, y=400, width=80, height=80)
                    bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton4.place(x=5, y=5, height=70, width=70)
                    text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                    text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)
            class guerre_froide:
                def QCM(self):
                    base_de_donné = [
                                ["Quelle conférence marque le début de la guerre froide ?", 
                                "Conférence de Yalta", 
                                "Conférence de Vienne", 
                                "Conférence de Berlin", 
                                "Conférence de Paris"],

                                ["Quel événement symbolise le début de la guerre froide en Europe ?", 
                                "Le blocus de Berlin", 
                                "La construction du mur de Berlin", 
                                "La crise des missiles de Cuba", 
                                "La chute du mur de Berlin"],

                                ["Quel est le plan économique américain pour aider l'Europe après la Seconde Guerre mondiale ?", 
                                "Plan Marshall", 
                                "Plan Molotov", 
                                "Plan Schuman", 
                                "Plan Truman"],

                                ["Quel était le principal allié des États-Unis pendant la guerre froide ?", 
                                "Le Royaume-Uni", 
                                "La Chine", 
                                "L'Allemagne de l'Ouest", 
                                "Le Japon"],

                                ["Quel était le principal allié de l'URSS pendant la guerre froide ?", 
                                "La Chine", 
                                "Le Cuba", 
                                "La Corée du Nord", 
                                "La RDA (République Démocratique Allemande)"],

                                ["Quel événement a mis fin à la guerre froide ?", 
                                "La chute du mur de Berlin", 
                                "La crise des missiles de Cuba", 
                                "La guerre du Vietnam", 
                                "La guerre de Corée"],

                                ["Quelle doctrine a été formulée par le président américain Truman pour contrer le communisme ?", 
                                "Doctrine Truman", 
                                "Doctrine Eisenhower", 
                                "Doctrine Kennedy", 
                                "Doctrine Reagan"],

                                ["Quelle organisation militaire a été créée par les pays occidentaux en 1949 ?", 
                                "OTAN (Organisation du Traité de l'Atlantique Nord)", 
                                "Pacte de Varsovie", 
                                "ONU (Organisation des Nations Unies)", 
                                "SEATO (Organisation du Traité de l'Asie du Sud-Est)"],

                                ["Quel était le nom du premier satellite artificiel lancé par l'URSS en 1957 ?", 
                                "Spoutnik", 
                                "Vostok", 
                                "Soyouz", 
                                "Luna"],

                                ["Quelle crise a eu lieu en 1962 entre les États-Unis et l'URSS ?", 
                                "Crise des missiles de Cuba", 
                                "Blocus de Berlin", 
                                "Guerre de Corée", 
                                "Guerre du Vietnam"],

                                ["Quel traité a été signé en 1987 pour réduire les armements nucléaires ?", 
                                "Traité INF (Intermediate-Range Nuclear Forces Treaty)", 
                                "Traité de Versailles", 
                                "Traité de Tlatelolco", 
                                "Traité de Genève"],

                                ["Quelle politique de réforme a été introduite par Mikhaïl Gorbatchev en URSS ?", 
                                "Perestroïka", 
                                "Glasnost", 
                                "NEP (Nouvelle Politique Économique)", 
                                "Collectivisation"],

                                ["Quel événement de 1950-1953 a été un conflit majeur de la guerre froide ?", 
                                "Guerre de Corée", 
                                "Guerre du Vietnam", 
                                "Crise de Suez", 
                                "Guerre d'Afghanistan"],

                                ["Quel pays a été envahi par l'URSS en 1979, marquant un tournant dans la guerre froide ?", 
                                "Afghanistan", 
                                "Pologne", 
                                "Tchécoslovaquie", 
                                "Hongrie"]
                                ]
                    qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                    self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                    self.énoncer.place(x=20,y=20)
                    réponse = [qts[1]]
                    self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                    self.score_affichage.place(x= 0, y=0)
                    aléa = random.randint(1,4)

                    cadre1 = Frame(self.parti_qts, background='black')
                    cadre1.place(x=60, y=100, width=80, height=80)
                    bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse(self, réponse, 50))
                    bouton1.place(x=5, y=5, height=70, width=70)
                    text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                    text_1.place(x= 200, y=aléa*100)

                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=60, y=200, width=80, height=80)
                    bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse(self, réponse , 50))
                    bouton2.place(x=5, y=5, height=70, width=70)
                    text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                    text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
                
                    cadre3 = Frame(self.parti_qts, background='black')
                    cadre3.place(x=60, y=300, width=80, height=80)
                    bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton3.place(x=5, y=5, height=70, width=70)
                    text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                    text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
                
                    cadre4 = Frame(self.parti_qts, background='black')
                    cadre4.place(x=60, y=400, width=80, height=80)
                    bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton4.place(x=5, y=5, height=70, width=70)
                    text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                    text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)

            class post_guerre_foide:
                def QCM(self):
                    base_de_donné = [
                                # Partie 1 : Conséquences de l'effondrement du bloc soviétique en 1989-1991 en Europe (4 questions)
                                ["Quels pays se sont réunifiés en 1990 après l'effondrement du bloc soviétique ?", 
                                "L'Allemagne", 
                                "La Tchécoslovaquie", 
                                "La Yougoslavie", 
                                "La Pologne"],
                                
                                ["Quel terme décrit la transition des pays de l'Europe de l'Est vers la démocratie et l'économie de marché ?", 
                                "Transition post-communiste", 
                                "Démocratisation", 
                                "Libéralisation", 
                                "Révolution industrielle"],

                                ["Quel événement marque la fin symbolique de la guerre froide en Europe ?", 
                                "La chute du mur de Berlin", 
                                "La chute de Stalingrad", 
                                "La création de l'Union européenne", 
                                "L'invasion de la Pologne"],

                                ["Quel était l'objectif de la politique de perestroïka en URSS ?", 
                                "Réformer l'économie soviétique", 
                                "Étendre le communisme en Europe", 
                                "Démanteler l'armée soviétique", 
                                "Renforcer l'alliance avec la Chine"],

                                # Partie 2 : La superpuissance étatsunienne dans un monde unipolaire : un "nouvel ordre mondial" (4 questions)
                                ["Quel président américain a proclamé un 'nouvel ordre mondial' après la guerre froide ?", 
                                "George H.W. Bush", 
                                "Bill Clinton", 
                                "Ronald Reagan", 
                                "George W. Bush"],

                                ["Quel était l'objectif principal de la doctrine du 'nouvel ordre mondial' ?", 
                                "Promouvoir la démocratie et la paix mondiale", 
                                "Augmenter les dépenses militaires", 
                                "Coloniser de nouveaux territoires", 
                                "Restaurer l'Empire britannique"],

                                ["Quel conflit a illustré la volonté des États-Unis de maintenir l'ordre mondial après la guerre froide ?", 
                                "La guerre du Golfe", 
                                "La guerre de Corée", 
                                "La guerre du Vietnam", 
                                "La guerre des Malouines"],

                                ["Quelle organisation internationale a été renforcée pour maintenir la paix après la guerre froide ?", 
                                "L'ONU", 
                                "OTAN", 
                                "UE", 
                                "OPEP"],

                                # Partie 3 : La superpuissance étatsunienne, une superpuissance contestée (3 questions)
                                ["Quel pays a contesté la superpuissance américaine en Asie dans les années 2000 ?", 
                                "La Chine", 
                                "L'Inde", 
                                "Le Japon", 
                                "La Corée du Sud"],

                                ["Quel événement en 2001 a mis en cause la sécurité des États-Unis ?", 
                                "Les attentats du 11 septembre", 
                                "La guerre d'Irak", 
                                "La guerre de Corée", 
                                "L'invasion du Panama"],

                                ["Quel terme désigne la politique américaine visant à promouvoir la démocratie par la force ?", 
                                "Interventionnisme", 
                                "Isolationnisme", 
                                "Neutralité", 
                                "Colonialisme"],

                                # Partie 4 : La guerre en Afghanistan (3 questions)
                                ["Quel groupe a pris le pouvoir en Afghanistan avant l'intervention américaine en 2001 ?", 
                                "Les talibans", 
                                "Al-Qaïda", 
                                "L'Armée rouge", 
                                "Le Viet Cong"],

                                ["Quel était l'objectif principal de l'intervention américaine en Afghanistan ?", 
                                "Éliminer les bases terroristes d'Al-Qaïda", 
                                "Établir une colonie", 
                                "S'emparer des ressources naturelles", 
                                "Renverser le gouvernement communiste"],

                                ["Quel pays a été accusé de soutenir les talibans et Al-Qaïda ?", 
                                "Le Pakistan", 
                                "L'Irak", 
                                "La Russie", 
                                "La Chine"],

                                # Partie 5 : La 2e guerre du Golfe contre l'Irak (3 questions)
                                ["Quel prétexte a été utilisé pour justifier l'invasion de l'Irak en 2003 ?", 
                                "La présence d'armes de destruction massive", 
                                "Le soutien à Al-Qaïda", 
                                "La protection des droits de l'homme", 
                                "L'expansion du communisme"],

                                ["Quel était le nom de l'opération militaire menée par les États-Unis en Irak en 2003 ?", 
                                "Opération Iraqi Freedom", 
                                "Opération Desert Storm", 
                                "Opération Enduring Freedom", 
                                "Opération Neptune Spear"],

                                ["Qui était le président de l'Irak au moment de l'invasion américaine en 2003 ?", 
                                "Saddam Hussein", 
                                "Hosni Mubarak", 
                                "Muammar Kadhafi", 
                                "Bashar al-Assad"],

                                # Partie 6 : La persistance des conflits au Moyen-Orient (3 questions)
                                ["Quel conflit a opposé Israël et le Hezbollah en 2006 ?", 
                                "La guerre du Liban", 
                                "La guerre du Golfe", 
                                "La guerre de Syrie", 
                                "La guerre de l'Irak"],

                                ["Quel pays a été le théâtre d'une guerre civile débutée en 2011 ?", 
                                "La Syrie", 
                                "Le Liban", 
                                "L'Égypte", 
                                "La Jordanie"],

                                ["Quel groupe terroriste a proclamé un califat en 2014 ?", 
                                "L'État islamique (Daech)", 
                                "Al-Qaïda", 
                                "Les talibans", 
                                "Boko Haram"],

                                # Partie 7 : Un monde actuel instable et dangereux (3 questions)
                                ["Quel pays a annexé la Crimée en 2014, provoquant des tensions internationales ?", 
                                "La Russie", 
                                "La Chine", 
                                "Les États-Unis", 
                                "L'Iran"],

                                ["Quel phénomène climatique a été exacerbé par les activités humaines, causant des conflits pour les ressources ?", 
                                "Le changement climatique", 
                                "La déforestation", 
                                "La désertification", 
                                "La montée des eaux"],

                                ["Quel pays a connu une tentative de coup d'État en 2016, renforçant l'instabilité régionale ?", 
                                "La Turquie", 
                                "La Grèce", 
                                "Le Brésil", 
                                "L'Italie"],

                                # Partie 8 : L'émergence de nouvelles puissances vers un monde multipolaire (5 questions)
                                ["Quel pays est devenu la deuxième économie mondiale, contestant la suprématie américaine ?", 
                                "La Chine", 
                                "L'Inde", 
                                "Le Japon", 
                                "L'Allemagne"],

                                ["Quelle organisation a été fondée pour contrer l'influence économique occidentale ?", 
                                "BRICS", 
                                "OTAN", 
                                "UE", 
                                "ALENA"],

                                ["Quel pays a investi massivement dans les infrastructures en Afrique et en Asie ?", 
                                "La Chine", 
                                "Les États-Unis", 
                                "La Russie", 
                                "L'Inde"],

                                ["Quel pays est devenu un acteur majeur dans le secteur technologique et numérique ?", 
                                "L'Inde", 
                                "La Russie", 
                                "Le Brésil", 
                                "L'Australie"],

                                ["Quelle alliance militaire renforce son rôle en Asie-Pacifique pour contrer la montée en puissance de la Chine ?", 
                                "AUKUS", 
                                "OTAN", 
                                "OPEP", 
                                "CSTO"],
                                ]



                    qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                    self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                    self.énoncer.place(x=20,y=20)
                    réponse = [qts[1]]
                    self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                    self.score_affichage.place(x= 0, y=0)
                    aléa = random.randint(1,4)

                    cadre1 = Frame(self.parti_qts, background='black')
                    cadre1.place(x=60, y=100, width=80, height=80)
                    bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse(self, réponse, 50))
                    bouton1.place(x=5, y=5, height=70, width=70)
                    text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                    text_1.place(x= 200, y=aléa*100)

                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=60, y=200, width=80, height=80)
                    bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse(self, réponse , 50))
                    bouton2.place(x=5, y=5, height=70, width=70)
                    text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                    text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
                
                    cadre3 = Frame(self.parti_qts, background='black')
                    cadre3.place(x=60, y=300, width=80, height=80)
                    bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton3.place(x=5, y=5, height=70, width=70)
                    text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                    text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
                
                    cadre4 = Frame(self.parti_qts, background='black')
                    cadre4.place(x=60, y=400, width=80, height=80)
                    bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton4.place(x=5, y=5, height=70, width=70)
                    text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                    text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)
            class hitler:
                def QCM(self):
                    base_de_donné = [
                                # Partie 1 : Les causes de l'arrivée au pouvoir des nazis : la crise des années 1930 (3 questions)
                                ["Quelles sont les principales causes de l'arrivée au pouvoir des nazis en Allemagne ?", 
                                "Crise économique, sociale et politique", 
                                "Crise économique, démographique et industrielle", 
                                "Crise politique, sociale et démographique", 
                                "Crise démographique, industrielle et politique"],
                                
                                ["Quel événement a exacerbé la crise économique en Allemagne dans les années 1930 ?", 
                                "La Grande Dépression", 
                                "Le traité de Versailles", 
                                "La Révolution russe", 
                                "La Première Guerre mondiale"],
                                
                                ["Quel était le taux de chômage en Allemagne en 1932 ?", 
                                "Près de 30%", 
                                "Près de 10%", 
                                "Près de 50%", 
                                "Près de 5%"],

                                # Partie 2 : L'arrivée au pouvoir des nazis et d'Hitler (5 questions)
                                ["De quel parti Adolf Hitler est-il le chef ?", 
                                "NSDAP (Parti national-socialiste des travailleurs allemands)", 
                                "KPD (Parti communiste d'Allemagne)", 
                                "SPD (Parti social-démocrate d'Allemagne)", 
                                "Zentrum (Parti du centre)"],
                                
                                ["En quelle année Hitler est-il devenu chancelier d'Allemagne ?", 
                                "1933", 
                                "1923", 
                                "1945", 
                                "1939"],
                                
                                ["Quel événement a permis à Hitler de prendre les pleins pouvoirs en 1933 ?", 
                                "L'incendie du Reichstag", 
                                "La nuit des longs couteaux", 
                                "Le pacte germano-soviétique", 
                                "La Kristallnacht"],
                                
                                ["Quel était le principal rival politique de Hitler avant sa prise de pouvoir ?", 
                                "Le KPD (Parti communiste d'Allemagne)", 
                                "Le SPD (Parti social-démocrate d'Allemagne)", 
                                "Le Zentrum (Parti du centre)", 
                                "Le DNVP (Parti national du peuple allemand)"],
                                
                                ["Quel accord signé en 1938 symbolise l'apaisement des tensions avec Hitler par les démocraties occidentales ?", 
                                "Les accords de Munich", 
                                "Le pacte de non-agression", 
                                "Le traité de Versailles", 
                                "Le pacte de Locarno"],

                                # Partie 3 : L'Allemagne nazie, une expérience totalitaire : dictature et régime totalitaire (27 questions)
                                ["Quel titre Hitler s'est-il attribué en 1934 ?", 
                                "Führer", 
                                "Kaiser", 
                                "Reichspräsident", 
                                "Reichskanzler"],
                                
                                ["Quel était l'objectif principal de la propagande nazie ?", 
                                "Contrôler l'opinion publique et renforcer le culte de la personnalité d'Hitler", 
                                "Promouvoir les arts et la culture", 
                                "Encourager le tourisme", 
                                "Favoriser l'industrialisation"],
                                
                                ["Quel ministre était en charge de la propagande nazie ?", 
                                "Joseph Goebbels", 
                                "Heinrich Himmler", 
                                "Hermann Göring", 
                                "Albert Speer"],
                                
                                ["Quel était le rôle de la Gestapo ?", 
                                "Police secrète d'État chargée de traquer les opposants au régime", 
                                "Organisation militaire d'élite", 
                                "Service de renseignement étranger", 
                                "Branche de la jeunesse hitlérienne"],
                                
                                ["Quel groupe était ciblé par les lois de Nuremberg de 1935 ?", 
                                "Les Juifs", 
                                "Les communistes", 
                                "Les Tziganes", 
                                "Les homosexuels"],
                                
                                ["Quel événement marque le début de la persécution violente des Juifs en 1938 ?", 
                                "La Kristallnacht (Nuit de cristal)", 
                                "La Nuit des longs couteaux", 
                                "L'incendie du Reichstag", 
                                "L'Anschluss"],
                                
                                ["Quel était le nom de l'organisation paramilitaire nazie chargée de la protection de Hitler et des hauts dirigeants nazis ?", 
                                "SS (Schutzstaffel)", 
                                "SA (Sturmabteilung)", 
                                "Wehrmacht", 
                                "Luftwaffe"],
                                
                                ["Quel était le rôle des camps de concentration nazis ?", 
                                "Emprisonner et exterminer les opposants politiques et les groupes persécutés", 
                                "Former les jeunes soldats", 
                                "Produire des armes", 
                                "Encourager le tourisme"],
                                
                                ["Quel était le nom du plan nazi visant à exterminer les Juifs d'Europe ?", 
                                "La Solution finale", 
                                "L'Anschluss", 
                                "Le Lebensraum", 
                                "Le plan Barbarossa"],
                                
                                ["Quel était le rôle de Heinrich Himmler dans le régime nazi ?", 
                                "Chef de la SS et responsable de la mise en œuvre de la Solution finale", 
                                "Ministre de la Propagande", 
                                "Commandant en chef de la Wehrmacht", 
                                "Ministre de l'Air"],
                                
                                ["Quel était l'objectif du Lebensraum (espace vital) prôné par les nazis ?", 
                                "Étendre le territoire allemand en Europe de l'Est", 
                                "Favoriser l'émigration des Allemands", 
                                "Construire des colonies en Afrique", 
                                "Annexer les États-Unis"],
                                
                                ["Quel traité signé en 1939 a permis à Hitler de commencer la Seconde Guerre mondiale sans craindre une attaque à l'Est ?", 
                                "Le pacte germano-soviétique", 
                                "Le traité de Versailles", 
                                "Les accords de Munich", 
                                "Le pacte de Varsovie"],
                                
                                ["Quelle organisation de jeunesse était destinée à endoctriner les jeunes allemands ?", 
                                "Jeunesses hitlériennes (Hitlerjugend)", 
                                "Ligue des jeunes communistes", 
                                "Jeunesses socialistes", 
                                "Jeunesses libérales"],
                                
                                ["Quel programme nazi visait à éliminer les personnes handicapées et malades mentales ?", 
                                "Action T4", 
                                "Solution finale", 
                                "Lebensraum", 
                                "Anschluss"],
                                
                                ["Quel était le principal instrument de la terreur nazie pour éliminer les opposants et maintenir le contrôle ?", 
                                "La Gestapo", 
                                "La Luftwaffe", 
                                "La Wehrmacht", 
                                "Le ministère de la Propagande"],
                                
                                ["Quel événement est considéré comme le début officiel de la Seconde Guerre mondiale ?", 
                                "L'invasion de la Pologne par l'Allemagne en 1939", 
                                "La Nuit de cristal en 1938", 
                                "L'annexion de l'Autriche en 1938", 
                                "La bataille de France en 1940"],
                                
                                ["Quel groupe était principalement ciblé par la politique d'euthanasie nazie ?", 
                                "Les handicapés et les malades mentaux", 
                                "Les communistes", 
                                "Les homosexuels", 
                                "Les Tziganes"],
                                
                                ["Quel était le principal camp de concentration nazi en Pologne ?", 
                                "Auschwitz", 
                                "Dachau", 
                                "Buchenwald", 
                                "Treblinka"],
                                
                                ["Quel événement a permis aux nazis de consolider leur pouvoir en éliminant les SA ?", 
                                "La Nuit des longs couteaux", 
                                "L'incendie du Reichstag", 
                                "La Kristallnacht", 
                                "L'Anschluss"],
                                
                                ["Quel terme désigne la propagande intensive utilisée par les nazis pour contrôler l'opinion publique ?", 
                                "Endoctrinement", 
                                "Brainstorming", 
                                "Infiltration", 
                                "Manipulation"],
                                
                                ["Quel symbole était utilisé par les nazis pour représenter leur idéologie ?", 
                                "La croix gammée (svastika)", 
                                "Le marteau et la faucille", 
                                "L'étoile rouge", 
                                "Le croissant de lune"],
                                
                                ["Quelle loi a permis à Hitler de gouverner par décrets sans consulter le Reichstag ?", 
                                "La loi des pleins pouvoirs (Ermächtigungsgesetz)", 
                                "La loi de Nuremberg", 
                                "La loi de protection du peuple allemand", 
                                "La loi sur la restauration du service civil"],
                                
                                ["Quel était le principal objectif des Jeunesses hitlériennes ?", 
                                "Former les jeunes allemands à l'idéologie nazie", 
                                "Former des artistes et des musiciens", 
                                "Encourager le commerce et l'industrie", 
                                "Promouvoir les sports et les loisirs"],
                                
                                ["Quel était le rôle du ministère de la Propagande dirigé par Goebbels ?", 
                                "Contrôler les médias et diffuser l'idéologie nazie", 
                                "Superviser les forces armées", 
                                "Gérer l'économie", 
                                "Organiser des événements sportifs"],
                                
                                ["Quelle organisation nazie était responsable de l'extermination systématique des Juifs ?", 
                                "Les SS", 
                                "La Wehrmacht", 
                                "La Luftwaffe", 
                                "Les Jeunesses hitlériennes"],
                                
                                ["Quel était le rôle du Tribunal de Nuremberg après la Seconde Guerre mondiale ?", 
                                "Jugement des principaux dirigeants nazis pour crimes de guerre", 
                                "Organisation de la reconstruction de l'Allemagne", 
                                "Gestion de l'économie allemande", 
                                "Répartition des territoires allemands"],
                                
                                ["Quel terme désigne le meurtre systématique de six millions de Juifs par les nazis ?", 
                                "Holocauste", 
                                "Génocide arménien", 
                                "Pogrom", 
                                "Déportation"],

                                # Partie 4 : Le nazisme : idéologie et pratiques nazies (12 questions)
                                ["Quelle idéologie raciale prônait la supériorité de la race aryenne ?", 
                                "Le nazisme", 
                                "Le fascisme", 
                                "Le communisme", 
                                "Le socialisme"],
                                
                                ["Quel concept de l'idéologie nazie justifiait l'expansion territoriale en Europe de l'Est ?", 
                                "Lebensraum", 
                                "Anschluss", 
                                "Blitzkrieg", 
                                "Détente"],
                                
                                ["Quelle organisation nazie était chargée de l'endoctrinement des enfants et des jeunes ?", 
                                "Les Jeunesses hitlériennes", 
                                "La Gestapo", 
                                "La Wehrmacht", 
                                "Les SA"],
                                
                                ["Quel livre écrit par Hitler exposait les idées nazies ?", 
                                "Mein Kampf", 
                                "Le Capital", 
                                "Le Manifeste du Parti communiste", 
                                "La Doctrine du fascisme"],
                                
                                ["Quel événement de 1938 a marqué le début des persécutions violentes des Juifs ?", 
                                "La Nuit de cristal", 
                                "L'incendie du Reichstag", 
                                "La Nuit des longs couteaux", 
                                "L'Anschluss"],
                                
                                ["Quel groupe était principalement ciblé par la politique d'euthanasie nazie ?", 
                                "Les handicapés et les malades mentaux", 
                                "Les communistes", 
                                "Les homosexuels", 
                                "Les Tziganes"],
                                
                                ["Quel symbole était utilisé par les nazis pour représenter leur idéologie ?", 
                                "La croix gammée (svastika)", 
                                "Le marteau et la faucille", 
                                "L'étoile rouge", 
                                "Le croissant de lune"],
                                
                                ["Quelle loi a permis à Hitler de gouverner par décrets sans consulter le Reichstag ?", 
                                "La loi des pleins pouvoirs (Ermächtigungsgesetz)", 
                                "La loi de Nuremberg", 
                                "La loi de protection du peuple allemand", 
                                "La loi sur la restauration du service civil"],
                                
                                ["Quel était le principal objectif des Jeunesses hitlériennes ?", 
                                "Former les jeunes allemands à l'idéologie nazie", 
                                "Former des artistes et des musiciens", 
                                "Encourager le commerce et l'industrie", 
                                "Promouvoir les sports et les loisirs"],
                                
                                ["Quel était le rôle du ministère de la Propagande dirigé par Goebbels ?", 
                                "Contrôler les médias et diffuser l'idéologie nazie", 
                                "Superviser les forces armées", 
                                "Gérer l'économie", 
                                "Organiser des événements sportifs"],
                                
                                ["Quelle organisation nazie était responsable de l'extermination systématique des Juifs ?", 
                                "Les SS", 
                                "La Wehrmacht", 
                                "La Luftwaffe", 
                                "Les Jeunesses hitlériennes"],
                                
                                ["Quel était le rôle du Tribunal de Nuremberg après la Seconde Guerre mondiale ?", 
                                "Jugement des principaux dirigeants nazis pour crimes de guerre", 
                                "Organisation de la reconstruction de l'Allemagne", 
                                "Gestion de l'économie allemande", 
                                "Répartition des territoires allemands"]
                                ]
                    qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                    self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                    self.énoncer.place(x=20,y=20)
                    réponse = [qts[1]]
                    self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                    self.score_affichage.place(x= 0, y=0)
                    aléa = random.randint(1,4)

                    cadre1 = Frame(self.parti_qts, background='black')
                    cadre1.place(x=60, y=100, width=80, height=80)
                    bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse(self, réponse, 50))
                    bouton1.place(x=5, y=5, height=70, width=70)
                    text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                    text_1.place(x= 200, y=aléa*100)

                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=60, y=200, width=80, height=80)
                    bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse(self, réponse , 50))
                    bouton2.place(x=5, y=5, height=70, width=70)
                    text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                    text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
                
                    cadre3 = Frame(self.parti_qts, background='black')
                    cadre3.place(x=60, y=300, width=80, height=80)
                    bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton3.place(x=5, y=5, height=70, width=70)
                    text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                    text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
                
                    cadre4 = Frame(self.parti_qts, background='black')
                    cadre4.place(x=60, y=400, width=80, height=80)
                    bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton4.place(x=5, y=5, height=70, width=70)
                    text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                    text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)
            
            class d2eme_guerre:
                def QCM(self):
                    base_de_donné = [
                                # Partie 1 : L'offensive allemande en 1940 et l'effondrement de la République (6 questions)
                                ["Quel événement marque le début de l'offensive allemande en 1940 ?", 
                                "L'invasion de la Pologne", 
                                "L'attaque de Pearl Harbor", 
                                "La bataille de Stalingrad", 
                                "L'opération Barbarossa"],
                                
                                ["Quel général français a demandé l'armistice avec l'Allemagne en juin 1940 ?", 
                                "Maréchal Pétain", 
                                "Charles de Gaulle", 
                                "Paul Reynaud", 
                                "Georges Clemenceau"],

                                ["Quel événement symbolise l'effondrement militaire de la France en 1940 ?", 
                                "La défaite de Dunkerque", 
                                "La prise de Paris", 
                                "La bataille de Normandie", 
                                "La libération de Strasbourg"],

                                ["Où le gouvernement français s'est-il réfugié après la défaite de 1940 ?", 
                                "Vichy", 
                                "Londres", 
                                "Berlin", 
                                "Alger"],

                                ["Quel était le principal objectif de l'offensive allemande en France en 1940 ?", 
                                "Envahir la France rapidement par la Blitzkrieg", 
                                "Obtenir des ressources naturelles", 
                                "Tester de nouvelles armes", 
                                "Faire une démonstration de force aérienne"],

                                ["Quel document officiel a marqué la fin de la Troisième République ?", 
                                "L'armistice du 22 juin 1940", 
                                "Le traité de Versailles", 
                                "La déclaration de guerre de 1939", 
                                "Le traité de Trianon"],

                                # Partie 2 : Le régime de Vichy, un régime autoritaire (5 questions)
                                ["Qui a dirigé le régime de Vichy ?", 
                                "Maréchal Pétain", 
                                "Charles de Gaulle", 
                                "Pierre Laval", 
                                "François Mitterrand"],

                                ["Comment s'appelle la police politique du régime de Vichy ?", 
                                "La Milice", 
                                "La Gestapo", 
                                "La Stasi", 
                                "Le NKVD"],

                                ["Quelle institution a été supprimée par le régime de Vichy ?", 
                                "Le Parlement", 
                                "L'armée", 
                                "L'église", 
                                "La justice"],

                                ["Quel était le slogan du régime de Vichy ?", 
                                "Travail, Famille, Patrie", 
                                "Liberté, Égalité, Fraternité", 
                                "Unité, Discipline, Travail", 
                                "Force et Honneur"],

                                ["Quelle politique a été promulguée par le régime de Vichy pour contrôler la presse ?", 
                                "La censure", 
                                "La liberté de la presse", 
                                "Le monopole d'État", 
                                "La nationalisation"],

                                # Partie 3 : Le régime de Vichy, la collaboration (4 questions)
                                ["Quel terme désigne la coopération du régime de Vichy avec l'Allemagne nazie ?", 
                                "La collaboration", 
                                "La résistance", 
                                "L'armistice", 
                                "L'occupation"],

                                ["Quel personnage était connu pour sa collaboration étroite avec les nazis ?", 
                                "Pierre Laval", 
                                "Charles de Gaulle", 
                                "Jean Moulin", 
                                "André Malraux"],

                                ["Quel accord de 1942 a renforcé la collaboration policière entre Vichy et l'Allemagne ?", 
                                "L'accord Bousquet", 
                                "Le traité de Versailles", 
                                "Le pacte germano-soviétique", 
                                "Le pacte de non-agression"],

                                ["Quelle politique économique a été adoptée par Vichy pour soutenir l'Allemagne ?", 
                                "La livraison de matières premières", 
                                "L'embargo commercial", 
                                "La fermeture des usines", 
                                "La nationalisation des banques"],

                                # Partie 4 : Le régime de Vichy, un régime antisémite (3 questions)
                                ["Quel statut a été promulgué par le régime de Vichy pour discriminer les Juifs ?", 
                                "Le statut des Juifs", 
                                "Le Code noir", 
                                "La Charte de l'Atlantique", 
                                "La loi sur les étrangers"],

                                ["Quelle rafle de 1942 a marqué la déportation massive des Juifs de Paris ?", 
                                "La rafle du Vél' d'Hiv'", 
                                "La rafle de Varsovie", 
                                "La nuit de Cristal", 
                                "La rafle de Drancy"],

                                ["Quel camp d'internement en France a été utilisé pour regrouper les Juifs avant leur déportation ?", 
                                "Drancy", 
                                "Auschwitz", 
                                "Dachau", 
                                "Bergen-Belsen"],

                                # Partie 5 : Le régime de Vichy, une idéologie : la Révolution nationale (3 questions)
                                ["Quel était l'objectif de la 'Révolution nationale' de Vichy ?", 
                                "Renforcer les valeurs traditionnelles", 
                                "Industrialiser la France", 
                                "Renforcer l'armée", 
                                "Promouvoir l'égalitarisme"],

                                ["Quel aspect social était mis en avant par la Révolution nationale ?", 
                                "La famille", 
                                "Le syndicalisme", 
                                "L'individualisme", 
                                "L'immigration"],

                                ["Quel groupe était exclu de la société selon les idéaux de la Révolution nationale ?", 
                                "Les Juifs", 
                                "Les paysans", 
                                "Les ouvriers", 
                                "Les catholiques"],

                                # Partie 6 : La résistance hors de France (3 questions)
                                ["Quel général a lancé l'appel du 18 juin 1940 ?", 
                                "Charles de Gaulle", 
                                "Philippe Pétain", 
                                "Jean Moulin", 
                                "André Malraux"],

                                ["Quel était le principal objectif des Forces françaises libres (FFL) ?", 
                                "Continuer la lutte contre l'Allemagne nazie", 
                                "Négocier avec le régime de Vichy", 
                                "Collaborer avec les Alliés", 
                                "Défendre les colonies françaises"],

                                ["Quelle ville est devenue le centre de la résistance française en exil ?", 
                                "Londres", 
                                "New York", 
                                "Moscou", 
                                "Alger"],

                                # Partie 7 : La résistance en France : la résistance intérieure (3 questions)
                                ["Quel réseau de résistance était dirigé par Jean Moulin ?", 
                                "Le Conseil national de la Résistance (CNR)", 
                                "La Milice", 
                                "Les FTP", 
                                "La Gestapo"],

                                ["Quelle était la principale activité des réseaux de résistance en France ?", 
                                "Sabotage et renseignement", 
                                "Collaboration", 
                                "Propagande pro-nazie", 
                                "Gestion des camps de concentration"],

                                ["Quel symbole est devenu emblématique de la résistance intérieure ?", 
                                "La croix de Lorraine", 
                                "La faucille et le marteau", 
                                "La croix gammée", 
                                "La colombe de la paix"],

                                # Partie 8 : L'unification de la résistance (2 questions)
                                ["Quel organisme a été créé pour unifier les différents mouvements de résistance en France ?", 
                                "Le Conseil national de la Résistance (CNR)", 
                                "La Milice", 
                                "Le Parti communiste français", 
                                "L'Assemblée nationale"],

                                ["Qui a été nommé président du CNR en 1943 ?", 
                                "Jean Moulin", 
                                "Charles de Gaulle", 
                                "André Malraux", 
                                "Philippe Pétain"],

                                # Partie 9 : La libération de la France et la refonte d'une république (9 questions)
                                ["Quelle opération a marqué le début de la libération de la France en 1944 ?", 
                                "Le débarquement de Normandie", 
                                "L'opération Barbarossa", 
                                "L'opération Market Garden", 
                                "La bataille de Stalingrad"],

                                ["Quel jour est connu sous le nom de 'Jour J' ?", 
                                "Le 6 juin 1944", 
                                "Le 8 mai 1945", 
                                "Le 11 novembre 1918", 
                                "Le 1er septembre 1939"],

                                ["Quelle ville a été libérée par les Alliés en août 1944 ?", 
                                "Paris", 
                                "Berlin", 
                                "Rome", 
                                "Varsovie"],

                                ["Quel rôle a joué la Résistance intérieure dans la libération de la France ?", 
                                "Soutien aux opérations militaires alliées", 
                                "Aucun rôle", 
                                "Organisation de la collaboration", 
                                "Mise en place du régime de Vichy"],

                                ["Quel a été le sort du maréchal Pétain après la libération ?", 
                                "Condamné à la prison à vie", 
                                "Exilé en Espagne", 
                                "Réélu président", 
                                "Déclaré héros national"],

                                ["Quel gouvernement a été formé à la libération de la France ?", 
                                "Le Gouvernement provisoire de la République française (GPRF)", 
                                "Le Directoire", 
                                "La Commune de Paris", 
                                "La IVe République"],

                                ["Qui était le chef du GPRF ?", 
                                "Charles de Gaulle", 
                                "Philippe Pétain", 
                                "Jean Moulin", 
                                "François Mitterrand"],

                                ["Quelle politique a été adoptée pour épurer la société française des collaborateurs ?", 
                                "L'épuration", 
                                "L'amnistie", 
                                "La nationalisation", 
                                "La censure"],

                                ["Quelle constitution a été adoptée après la libération pour fonder la Quatrième République ?", 
                                "La constitution de 1946", 
                                "La constitution de 1958", 
                                "La constitution de 1875", 
                                "La constitution de 1791"],
                                ]

                    qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                    self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                    self.énoncer.place(x=20,y=20)
                    réponse = [qts[1]]
                    self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                    self.score_affichage.place(x= 0, y=0)
                    aléa = random.randint(1,4)

                    cadre1 = Frame(self.parti_qts, background='black')
                    cadre1.place(x=60, y=100, width=80, height=80)
                    bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse(self, réponse, 50))
                    bouton1.place(x=5, y=5, height=70, width=70)
                    text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                    text_1.place(x= 200, y=aléa*100)

                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=60, y=200, width=80, height=80)
                    bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse(self, réponse , 50))
                    bouton2.place(x=5, y=5, height=70, width=70)
                    text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                    text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
                
                    cadre3 = Frame(self.parti_qts, background='black')
                    cadre3.place(x=60, y=300, width=80, height=80)
                    bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton3.place(x=5, y=5, height=70, width=70)
                    text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                    text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
                
                    cadre4 = Frame(self.parti_qts, background='black')
                    cadre4.place(x=60, y=400, width=80, height=80)
                    bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton4.place(x=5, y=5, height=70, width=70)
                    text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                    text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)
            class d1er_guerre:
                def QCM(self):
                    base_de_donné = [
                        # Partie 1 : Les principales dates (3 questions)
                        ["Quand la Première Guerre mondiale a-t-elle commencé ?", 
                        "28 juillet 1914", 
                        "1er août 1914", 
                        "11 novembre 1918", 
                        "28 juin 1914"],

                        ["Quand l'armistice de la Première Guerre mondiale a-t-il été signé ?", 
                        "11 novembre 1918", 
                        "28 juillet 1918", 
                        "1er septembre 1918", 
                        "8 mai 1918"],

                        ["Quand le traiter de Versaille a-t-il été signé ?", 
                        "28 juin 1918",
                        "11 novembre 1918", 
                        "28 juillet 1918",  
                        "8 mai 1918"],

                        ["Quand la bataille de la Marne a-t-elle eu lieu ?", 
                        "1914", 
                        "1916", 
                        "1915", 
                        "1917"],

                        # Partie 2 : Les événements (5 questions)
                        ["Quand a eu lieu la 1ère Révolution en Russie ?", 
                        "Février 1917", 
                        "Octobre 1917", 
                        "Mars 1918", 
                        "Novembre 1916"],

                        ["Quand a eu lieu la 2ème Révolution en Russie ?", 
                        "Octobre 1917", 
                        "Février 1917", 
                        "Mars 1918", 
                        "Novembre 1916"],

                        ["Quelle est la date de la bataille de Verdun ?", 
                        "1916", 
                        "1914", 
                        "1915", 
                        "1917"],

                        ["Quand les États-Unis sont-ils entrés en guerre lors de la Première Guerre mondiale ?", 
                        "1917", 
                        "1914", 
                        "1916", 
                        "1918"],

                        ["Quand a eu lieu le génocide arménien ?", 
                        "1915-1917", 
                        "1914-1916", 
                        "1916-1918", 
                        "1917-1919"],

                        ["Quand l'assassinat de François-Ferdinand a-t-il eu lieu ?", 
                        "28 juin 1914", 
                        "1er août 1914", 
                        "15 juillet 1914", 
                        "4 août 1914"],

                        # Partie 3 : Le traité de Versailles (1 question)
                        ["Pourquoi le traité de Versailles est-il appelé Diktat de Versailles ?", 
                        "Parce qu'il a été imposé à l'Allemagne sans négociation", 
                        "Parce qu'il a été signé à Versailles", 
                        "Parce qu'il a été accepté par toutes les nations", 
                        "Parce qu'il a été ratifié par le peuple allemand"],

                        # Partie 4 : Le bilan humain et les vainqueurs et perdants (2 questions)
                        ["Quel a été le bilan humain de la Première Guerre mondiale ?", 
                        "Environ 18 millions de morts", 
                        "Environ 10 millions de morts", 
                        "Environ 5 millions de morts", 
                        "Environ 25 millions de morts"],

                        ["Quels étaient les pays vainqueurs de la Première Guerre mondiale ?", 
                        "Les Alliés (France, Royaume-Uni, États-Unis, Italie)", 
                        "Les Puissances centrales (Allemagne, Autriche-Hongrie, Empire ottoman)", 
                        "Les Pays neutres (Suisse, Espagne, Suède)", 
                        "Les Pays colonisés"],

                        ["Quels étaient les principaux pays perdants de la Première Guerre mondiale ?", 
                        "Allemagne, Autriche-Hongrie, Empire ottoman", 
                        "France, Royaume-Uni, États-Unis", 
                        "Italie, Japon, Chine", 
                        "Russie, Belgique, Serbie"],
                    ]


                    qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                    self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                    self.énoncer.place(x=20,y=20)
                    réponse = [qts[1]]
                    self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                    self.score_affichage.place(x= 0, y=0)
                    aléa = random.randint(1,4)

                    cadre1 = Frame(self.parti_qts, background='black')
                    cadre1.place(x=60, y=100, width=80, height=80)
                    bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse(self, réponse, 50))
                    bouton1.place(x=5, y=5, height=70, width=70)
                    text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                    text_1.place(x= 200, y=aléa*100)

                    cadre2 = Frame(self.parti_qts, background='black')
                    cadre2.place(x=60, y=200, width=80, height=80)
                    bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse(self, réponse , 50))
                    bouton2.place(x=5, y=5, height=70, width=70)
                    text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                    text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
                
                    cadre3 = Frame(self.parti_qts, background='black')
                    cadre3.place(x=60, y=300, width=80, height=80)
                    bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton3.place(x=5, y=5, height=70, width=70)
                    text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                    text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
                
                    cadre4 = Frame(self.parti_qts, background='black')
                    cadre4.place(x=60, y=400, width=80, height=80)
                    bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse(self,réponse , 50))
                    bouton4.place(x=5, y=5, height=70, width=70)
                    text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                    text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)
                    

        class EMC:
            def QCM(self):
                base_de_donné = [["Quand et par quelle texte est créé la citoyenneté de L'UE ?",
                                        "Par le traité de Maastricht en 1992", 
                                        "Par La Déclaration des droits de l'homme et du citoyen du 26 août 1789",
                                        "Par la cinquième répubique suite à la guerre d'Algérie",
                                        "Par Emanuel Macron en 2020"],
                                 ["Quelle est la condition pour être citoyen de l'UE?",
                                        "Avoir la nationalité d'un des 27 pays le l'UE", 
                                        "Rester 5 ans dans l'UE",
                                        "Avoir la nationalité d'un des 52 pays européens",
                                        "Demander a un président de la république européen"],
                                 ["Quelle sont les valeurs de L'UE ?",
                                        "dignité humaine, liberté, égalité", 
                                        "liberté, égalité fraternité",
                                        "ein Reich, ein Volk, ein Fuhrer",
                                        "droit du travail, de l'égalité et du soutien"],
                                 ["Quelle sont les principles de L'UE ?",
                                        "démocratie, Etat de droit", 
                                        "liberté, égalité, fraternité",
                                        "dignité humaine, liberté, égalité",
                                        "Aucune"]
                                 ]

                qts = base_de_donné[random.randint(0, len(base_de_donné)-1)]
                self.énoncer = Label(self.parti_qts, text = qts[0], font = ("", 30))
                self.énoncer.place(x=20,y=20)
                self.score_affichage = Label(self.parti_qts, text = str(self.score) + " sur "+ str(self.score_sur))
                self.score_affichage.place(x= 0, y=0)
                réponse = [qts[1]]

                aléa = random.randint(1,4)

                cadre1 = Frame(self.parti_qts, background='black')
                cadre1.place(x=60, y=100, width=80, height=80)
                bouton1 = Button(cadre1, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse, 50) if aléa ==1 else self.question.mauvaise_réponse(self, réponse, 50))
                bouton1.place(x=5, y=5, height=70, width=70)
                text_1 = Label(self.parti_qts, text = qts[1], font = ("", 30))
                text_1.place(x= 200, y=aléa*100)

                cadre2 = Frame(self.parti_qts, background='black')
                cadre2.place(x=60, y=200, width=80, height=80)
                bouton2 = Button(cadre2, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==2 else self.question.mauvaise_réponse(self, réponse , 50))
                bouton2.place(x=5, y=5, height=70, width=70)
                text_2 = Label(self.parti_qts, text = qts[2], font = ("", 30))
                text_2.place(x= 200, y=aléa*100+100 if not aléa ==4 else 100)
            
                cadre3 = Frame(self.parti_qts, background='black')
                cadre3.place(x=60, y=300, width=80, height=80)
                bouton3 = Button(cadre3, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==3 else self.question.mauvaise_réponse(self,réponse , 50))
                bouton3.place(x=5, y=5, height=70, width=70)
                text_3 = Label(self.parti_qts, text = qts[3], font = ("", 30))
                text_3.place(x= 200, y=aléa*100-100 if not aléa ==1 else 400)
            
                cadre4 = Frame(self.parti_qts, background='black')
                cadre4.place(x=60, y=400, width=80, height=80)
                bouton4 = Button(cadre4, text = "       ", font=("", 80), command = lambda:self.question.bonne_réponse(self, réponse , 50) if aléa ==4 else self.question.mauvaise_réponse(self,réponse , 50))
                bouton4.place(x=5, y=5, height=70, width=70)
                text_4 = Label(self.parti_qts, text = qts[4], font = ("", 30))
                text_4.place(x= 200, y=aléa*100+200 if not aléa in [3,4] else aléa*100-200)

