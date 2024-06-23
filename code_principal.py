import subprocess
import sys

try:
    print("importation de tkinter")
    from tkinter import *
except ImportError:
    print(f"Le module tkinter n'est pas installé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinter"])
    print(f"Le module tkinter a été installé avec succès.")
    from tkinter import *
try:
    print("importation de os")
    import os
except ImportError:
    print(f"Le module os n'est pas installé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "os"])
    print(f"Le module os a été installé avec succès.")
    import os
try:
    print("importation de PIL")
    from PIL import ImageTk, Image
except ImportError:
    print(f"Le module PIL n'est pas installé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    print(f"Le module PIL a été installé avec succès.")
    from PIL import ImageTk, Image
import bouton_math, bouton_pch, bouton_fra, bouton_histoire


fenetre = Tk()
fenetre.geometry("1440x780")

class Code:
    
    def __init__(self, fenetre):
        self.fenetre = fenetre
        chemin_actuel = os.path.abspath(__file__)
        self.boite = Frame(self.fenetre )

        self.boite.place(x=0,y=0, height=780, width= 1440)
        chemin_actuel = chemin_actuel.replace("code_principal.py", "image/menu_prin/Révision.png")
        image = Image.open(chemin_actuel)
        image = image.resize((1440, 780))
        self.image = ImageTk.PhotoImage(image)
        self.labelimage = Label(self.boite, image = self.image)
        self.labelimage.image = self.image 
        self.labelimage.place(x=0,y=0)
        g = bouton_math.init(fenetre = self.fenetre, boite =  self.boite)
        e = bouton_pch.init(fenetre = self.fenetre, boite =  self.boite)
        f = bouton_fra.init(fenetre = self.fenetre, boite =  self.boite)
        e = bouton_histoire.init(fenetre = self.fenetre, boite =  self.boite)



run = Code(fenetre)
fenetre.mainloop()