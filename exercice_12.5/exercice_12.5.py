""" ENONCE 12.5:
Définissez une classe Cercle(). Les objets construits à partir de cette classe seront des
cercles de tailles variées. En plus de la méthode constructeur (qui utilisera donc un paramètre
rayon), vous définirez une méthode surface(), qui devra renvoyer la surface
du cercle.
Définissez ensuite une classe Cylindre() dérivée de la précédente. Le constructeur de
cette nouvelle classe comportera les deux paramètres rayon et hauteur. Vous y ajouterez
une méthode volume() qui devra renvoyer le volume du cylindre (rappel : volume
d’un cylindre = surface de section × hauteur).

ENONCE 12.6:
Complétez l’exercice précédent en lui ajoutant encore une classe Cone(), qui devra dériver
cette fois de la classe Cylindre(), et dont le constructeur comportera lui aussi les
deux paramètres rayon et hauteur. Cette nouvelle classe possédera sa propre méthode
volume(), laquelle devra renvoyer le volume du cône (rappel : volume d’un cône
= volume du cylindre correspondant divisé par 3).
"""
from math import pi

# classe Cercle = Classe mère
class Cercle(object):
	def __init__(self, rayon):
		self.rayon = rayon

	def surface(self):
		return pi * (self.rayon)**2 #cf. formule de la surface d'un cercle

#classe Cylindre = classe fille de la classe Cercle
class Cylindre(Cercle):
	def __init__(self,rayon,hauteur):
		Cercle.__init__(self,rayon)
		self.hauteur = hauteur

	def volume(self):
		return pi*(self.rayon)**2*self.hauteur #cf formule du volume d'un cylindre

#classe Cone = classe fille de la classe Cylindre

class Cone(Cylindre):
	def __init__(self,rayon,hauteur):
		Cylindre.__init__(self,rayon,hauteur)

	# la méthode volume remplace la méthode volume de la classe Cylindre (exemple de polymorphisme)
	def volume(self):
		return Cylindre.volume(self)/3 #cf. formule du volume d'un cône

# programme principal de test:

c1 = Cercle(5)
print("la surface de ce cercle est de {}".format(c1.surface()))
cyl = Cylindre(5,7)
print("surface de section du cylindre =", cyl.surface())
print("volume du cylindre =",cyl.volume())
co = Cone(5,7)
print("surface de la base du cône =",co.surface())
print("volume du cône =",co.volume())

