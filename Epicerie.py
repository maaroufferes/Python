PRIX_PAIN = 0.80
PRIX_LAIT = 1.50
PRIX_OEUFS = 2.20
PRIX_FROMAGE = 4.50
STOCK_PAIN = 50
STOCK_LAIT = 40
STOCK_OEUFS = 30
STOCK_FROMAGE = 15

def afficher_menu_produit():
    print("Code   Produit      Prix unitaire (TND)     Stock initial")
    print("1      PAIN             ", PRIX_PAIN, "         ", STOCK_PAIN)
    print("2      LAIT (L)         ", PRIX_LAIT, "         ", STOCK_LAIT)
    print("3      OEUFS (x6)       ", PRIX_OEUFS, "        ", STOCK_OEUFS)
    print("4      FROMAGE          ", PRIX_FROMAGE, "      ", STOCK_FROMAGE)

def est_code_valide(code):
    if code in [1, 2, 3, 4]:
        return True
    else:
        return False
    
def obtenir_nom(code):
    if code == 1:
        return "PAIN"
    elif code == 2:
        return "LAIT"
    elif code == 3:
        return "OEUFS"
    elif code == 4:
        return "FROMAGE"

def obtenir_prix(code):
    if code == 1:
        return PRIX_PAIN
    elif code == 2:
        return PRIX_LAIT
    elif code == 3:
        return PRIX_OEUFS
    elif code == 4:
        return PRIX_FROMAGE
    
def calculer_montant(quantite, code):
    prix = obtenir_prix(code)
    montant = quantite * prix
    return montant

def gerer_vente():
    global STOCK_PAIN, STOCK_LAIT, STOCK_OEUFS, STOCK_FROMAGE
    total_brut=0
    nb_articles=0
    nb_refus=0
    qp=0
    ql=0
    qo=0
    qf=0
    code=int(input("Entrez le code du produit (1-4) ou -1 pour terminer : "))
    while code!=-1:
        if est_code_valide(code):
            if code==1:
                qp=int(input("Entrez la quantité de PAIN : "))
                if qp<=STOCK_PAIN:
                    montant=calculer_montant(qp, code)
                    total_brut+=montant
                    nb_articles+=qp
                    STOCK_PAIN-=qp
                else:
                    print("Stock insuffisant pour PAIN.")
                    nb_refus+=1
            elif code==2:
                ql=int(input("Entrez la quantité de LAIT : "))
                if ql<=STOCK_LAIT:
                    montant=calculer_montant(ql, code)
                    total_brut+=montant
                    nb_articles+=ql
                    STOCK_LAIT-=ql
                else:
                    print("Stock insuffisant pour LAIT.")
                    nb_refus+=1
            elif code==3:
                qo=int(input("Entrez la quantité d'OEUFS : "))
                if qo<=STOCK_OEUFS:
                    montant=calculer_montant(qo, code)
                    total_brut+=montant
                    nb_articles+=qo
                    STOCK_OEUFS-=qo
                else:
                    print("Stock insuffisant pour OEUFS.")
                    nb_refus+=1
            elif code==4:
                qf=int(input("Entrez la quantité de FROMAGE : "))
                if qf<=STOCK_FROMAGE:
                    montant=calculer_montant(qf, code)
                    total_brut+=montant
                    nb_articles+=qf
                    STOCK_FROMAGE-=qf
                else:
                    print("Stock insuffisant pour FROMAGE.")
                    nb_refus+=1
        else:
            print("Code de produit invalide.")
        code=int(input("Entrez le code du produit (1-4) ou -1 pour terminer : "))
    return total_brut, nb_articles, nb_refus, qp, ql, qo, qf, STOCK_PAIN, STOCK_LAIT, STOCK_OEUFS, STOCK_FROMAGE


def appliquer_remise(total_brut):
    if total_brut>50:
        remise=total_brut*0.05
        total_net=total_brut-remise
    return total_net, remise


def afficher_rapport(total_brut,nb_articles,nb_refus,qp,ql,qo,qf,STOCK_PAIN,STOCK_LAIT,STOCK_OEUFS,STOCK_FROMAGE):
    print("Rapport de vente :")
    print("Total brut : ", total_brut, " TND")
    print("Nombre d'articles vendus : ", nb_articles)
    print("Nombre de refus de vente : ", nb_refus)
    print("Quantité vendue de PAIN : ", qp)
    print("Quantité vendue de LAIT : ", ql)
    print("Quantité vendue d'OEUFS : ", qo)
    print("Quantité vendue de FROMAGE : ", qf)
    print("Stock restant de PAIN : ", STOCK_PAIN)
    print("Stock restant de LAIT : ", STOCK_LAIT)
    print("Stock restant d'OEUFS : ", STOCK_OEUFS)
    print("Stock restant de FROMAGE : ", STOCK_FROMAGE)
    if total_brut>50:
        total_net, remise=appliquer_remise(total_brut)
        print("Remise appliquée : ", remise, " TND")
        print("Total net à payer : ", total_net, " TND")
    if STOCK_PAIN<5:
        print("Rupture de stock imminente pour PAIN.")
    if STOCK_LAIT<5:
        print("Rupture de stock imminente pour LAIT.")
    if STOCK_OEUFS<5:
        print("Rupture de stock imminente pour OEUFS.")
    if STOCK_FROMAGE<5:
        print("Rupture de stock imminente pour FROMAGE.")


afficher_menu_produit()
total_brut, nb_articles, nb_refus, qp, ql, qo, qf, STOCK_PAIN, STOCK_LAIT, STOCK_OEUFS, STOCK_FROMAGE = gerer_vente()
afficher_rapport(total_brut, nb_articles, nb_refus, qp, ql, qo, qf, STOCK_PAIN, STOCK_LAIT, STOCK_OEUFS, STOCK_FROMAGE)
