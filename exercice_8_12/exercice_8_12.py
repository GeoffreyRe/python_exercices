from tkinter import *
from math import * # nous voulons la fonction valeur absolue cad : fabs(x) ainsi que la fonction racine carrée cad:sqrt(x)
#définition des fonctions:
def bouger(astre,gd,hb):
	#cette fonction permet de changer les coordonnées des astres grâce à la méthode coords
	#on regarde de quel astre il s'agit pour pouvoir changer les bonnes coordonnées
	if astre==astre_rouge:
		global x1,y1
		x1,y1=x1+gd,y1+hb
		can1.coords(astre,x1,y1,x1+30,y1+30)
	elif astre==astre_bleu:
		global x2,y2
		x2,y2=x2+gd,y2+hb
		can1.coords(astre,x2,y2,x2+45,y2+45)
	#on appelle la fonction distance
	distance()
	
def force():
	# idem que bouger sauf que ça change le texte de la force gravitationelle
	global masse_rouge,masse_bleu,c,g
	if c==0:
		force_gravitationnelle.configure(text="force gravitationnelle= infini")
	else:
		#loi de Newton
		fg=g*((masse_rouge*masse_bleu)/(c**2))
		force_gravitationnelle.configure(text="force gravitationnelle= "+ str(fg) +" N") 
def distance():
	# permet de changer le texte de la distance grâce à la méthode configure
	#calcule la distance grâce au théorème de pythagore
	#change la force gravitationnelle 
	global x1,y1,x2,y2,a,b,c
	a=fabs(x2-x1)
	b=fabs(y2-y1)
	c=sqrt(a**2+b**2)
	text_distance.configure(text="distance: " + str(c) +" m")
	force()
# toutes ces fonctions permettent de faire les mouvements dans les 4 directions
def monter_astre_rouge():
	bouger(astre_rouge,0,-10)

def descendre_astre_rouge():
	bouger(astre_rouge,0,10)

def gauche_astre_rouge():
	bouger(astre_rouge,-10,0)

def droite_astre_rouge():
	bouger(astre_rouge,10,0)

def monter_astre_bleu():
	bouger(astre_bleu,0,-10)

def descendre_astre_bleu():
	bouger(astre_bleu,0,10)

def gauche_astre_bleu():
	bouger(astre_bleu,-10,0)

def droite_astre_bleu():
	bouger(astre_bleu,10,0)
#position initiale des deux astres+ calcul de la distance initiale:
x1,y1,x2,y2=50,50,150,150
a=fabs(x2-x1)
b=fabs(y2-y1)
c=sqrt(a**2+b**2)
masse_rouge=6e24
masse_bleu=6e24
g=6.67408*(10**(-11)) #constante de gravitation
fg=g*((masse_rouge*masse_bleu)/(c**2))
# widget principal
fen1=Tk()
#donne un titre à la fenêtre principale
fen1.title("illustration de 2 astres se mouvant")
#widgets esclaves
can1=Canvas(fen1,width=400,height=500,bg="grey") #crée un canevas
can1.grid(row=2,column=0,columnspan=2) #on le positionne grâce à la méthode grid
bou_quitter=Button(fen1, text="Quitter", command=fen1.quit) # on crée le bouton quitter
bou_quitter.grid(row=5,column=0,columnspan=2,sticky=N)
astre_rouge=can1.create_oval(x1,y1,x1+30,y1+30,fill="red")#on crée les deux astres 
astre_bleu=can1.create_oval(x2,y2,x2+45,y2+45,fill="blue")
fra1=Frame(fen1)
fra1.grid(row=4,column=0)
bou_monter_rouge=Button(fra1,text="^",fg="red",command=monter_astre_rouge).pack(side=LEFT)#on crée les deux boutons
bou_descendre_rouge=Button(fra1,text="\/",fg="red",command=descendre_astre_rouge).pack(side=LEFT)

bou_gauche_rouge=Button(fra1,text="<",fg="red",command=gauche_astre_rouge).pack(side=LEFT)
bou_droite_rouge=Button(fra1,text=">",fg="red",command=droite_astre_rouge).pack(side=LEFT)
fra2=Frame(fen1)
fra2.grid(row=4,column=1)
bou_monter_bleu=Button(fra2,text="^",fg="blue",command=monter_astre_bleu).pack(side=LEFT)
bou_descendre_bleu=Button(fra2,text="\/",fg="blue",command=descendre_astre_bleu).pack(side=LEFT)
bou_gauche_bleu=Button(fra2,text="<",fg="blue",command=gauche_astre_bleu).pack(side=LEFT)
bou_droite_bleu=Button(fra2,text=">",fg="blue",command=droite_astre_bleu).pack(side=LEFT)
text_distance=Label(fen1,text="distance: " + str(c)+" m")
text_distance.grid(row=3,column=0)#columnspan permet d'étaler le texte sur 3 "colonnes"
#programme principal concernant la gravitation:
Label(fen1,text="Masse astre rouge= "+str(masse_rouge)+" Kilos").grid(row=1, column=0)
Label(fen1,text="Masse astre bleu= "+str(masse_bleu)+" kilos").grid(row=1,column=1)
force_gravitationnelle=Label(fen1, text="force gravitationnelle= "+ str(fg) +" N")# dans ce cas-ci on ne peut pas l'appliquer directement car on l'utilise
#par la suite
force_gravitationnelle.grid(row=3,column=1)


fen1.mainloop()

fen1.destroy()