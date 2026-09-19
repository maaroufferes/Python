f=open("Etudiants.txt","w")
f.write("Ahmed Ben Ali, 20, GLSI1, 14.5\nNour Trabelsi, 19, GLSI1, 15.2\nLeila Mansouri, 21, GLSI2, 13.8\nYoussef Hakimi, 20, GLSI1, 12.9\nSarah Amri, 19, GLSI2, 16.1\n")
f.close()
def lire_fichier(nom_fichier):
        f=open(nom_fichier,"r")
        for ligne in f:
            print(ligne)
        f.close()
lire_fichier("Etudiants.txt")
def ajouter_etudiant(nom_fichier, nom, age, classe, note):
    f=open(nom_fichier,"a")
    f.write(nom+", "+str(age)+", "+classe+", "+str(note)+"\n")
    f.close()
ajouter_etudiant("Etudiants.txt", "Ghada Ben Salem", 20, "GLSI1", 14.8)
ajouter_etudiant("Etudiants.txt", "Mohamed Krimi", 21, "GLSI2", 13.5)
lire_fichier("Etudiants.txt")
def afficher_etudiants_propre(nom_fichier):
     f=open(nom_fichier,"r")
     for ligne in f:
            ligne=ligne.strip().split(", ")
            print("Nom: ", ligne[0])
            print("Age: ", ligne[1])
            print("Groupe: ", ligne[2])
            print("Moyenne: ", ligne[3])
     f.close()
afficher_etudiants_propre("Etudiants.txt")
def statistiques_etudiants(nom_fichier):
    f=open(nom_fichier,"r")
    total_etudiants=0
    total_notes=0
    total_etudiants_GLSI1=0
    total_etudiants_GLSI2=0
    meilleure_etudiant=""
    meilleure_note=0
    for ligne in f:
        ligne=ligne.strip().split(", ")
        total_etudiants+=1
        total_notes+=float(ligne[3])
        if ligne[2]=="GLSI1":
            total_etudiants_GLSI1+=1
        elif ligne[2]=="GLSI2":
            total_etudiants_GLSI2+=1
        if float(ligne[3])>meilleure_note:
            meilleure_note=float(ligne[3])
            meilleure_etudiant=ligne[0]
    f.close()
    print("Nombre total d'etudiants: ", total_etudiants)
    print("Moyenne generale: ", total_notes/total_etudiants)
    print("Nombre d'etudiants en GLSI1: ", total_etudiants_GLSI1)
    print("Nombre d'etudiants en GLSI2: ", total_etudiants_GLSI2)
    print("Le meilleure Etudiant: ", meilleure_etudiant, "avec une note de ", meilleure_note)
statistiques_etudiants("Etudiants.txt")

print("Menu:")
print("1. Afficher tous les etudiants")
print("2. Ajouter un etudiant")
print("3. Afficher les statistiques")
print("4. Lire le contenu brut du fichier")
while True:
    o=int(input("Entrez Commande: "))
    if o==1:
        afficher_etudiants_propre("Etudiants.txt")
    elif o==2:
        nom=input("Entrez le nom de l'etudiant: ")
        age=int(input("Entrez l'age de l'etudiant: "))
        classe=input("Entrez la classe de l'etudiant: ")
        note=float(input("Entrez la note de l'etudiant: "))
        ajouter_etudiant("Etudiants.txt", nom, age, classe, note)
    elif o==3:
        statistiques_etudiants("Etudiants.txt")
    elif o==4:
        lire_fichier("Etudiants.txt")
    elif o==0:
        print("Au revoir!")
        break
    else:
        print("Commande invalide, essayez encore.")
    
         
        

