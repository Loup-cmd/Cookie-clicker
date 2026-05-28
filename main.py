from tkinter import *
from time import *

score = 0

NiveauW = 0
NiveauM = 0

PrixW = 45
PrixM = 150

COOKIESPS = 0
COOKIESPSajout = 0

# stocke le temps de chaque clic
clics = []


def boucle():
    global COOKIESPSajout, clics

    maintenant = time()

    # garde seulement les clics de la dernière seconde
    clics = [t for t in clics if maintenant - t <= 1]

    COOKIESPSajout = len(clics)

    Label(
        fenetre,
        text=f"Score = {score} | Cookies/sec = {COOKIESPS + COOKIESPSajout}"
    ).grid(row=2)

    fenetre.after(50, boucle)


def cookie():
    global score, clics

    score += 1

    # ajoute le temps du clic
    clics.append(time())


def upgradeW():
    global NiveauW, score, PrixW, COOKIESPS

    if score >= PrixW:

        NiveauW += 1

        score -= PrixW

        PrixW += 10

        COOKIESPS += 1

        Label(
            fenetre,
            text=f"Tu as actuellement {NiveauW} workers, Prix actuel : {PrixW}"
        ).place(x=500, y=20)


def upgradeM():
    global NiveauM, score, PrixM, COOKIESPS

    if score >= PrixM:

        NiveauM += 1

        score -= PrixM

        PrixM += 10

        COOKIESPS += 2

        Label(
            fenetre,
            text=f"Tu as actuellement {NiveauM} Mamies, Prix actuel : {PrixM}"
        ).place(x=500, y=70)


def passive():
    global score, NiveauW, NiveauM

    score += NiveauW + (NiveauM * 2)

    fenetre.after(1000, passive)


def ouvrir_explications():

    fenetre_info = Toplevel(fenetre)

    fenetre_info.title("Explications")
    fenetre_info.geometry("350x180")

    Label(
        fenetre_info,
        text="À quoi servent les Workers ?",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    texte_explicatif = (
        "Chaque Worker génère 1 cookie/seconde.\n"
        "Chaque Mamie génère 2 cookies/seconde."
    )

    Label(
        fenetre_info,
        text=texte_explicatif
    ).pack(pady=10)

    Button(
        fenetre_info,
        text="Fermer",
        command=fenetre_info.destroy
    ).pack(pady=10)


def detruire():

    fenetre_info = Toplevel(fenetre)

    fenetre_info.title("COOKIES")
    fenetre_info.geometry("1080x1080")


# ---------------- FENÊTRE ---------------- #

fenetre = Tk()

fenetre.title("Cookie Clicker")
fenetre.geometry("900x600")

# titre
Label(
    fenetre,
    text="Voici le cookie cliqueur, clique sur le cookie"
).grid(row=0)

# score
Label(
    fenetre,
    text="Score = 0"
).grid(row=2)

# passive income
fenetre.after(1000, passive)

# bouton cookie
photo = PhotoImage(file=r".\cookie.png")

Button(
    fenetre,
    image=photo,
    command=cookie
).grid(row=3)

# Workers
Label(
    fenetre,
    text=f"Tu as actuellement {NiveauW} workers, Prix actuel : {PrixW}"
).place(x=500, y=20)

Button(
    fenetre,
    text="Acheter",
    command=upgradeW
).place(x=500, y=40)

# Mamies
Label(
    fenetre,
    text=f"Tu as actuellement {NiveauM} Mamies, Prix actuel : {PrixM}"
).place(x=500, y=70)

Button(
    fenetre,
    text="Acheter",
    command=upgradeM
).place(x=500, y=90)

# aide
Button(
    fenetre,
    text="Aide & Explications",
    command=ouvrir_explications
).grid(row=4, column=0, columnspan=2, pady=10)

# destruction
Button(
    fenetre,
    text="Tout détruire ?",
    command=detruire
).grid(row=6)

# boucle principale
boucle()

mainloop()
