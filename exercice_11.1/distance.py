""" exercice 11.1 de la page 174 du livre de référence "apprendre à programmer en python 3" de Gérard swinnen 
ENONCE : 
Écrivez une fonction distance() qui permette de calculer la distance entre deux points.
(Il faudra vous rappeler le théorème de Pythagore !)
Cette fonction attendra évidemment deux objets Point() comme arguments.
"""

from math import * # importation du module math pour l'utilisation de la fonction sqrt ainsi que fabs

# création d'une classe "Point", avec comme argument "Object" qui signifie que cette classe est une classe parente
class Point(object):
	"définition d'un point géométrique" # commentaire sur la classe


# définition d'une fonction distance(), qui prendra en paramètre 2 objets de la classe Point 
# et qui calculera la distance entre ces deux objets grâce au théorème de pythagore

def distance(point_1,point_2):
	return sqrt((fabs(point_1.x - point_2.x))**(2) + (fabs(point_1.y - point_2.y))**2) # calcul de la "taille" de l'hypothénuse ( = distance)


p1 = Point() # 1ere instance de la classe Point

# assignation d'attributs d'instance "x" et "y" à l'objet p1, ce sont ces coordonnées dans un plan en deux dimensions

p1.x = 15.5

p1.y = 12.222	

# deuxième instanciation de la classe Point + assignation d'attributs d'instance

p2 = Point()

p2.x = -125.17

p2.y = 34.26

# appel de la fonction avec les deux objets p1 et p2 en paramètre + "capture" du résultat dans une variable

distance_p1_p2 = distance(p1, p2)

# affichage de la distance

print(distance_p1_p2)

