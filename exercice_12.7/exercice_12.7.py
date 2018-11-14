"""
ENONCE 12.7 : 
Définissez une classe JeuDeCartes() permettant d’instancier des objets dont le comportement
soit similaire à celui d’un vrai jeu de cartes. La classe devra comporter au
moins les quatre méthodes suivantes :
• méthode constructeur : création et remplissage d’une liste de 52 éléments, qui sont
eux-mêmes des tuples de 2 entiers. Cette liste de tuples contiendra les caractéristiques
de chacune des 52 cartes. Pour chacune d’elles, il faut en effet mémoriser séparément
un entier indiquant la valeur (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, les 4 dernières
valeurs étant celles des valet, dame, roi et as), et un autre entier indiquant la
couleur de la carte (c’est-à-dire 3,2,1,0 pour Coeur, Carreau, Trèfle et Pique).
Dans une telle liste, l’élément (11,2) désigne donc le valet de Trèfle, et la liste terminée
doit être du type :
[(2, 0), (3,0), (3,0), (4,0), ..... (12,3), (13,3), (14,3)]
• méthode nom_carte() : cette méthode doit renvoyer, sous la forme d’une chaîne,
l’identité d’une carte quelconque dont on lui a fourni le tuple descripteur en argument.
Par exemple, l’instruction : print(jeu.nom_carte((14, 3))) doit provoquer
l’affichage de : As de pique
• méthode battre() : comme chacun sait, battre les cartes consiste à les mélanger.
Cette méthode sert donc à mélanger les éléments de la liste contenant les cartes,
quel qu’en soit le nombre.
• méthode tirer() : lorsque cette méthode est invoquée, une carte est retirée du jeu.
Le tuple contenant sa valeur et sa couleur est renvoyé au programme appelant. On
retire toujours la première carte de la liste. Si cette méthode est invoquée alors qu’il
ne reste plus aucune carte dans la liste, il faut alors renvoyer l’objet spécial None au
programme appelant. Exemple d’utilisation de la classe JeuDeCartes() :

"""
import random
#création de la classe JeuDeCartes

class JeuDeCartes(object):
	# constructeur
	def __init__(self):
		self.jeu =[] # création d'une liste qui contiendra les valeurs et les couleurs des 52 cartes (une carte = un tuple de 2 valeurs)
		i = 2 # variable correspondant à la valeur d'une carte
		j = 0 # variable correspondant à la couleur (où 0 = coeur, 1 = carreau , 2 = Trèfle et 3 = Pique)
		while len(self.jeu) < 52: # on veut un jeu de 52 cartes
			while i <= 14: # les valeurs vont de 2 à 14
				self.jeu.append((i,j))
				if i ==14:
					i = 2
					break # lorsqu'on a toutes les valeurs pour une couleur, on passe à la couleur suivante
				i += 1
			j +=1
	def nom_carte(self, carte):
		valeur = carte[0]
		couleur = carte[1]
		if couleur == 0 :
			couleur = "coeur"
		elif couleur == 1:
			couleur = "carreau"
		elif couleur == 2 :
			couleur = "trèfle"
		elif couleur == 3 :
			couleur = "pique"
		if valeur <=10:
			return str(valeur) + " de " + couleur
		elif valeur > 10:
			if valeur ==11 :
				valeur = "Valet"
			if valeur == 12 :
				valeur = "Dame"
			if valeur == 13 :
				valeur = "Roi"
			if valeur ==14 :
				valeur = "As"
			return valeur + " de " + couleur

	def battre(self):
		random.shuffle(self.jeu)

	def tirer(self):
		if len(self.jeu) == 0:
			return None
		else : 
			carte = self.jeu[0]
			self.jeu.remove(carte)
			return carte

jeu = JeuDeCartes() # instanciation d'un objet
jeu.battre() # mélange des cartes
for n in range(53): # tirage des 52 cartes :
	c = jeu.tirer()
	if c == None: # il ne reste plus aucune carte
		print("il n'y a plus de cartes à tirer") # dans la liste
	else:
		print(jeu.nom_carte(c))
		input()

