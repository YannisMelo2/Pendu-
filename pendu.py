import random
from tkinter import *
from tkinter.messagebox import showinfo

# Liste de mots pour le jeu
mots = ["naruto", "onepiece", "fairytail", "vinlandsaga", "myheroacademia", "l'attaquedestitans", "hunterxhunter", "bluelock", "gamblingschool", "genshinimpact"]

# Choisir un mot au hasard
mot = random.choice(mots)

# Initialiser les variables
lettres_trouvees = []
lettres_fausses = []
erreurs = 0

# Fonction pour afficher le pendu
def afficher_pendu():
    global erreurs
    canvas.itemconfig(pendu, image=pendu_images[erreurs])

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
    tentatives_restantes = len(pendu_images) - erreurs - 1
    if tentatives_restantes == 1:
        tentatives_label.config(text="Il ne vous reste plus qu'une tentative !")
    else:
        tentatives_label.config(text="Tentatives restantes : " + str(tentatives_restantes))

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
    canvas.itemconfig(pendu, image=pendu_images[0])

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
#Créer l'interface graphique
fenetre = Tk()
fenetre.title("Jeu du Pendu")
fenetre.geometry("400x400")

#Liste d'images pour le pendu
pendu_images = [
PhotoImage(file="Pendu-/pendu0.png"),
PhotoImage(file="Pendu-/pendu1.png"),
PhotoImage(file="Pendu-/pendu2.png"),
PhotoImage(file="Pendu-/pendu3.png"),
PhotoImage(file="Pendu-/pendu4.png"),
PhotoImage(file="Pendu-/pendu5.png"),
PhotoImage(file="Pendu-/pendu6.png"),
PhotoImage(file="Pendu-/pendu7.png")
]

#créer les widgets
canvas = Canvas(fenetre, width=1096, height=500, bg="green")
canvas.pack()

pendu = canvas.create_image(0, 0, anchor="nw", image=pendu_images[0])

label_titre = Label(fenetre, text="JEU DU PENDU", bg="green", fg="white")
label_titre.pack()

mot_label = Label(fenetre, text="", font=("Arial", 24), bg="green", fg="white")
mot_label.pack(pady=20)

lettres_label = Label(fenetre, text="Lettres utilisées :", bg="green", fg="white")
lettres_label.pack(pady=10)

tentatives_label = Label(fenetre, text="Tentatives restantes :", bg="green", fg="white")
tentatives_label.pack(pady=10)

lettre_entry = Entry(fenetre, width=5, bg="white", fg="black")
lettre_entry.pack(pady=10)

essayer_lettre_button = Button(fenetre, text="Essayer", bg="white", fg="black", command=essayer_lettre)
essayer_lettre_button.pack(pady=10)

rejouer_button = Button(fenetre, text="Rejouer", bg="white", fg="black", command=rejouer, state=DISABLED)
rejouer_button.pack(pady=10)

quitter_button = Button(fenetre, text="Quitter", bg="white", fg="black", command=fenetre.quit)
quitter_button.pack(pady=10)


#Appeler les fonctions pour afficher les éléments initiaux
afficher_mot()
afficher_tentatives()

#Boucle principale
fenetre.mainloop()



