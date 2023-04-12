import random
from tkinter import *
from tkinter.messagebox import showinfo 

# Liste de mots pour le jeu
mots = ["naruto", "one piece", "fairy tail", "vinland saga", "my hero academia", "l'attaque des titans", "hunterxhunter", "blue lock", "gambling school", "genshin impact"]

# Choisir un mot au hasard
mot = random.choice(mots)

# Initialiser les variables
lettres_trouvees = []
lettres_fausses = []
erreurs = 0

# Fonction pour afficher le pendu
def afficher_pendu():
    global erreurs
    pendu.config(image=pendu_images[erreurs])

# Fonction pour afficher le mot avec les lettres trouvées
def afficher_mot():
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "_ "
    mot_label.config(text=mot_affiche)

# Fonction pour afficher les lettres utilisées
def afficher_lettres():
    lettres_label.config(text="Lettres utilisées : " + ", ".join(lettres_fausses))

# Fonction pour afficher les tentatives restantes
def afficher_tentatives():
    tentatives_label.config(text="Tentatives restantes : " + str(len(pendu_images) - erreurs - 1))

# Fonction pour vérifier si le joueur a gagné ou perdu
def verifier_resultat():
    global erreurs
    if len(lettres_fausses) == len(pendu_images) - 1:
        afficher_pendu()
        showinfo("Jeu du Pendu", f"Vous avez perdu ! Le mot était {mot}")
        rejouer()
    elif set(mot) == set(lettres_trouvees):
        showinfo("Jeu du Pendu", f"Félicitations, vous avez gagné ! Le mot était {mot}")
        rejouer()

# Fonction pour rejouer
def rejouer():
    global mot, lettres_trouvees, lettres_fausses, erreurs
    mot = random.choice(mots)
    lettres_trouvees = []
    lettres_fausses = []
    erreurs = 0
    afficher_pendu()
    afficher_mot()
    afficher_lettres()
    afficher_tentatives()

from tkinter import *
from tkinter.messagebox import showinfo

# Fonction pour essayer une lettre
def essayer_lettre():
    global erreurs
    lettre = lettre_entry.get().lower()
    if not lettre.isalpha() or len(lettre) != 1:
        showinfo("Jeu du Pendu", "Veuillez entrer une seule lettre de l'alphabet !")
    elif lettre in lettres_trouvees or lettre in lettres_fausses:
        showinfo("Jeu du Pendu", "Vous avez déjà essayé cette lettre !")
    elif lettre in mot:
        lettres_trouvees.append(lettre)
        afficher_mot()
        verifier_resultat()
    else:
        lettres_fausses.append(lettre)
        erreurs += 1
        afficher_pendu()
        afficher_lettres()
        afficher_tentatives()
        verifier_resultat()
    lettre_entry.delete(0, END)

# Créer l'interface graphique
fenetre = Tk()
fenetre.title("Jeu du Pendu")
fenetre.geometry("400x400")

# Créer les widgets
pendu = Label(fenetre, image=pendu_images[0])
pendu.pack(pady=20)

label_titre = Label(fenetre, text="Jeu du Pendu", bg="yellow")
label_titre.pack()

mot_label = Label(fenetre, text="", font=("Arial", 24))
mot_label.pack(pady=20)

lettres_label = Label(fenetre, text="Lettres utilisées :")
lettres_label.pack(pady=10)

tentatives_label = Label(fenetre, text="Tentatives restantes :")
tentatives_label.pack(pady=10)

lettre_entry = Entry(fenetre, width=5)
lettre_entry.pack(pady=10)

essayer_lettre_button = Button(fenetre, text="Essayer", command=essayer_lettre)
essayer_lettre_button.pack(pady=10)

fenetre.mainloop()

