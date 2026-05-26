from tkinter import *
from time import *
score = 0

Niveau = 0
def cookie():    
    global score
    score+=1
    Label(fenetre, text="Score ="+ str(score)).grid(row=2)

def upgrade():
    global Niveau
    Niveau += 1
    Label(fenetre, text="Achete un worker, tu as actuellement "+ str(Niveau) +" workers").grid(row=2, column = 1 )


def passive():
    global score
    global Niveau
    score += Niveau
    fenetre.after(1000, passive)
    Label(fenetre, text="Score ="+ str(score)).grid(row=2)


def ouvrir_explications():
    fenetre_info = Toplevel(fenetre)
    fenetre_info.title("Explications des Workers")
    fenetre_info.geometry("300x150") 
    
    Label(fenetre_info, text="À quoi servent les Workers ?", font=("Arial", 12, "bold")).pack(pady=10)
    texte_explicatif = "Chaque worker acheté génère automatiquement\n1 cookie par seconde de manière passive !"
    Label(fenetre_info, text=texte_explicatif).pack(pady=5)
    
    Button(fenetre_info, text="Fermer", command=fenetre_info.destroy).pack(pady=10)
    
def détruire():
    fenetre_info = Toplevel(fenetre)
    fenetre.title("COOKIES")
    fenetre_info.geometry("1080x1080") 

    détruire()

fenetre = Tk()
fenetre.title("Cookie Clicker")
Label(fenetre, text="Voici le cookie cliqueur, click sur le cookie").grid(row=0)
#score
Label(fenetre, text="Score ="+ str(score)).grid(row=2)

fenetre.after(1000, passive)

#pour le bouton de cookie
photo = PhotoImage(file = r"M:\Mes Devoirs\TK\cookie.png") 
Button(fenetre, image=photo, command = cookie).grid(row=3)


#Pour acheter des workers
Label(fenetre, text="Achete un worker, tu as actuellement "+ str(Niveau) +" workers").grid(row=2, column = 1 )
Button(fenetre, text= "Acheter", command = upgrade).grid(row=3, column = 1)

Button(fenetre, text="Aide & Explications", command=ouvrir_explications).grid(row=4, column=0, columnspan=2, pady=10)

Button(fenetre, text= "tout détruire ?", command = détruire).grid(row=6)


mainloop()