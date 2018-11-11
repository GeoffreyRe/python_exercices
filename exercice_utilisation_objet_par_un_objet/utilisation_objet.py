# Réalisation d'un petit exercice d'un objet de la classe "Rectangle" qui utilise un objet de la classe "Point".

#Création des deux classes 

class Point(object):
	"définition d'un point géométrique"



class Rectangle(object) : 
	"définition d'une classe de rectangle"


# instanciation de la classe Rectangle + attributs "largeur", "hauteur" et "coin"
boite = Rectangle()

boite.largeur = 50.0

boite.hauteur = 35.0

boite.coin = Point() # coin inférieur gauche ( = instanciation d'un objet à l'intérieur d'un autre objet)

boite.coin.x = 12.0 # attribut x  de l'objet coin de la classe Point

boite.coin.y = 27.0 # attribut y de l'objet coin de la classe Point

# définition d'une fonction qui "retourne" un objet de la classe Point et qui prend en paramètre un objet de la classe Rectangle
# cet objet "p" n'est rien d'autre que le centre de l'objet de la classe rectangle
def trouver_centre(box):
	p = Point()
	p.x = box.coin.x + box.largeur/2 
	p.y = box.coin.y + box.hauteur/2

	return p


p = trouver_centre(boite) # on capture cet objet dans une variable "p"

print("le point au centre du rectangle se trouve aux coordonnées (",p.x ,",", p.y, ")") # affichage des coordonnées du centre du rectangle