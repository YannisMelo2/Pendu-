import random
from tkinter import *
from tkinter import simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno


# Liste de mots pour le jeu
mots = ["naruto", "onepiece", "fairytail", "vinlandsaga", "myheroacademia", "l'attaquedestitans", "hunterxhunter", "bluelock", "gamblingschool", "genshinimpact"]

# Choisir un mot au hasard
mot = random.choice(mots)

# Initialiser les variables
lettres_trouvees = []
lettres_fausses = []
erreurs = 0
tentatives = 0

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

#fonction pour donner son nom à la Partie
def demander_nom():
    nom_joueur = simpledialog.askstring("Nom du joueur", "Quel est votre nom ?")
    return nom_joueur

#Fonction pour sauvegarder le score
def enregistrer_scores():
    try:
        with open("scores.txt", "r") as f:
            scores = f.readlines()
        scores = [score.strip() for score in scores]
        return scores
    except FileNotFoundError:
        return []

#fonction pour afficher le score
def montrer_scores():
    scores = enregistrer_scores()
    if scores:
        score_str = "Historique des scores :\n\n" + "\n".join(scores)
    else:
        score_str = "Aucun score enregistré pour l'instant."
    showinfo("Scores", score_str)

#Fonction pour donner un indice au joueur
def get_hint():
    hint_type = random.choice(["lettre", "nombre"])
    if hint_type == "lettre":
        letters_not_found = set(mot) - set(lettres_trouvees)
        if letters_not_found:
            random_letter = random.choice(list(letters_not_found))
            lettres_trouvees.append(random_letter)
            afficher_mot()
            showinfo("Indice", f"Il y a la lettre '{random_letter}'dans le mot !")
    else:
        letters_not_found = set(mot) - set(lettres_trouvees)
        nb_letters_not_found = len(letters_not_found)
        if nb_letters_not_found > 0:
            showinfo("Indice", f"Il y a {nb_letters_not_found} lettres dans le mot qui n'ont pas encore été trouvées.")

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

def sauvegarder_score(nom, tentatives):
    with open("scores.txt", "a") as f:
        f.write(f"{nom} a trouvé le mot '{mot}' en {tentatives}tentatives\n")


#personnalisation fonction aide
def aide() : 
    showinfo("Règles du pendu", "Le but du jeu est simple : deviner toute les lettres qui doivent composer un mot, éventuellement avec un nombre limité de tentatives et des thèmes fixés à l'avance. A chaque fois que le joueur devine une lettre, celle-ci est affichée. Dans le cas contraire, le dessin d'un pendu se met à apparaître...")

#Créer l'interface graphique
fenetre = Tk()
fenetre.title("Jeu du Pendu")
fenetre.geometry("400x400")

#Liste d'images pour le pendu
pendu_images = [
PhotoImage(file="pendu0.png"),
PhotoImage(file="pendu1.png"),
PhotoImage(file="pendu2.png"),
PhotoImage(file="pendu3.png"),
PhotoImage(file="pendu4.png"),
PhotoImage(file="pendu5.png"),
PhotoImage(file="pendu6.png"),
PhotoImage(file="pendu7.png")
]

#Fonction pour quitter la partie depuis le menu
def quitter(): 
    if askyesno('Fermeture', 'Êtes-vous sûr de vouloir fermer ?'): #si oui afficher les messages suivants
        fenetre.destroy()

# Fonction pour rejouer
def rejouer():
    global mot, lettres_trouvees, lettres_fausses, erreurs

    rejouer = askyesno("Jeu du Pendu", "Voulez-vous jouer à nouveau")

    mot = random.choice(mots)
    lettres_trouvees = []
    lettres_fausses = []
    erreurs = 0
    tentatives = 0
    afficher_pendu()
    afficher_mot()
    afficher_lettres()
    afficher_tentatives()


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

bouton1=Button(fenetre,text='Indice', command=get_hint)
bouton1.pack(padx=15)
bouton1.place(x=50, y=50)

menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle partie", command=rejouer)
menu1.add_separator()
menu1.add_command(label="Quitter", command=quitter)
menubar.add_cascade(label="Fichier", menu=menu1)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Règles du pendu", command=aide)
menubar.add_cascade(label="Aide", menu=menu3)

scores_menu = Menu(menubar, tearoff=0)
scores_menu.add_command(label="Afficher les scores",command=montrer_scores)
menubar.add_cascade(label="Scores", menu=scores_menu)

label_titre = Label(fenetre, text="Jeu du Pendu", bg="green")
label_titre.pack()

fenetre.config(menu=menubar)

#Appeler les fonctions pour afficher les éléments initiaux
afficher_mot()
afficher_tentatives()

#Boucle principale
fenetre.mainloop()



