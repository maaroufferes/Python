bibliotheque = [
{"titre": "Le Petit Prince", "auteur": "Saint-Exupéry", "annee": 1943, "disponible": True, "emprunteur": None},
{"titre": "Harry Potter et la Pierre Philosophale", "auteur": "J.K. Rowling", "annee": 1997, "disponible": True,
"emprunteur": None},
{"titre": "1984", "auteur": "George Orwell", "annee": 1949, "disponible": False, "emprunteur": "Ahmed"},
{"titre": "L'Étranger", "auteur": "Albert Camus", "annee": 1942, "disponible": True, "emprunteur": None},
{"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "annee": 1954, "disponible": True, "emprunteur": None}]

def afficher_livres(bibliotheque):
    print("Titre | Auteur | Année | Dispo | Emprunté par")
    print("────────────────────────────────────────────────────────────────────────────────")
    for i in range (len(bibliotheque)):
        print(bibliotheque[i]["titre"]," | ",bibliotheque[i]["auteur"]," | ",bibliotheque[i]["annee"]," | ",bibliotheque[i]["disponible"]," | ",bibliotheque[i]["emprunteur"])

def chercher_livres(bibliotheque, mot):
    livres_trouves = []
    for i in range (len(bibliotheque)):
        if mot.upper() in bibliotheque[i]["titre"].upper():
            livres_trouves.append(bibliotheque[i])
    return livres_trouves
def emprunter_livre(bibliotheque, titre, personne):
    resultat=chercher_livres(bibliotheque, titre)
    if (resultat==[])or(resultat[0]["disponible"]==False):
        print("Ton livre n´existe pas")
        return False
    else:
        resultat[0]["disponible"]=False
        resultat[0]["emprunteur"]=personne
        return True
def rendre (bibliotheque,titre):
    resultat=chercher_livres(bibliotheque, titre)
    if (resultat==[])or(resultat[0]["emprunteur"]==False):
        print("Ton livre n´existe pas")
        return False
    else:
        resultat[0]["disponible"]=True
        resultat[0]["emprunteur"]=None
        return True
def compter_disponibles(bibliotheque):
    n=0
    for i in range (len(bibliotheque)):
        if bibliotheque[i]["disponible"]==True:
            n+=1
    return n

def compter_empruntes(bibliotheque):
    n=0
    for i in range (len(bibliotheque)):
        if bibliotheque[i]["disponible"]==False:
            n+=1
    return n

def personne_qui_a_le_plus_emprunte(bibliotheque):
    n=0
    max=0
    for i in range (len(bibliotheque)):
        for j in range (len(bibliotheque)):
            if (bibliotheque[i]["emprunteur"]==bibliotheque[j]["emprunteur"])and(bibliotheque[i]["emprunteur"]!=None):
                n=+1
                if n>max:
                    max=n
                    return bibliotheque[i]["emprunteur"]
                elif n==max:
                    return bibliotheque[i]["emprunteur"]
                else:
                    return"Aucun emprunt"
nd=compter_disponibles(bibliotheque)
ne=compter_empruntes(bibliotheque)
nom=personne_qui_a_le_plus_emprunte(bibliotheque)
print("Nombre de livres disponibles :",nd)
print("Nombre de livres empruntés :",ne)
print("Personne qui a emprunté le plus de livres :",nom)


mon_nom=input("Comment vous appelez-vous? :")
print("========================================")
print("    Ma bibliotheque")
print("========================================")
print("   1. Voir tous les livres")
print("   2. Chercher un livre")
print("   3. Emprunter un livre")
print("   4. Rendre un livre")
print("   5. Voir mes emprunts")
print("   0. Quitter")
print("────────────────────────────────────────")
mon_choix=int(input("Votre choix :"))
while mon_choix!=-1:
    if mon_choix==1:
        afficher_livres(bibliotheque)
    elif mon_choix==2:
        mot=input("Mot à chercher :")
        resultat=chercher_livres(bibliotheque, mot)
        if resultat==[]:
         print("Aucun livre trouvé")
        else:
            for i in range (len(resultat)):
                print(resultat[i]["titre"]," | ",resultat[i]["auteur"]," | ",resultat[i]["annee"]," | ",resultat[i]["disponible"]," | ",resultat[i]["emprunteur"])
    elif mon_choix==3:
        titre=input("Titre du livre à emprunter :")
        if emprunter_livre(bibliotheque, titre, mon_nom):
            print("Livre emprunté avec succès")
        else:
            print("Échec de l'emprunt")
    elif mon_choix==4:
        titre=input("Titre du livre à rendre :")
        if rendre(bibliotheque, titre):
            print("Livre rendu avec succès")
        else:
            print("Échec du retour")
    elif mon_choix==5:
        print("Vos emprunts :")
        for i in range (len(bibliotheque)):
            if bibliotheque[i]["emprunteur"]==mon_nom:
                print(bibliotheque[i]["titre"]," | ",bibliotheque[i]["auteur"]," | ",bibliotheque[i]["annee"]," | ",bibliotheque[i]["disponible"]," | ",bibliotheque[i]["emprunteur"])
    elif mon_choix==0:
        print("Merci d'avoir utilisé notre bibliothèque !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")
    mon_choix=int(input("Votre choix :"))

    