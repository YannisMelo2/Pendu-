import random

# Liste de mots pour le jeu
mots = ["naruto", "one piece", "fairy tail", "vinland saga", "my hero academia", "l'attaque des titans", "hunterxhunter", "blue lock", "gambling school", "genshin impact"]

# Choisir un mot au hasard
mot = random.choice(mots)

# Initialiser les variables
lettres_trouvees = []
lettres_fausses = []
pendu = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========''']

# Fonction pour afficher le pendu
def afficher_pendu(erreurs):
    print(pendu[erreurs])

# Fonction pour afficher le mot avec les lettres trouvées
def afficher_mot(mot, lettres_trouvees):
    for lettre in mot:
        if lettre in lettres_trouvees:
            print(lettre, end=" ")
        else:
            print("_", end=" ")
    print("")

# Boucle principale du jeu
while True:
    # Afficher le pendu et le mot actuel
    afficher_pendu(len(lettres_fausses))
    afficher_mot(mot, lettres_trouvees)

    # Demander à l'utilisateur de saisir une lettre
    lettre = input("Entrez une lettre : ")

    # Vérifier si la lettre est dans le mot
    if lettre in mot:
        lettres_trouvees.append(lettre)
    else:
        lettres_fausses.append(lettre)

    # Vérifier si le joueur a gagné ou perdu
    if len(lettres_fausses) == len(pendu) - 1:
        afficher_pendu(len(lettres_fausses))
        print("Vous avez perdu ! Le mot était", mot)
        break
    elif set(mot) == set(lettres_trouvees):
        print("Félicitations, vous avez gagné ! Le mot était", mot)
        break
