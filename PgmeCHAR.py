from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
from random import randint
t=array([int]*8)
def play ():
    chn=fen.vn.text()
    if (chn.isdecimal()) and (len(chn)==8) and (int(chn[0]) in [2,3,4,9]):
        n=int(chn)
        if gainperd (n):
            fen.l2.setText("le client ayant le numero de telephone "+chn+" a ganger un chariot gratuit")
        else :
            fen.l2.setText("le client ayant le numero de telephone "+chn+" doit payer les achats du chariot")                
    else :
        fen.l2.setText("desoler ! verifier le numero de telephone du client !!")
def gainperd (n):
    remp_affiche (t)
    while n>9 :
        ch=str(n)
        s=0
        for i in range (len(ch)):
            s=s+int(ch[i])
        n=s
    cc=n*n
    test=False
    i=0
    while (i<8) and not(test):
        if cc==t[i]:
            test=True
        else:
            i=i+1
    return (test)
    
        
def remp_affiche (t):
    for i in range (8):
        t[i]=randint(1,99)
        print(t[i],"|")


app = QApplication([])
fen = loadUi ("InterCHARIOT.ui")
fen.show()
fen.bv.clicked.connect (play)
app.exec_()