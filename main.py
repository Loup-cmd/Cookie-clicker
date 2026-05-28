from tkinter import *
from time import *
score = 0
score_after=0
Niveau = 0
def cookie():    
    global score
    score+=1
    Label(fenetre, text="Score ="+ str(score)).grid(row=2)

def upgrade():
    global Niveau
    global score
    if Niveau *2+50 <= score:
        Niveau += 1
        score = score-(Niveau *2+50)
        Label(fenetre, text="Score ="+ str(score)).grid(row=2)
        Label(fenetre, text="Achete un worker, tu as actuellement "+ str(Niveau) +" workers").grid(row=2, column = 1 )
        Label(fenetre, text=f"Un worker coûte actuemmement {Niveau *2+50} cookies").grid(row=3, column = 1 )

    else:
        fenetre_erreur = Toplevel(fenetre)
        fenetre_erreur.title("ERREUR")
        fenetre_erreur.geometry("550x150") 
        
        Label(fenetre_erreur, text="Pas assez de cookies", font=("Arial", 12, "bold")).pack(pady=10)
        texte_erreur = "Les workers ne sont pas gratuits ! tu n'as pas assez pour en acheter, travail un peu par toi même !"
        Label(fenetre_erreur, text=texte_erreur).pack(pady=5)
        
        Button(fenetre_erreur, text="Fermer", command=fenetre_erreur.destroy).pack(pady=10)
        

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

def cookie_par_sec():
    global score
    global score_after

    cps = score - score_after
    score_after = score

    Label(fenetre, text=f"{cps} Cookies par seconde").grid(row=3)

    fenetre.after(1000, cookie_par_sec)

fenetre = Tk()
fenetre.title("Cookie Clicker")
Label(fenetre, text="Voici le cookie cliqueur, click sur le cookie").grid(row=0)
#score
Label(fenetre, text="Score ="+ str(score)).grid(row=2)

fenetre.after(1000, passive)
fenetre.after(1000, cookie_par_sec)
#pour le bouton de cookie
photo = PhotoImage(file = r".\cookie.png") 
Button(fenetre, image=photo, command = cookie).grid(row=4)


#Pour acheter des workers
Label(fenetre, text="Achete un worker, tu as actuellement "+ str(Niveau) +" workers").grid(row=2, column = 1 )
Button(fenetre, text= "Acheter", command = upgrade).grid(row=4, column = 1)
Label(fenetre, text=f"Un worker coûte actuemmement {Niveau *2+50} cookies").grid(row=3, column = 1 )

Button(fenetre, text="Aide & Explications", command=ouvrir_explications).grid(row=5, column=0, columnspan=2, pady=10)

Button(fenetre, text= "tout détruire ?", command = détruire).grid(row=7)


mainloop()
