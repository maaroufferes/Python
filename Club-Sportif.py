club = {
    "nom_club": "Espoir GLSI",
    "sport": "Football",
    "joueurs": [
        {"nom": "Ahmed Ben Ali", "age": 20, "poste": "Attaquant", "buts": 7, "matches_joues": 8},
        {"nom": "Nour Trbelsi", "age": 19, "poste": "Milieu", "buts": 3, "matches_joues": 9},
        {"nom": "Leila Mansouri", "age": 21, "poste": "Defenseur", "buts": 1, "matches_joues": 10},
        {"nom": "Youssef Hakimi", "age": 20, "poste": "Gardien", "buts": 0, "matches_joues": 8},
    ],"matchs": []
}

def affiche_joueurs(joueurs):
    print("Nom          |Age    |Poste          |Buts   |Matches")
    print("-------------------------------------------------------")
    for i in joueurs:
        print(i["nom"], " |", i["age"], " |", i["poste"], " |", i["buts"], " |", i["matches_joues"])

def ajouter_joueur(joueurs):
    n = input("Nom: ")
    a = int(input("Age: "))
    p = input("Poste: ")
    joueurs.append({"nom": n, "age": a, "poste": p, "buts": 0, "matches_joues": 0})
    print("Ajoute avec succes")

def enregistrer_matches(matchs, date, adversaire, score_club, score_adversaire):
    matchs.append({"date": date, "adversaire": adversaire, "score_club": score_club, "score_adversaire": score_adversaire})
    print("Match Enregistre: Espoir GLSI ", score_club, "-", score_adversaire, " contre ", adversaire)

def afficher_matches(matchs):
    print("Date         |Adversaire      |Score")
    print("---------------------------------------")
    for i in matchs:
        print(i["date"], " |", i["adversaire"], " |", i["score_club"], "-", i["score_adversaire"])

def nombre_total_but(joueurs):
    tb = 0
    for i in joueurs:
        tb = tb + i["buts"]
    print("le nombres de but total : ", tb)

def meilleur_buteur(joueurs):
    max_buts = 0
    j = 0
    for i in joueurs:
        if max_buts < i["buts"]:
            max_buts = i["buts"]
            j = i
    
    print("Le meilleur buteur est: ", j["nom"])
def taux_victoire(matchs):
    w=0
    for i in matchs:
        if (i["score_club"]<i["score_adversaire"]):
            w=+1
    if w==0:
        print("Acune Matchs")
    else:
        print("Le Taux de Victoire est",(w/len(matchs)*100),"%")
print("1. Afficher tous les joueurs")
print("2. Ajouter un nouveau joueur")
print("3. Enregistrer un nouveau match")
print("4. Afficher l’historique des matchs") 
print("5. Afficher les statistiques du club") 
print("0. Quitter")
while True:
    choix = int(input("Choisissez une option: "))
    if choix == 1:
        affiche_joueurs(club["joueurs"])
    elif choix == 2:
        ajouter_joueur(club["joueurs"])
    elif choix == 3:
        date = input("Date du match: ")
        adversaire = input("Adversaire: ")
        score_club = int(input("Score du club: "))
        score_adversaire = int(input("Score de l'adversaire: "))
        enregistrer_matches(club["matchs"], date, adversaire, score_club, score_adversaire)
    elif choix == 4:
        afficher_matches(club["matchs"])
    elif choix == 5:
        nombre_total_but(club["joueurs"])
        meilleur_buteur(club["joueurs"])
        taux_victoire(club["matchs"])
    elif choix == 0:
        print("Merci d'avoir utilisé le programme!")
        break
    else:
        print("Option invalide.")



