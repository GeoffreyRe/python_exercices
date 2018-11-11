""" Exercice 12.1 
	
	Enoncé :

	Définissez une classe Domino() qui permette d’instancier des objets simulant les pièces
	d’un jeu de dominos. Le constructeur de cette classe initialisera les valeurs des points
	présents sur les deux faces A et B du domino (valeurs par défaut = 0).
	Deux autres méthodes seront définies :
	• une méthode affiche_points() qui affiche les points présents sur les deux faces ;
	• une méthode valeur() qui renvoie la somme des points présents sur les 2 faces.

"""

class Domino():
	""" Classe du jeu de domino"""

	# constructeur : 
	def __init__(self, a = 0, b = 0):

		# attributs : valeurs des points sur chaque face A et B

		self.face_A = a
		self.face_B = b

	# méthode affichant les points sur chaque face

	def affiche_points(self):
		print("points sur la face A: " + str(self.face_A) + " et points sur la face B : " + str(self.face_B))

	# méthode retournant la somme des points du domino

	def valeur(self):
		return self.face_A + self.face_B

#instanciation de la classe

dom1 = Domino(6,2)

#on applique les méthodes sur l'instance

dom1.affiche_points()
somme_dom1 = dom1.valeur()

print("la somme des deux faces du domino est",somme_dom1)
