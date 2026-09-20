from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def play ():
    n=fen.ln.text()
    m=fen.lm.text()    
    if not((10<=int(n)<=50) or (int(n)<int(m)<=200)) :
        fen.l1.setText("Veuillez respecter: 10<=N<=50 et N<M<=200")
    else:
        
        l=chercher(n,m)        
        if len(l)!=0:
            fen.l1.setText("Nombre(s) primaire(s) :"+str(l))
        else:
            fen.l1.setText("Aucun nombre primaires enter "+n+" et "+m)

def premier (x):
    test=True
    if x==1:
        test=False
    elif x>3 :
        k=2
        while test and (k<=x//2):
            if x%k==0 :
                test=False
            else:
                k=k+1
                
    return test

def verif (p):
    return premier(p)

def chercher(n,m):
    l=[]
    for i in range (int(n),int(m)+1):
        if verif(i):
            l.append(str(i))
    return l
        
        
            

     
    
    


app = QApplication([])
fen = loadUi ("InterfacesPrimaires.ui")
fen.show()
fen.ba.clicked.connect (play)
app.exec_()