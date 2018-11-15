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
ENONCE 12.8 :
Complément de l’exercice précédent : définir deux joueurs A et B. Instancier deux jeux
de cartes (un pour chaque joueur) et les mélanger. Ensuite, à l’aide d’une boucle, tirer
52 fois une carte de chacun des deux jeux et comparer leurs valeurs. Si c’est la première
des deux qui a la valeur la plus élevée, on ajoute un point au joueur A. Si la situation
contraire se présente, on ajoute un point au joueur B. Si les deux valeurs sont
égales, on passe au tirage suivant. Au terme de la boucle, comparer les comptes de A et
B pour déterminer le gagnant.

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
	#méthode qui permet d'avoir le nom de la carte 

	def nom_carte(self, carte):
		valeur = carte[0] # la valeur de la carte = premier élément du tuple
		couleur = carte[1] # couleur de la carte = 2ème élément du tuple
		# conditions qui permettent de déterminer le "nom" de la couleur
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
			# conditions qui permettent de déterminer le "nom" de la valeur
			if valeur ==11 :
				valeur = "Valet"
			if valeur == 12 :
				valeur = "Dame"
			if valeur == 13 :
				valeur = "Roi"
			if valeur ==14 :
				valeur = "As"
			return valeur + " de " + couleur

	# méthode qui permet de mélanger le paquet
	def battre(self):
		random.shuffle(self.jeu) # la méthode "shuffle" permet de mélanger une liste
	# méthode qui permet de tirer la première carte du paquet
	def tirer(self):
		if len(self.jeu) == 0:
			return None
		else : 
			carte = self.jeu[0] # variable = au premier élément de la liste ( = première carte du paquet)
			self.jeu.remove(carte) # on retire la carte du jeu
			return carte

# on crée un jeu par Joueur et on mélange chaque paquet
jeu_A = JeuDeCartes()
jeu_A.battre()

jeu_B = JeuDeCartes()
jeu_B.battre()
# "compteur" de points pour chaque joueur
points_A = 0 

points_B = 0

# boucle qui permet de comparer la valeur de la carte tirée de chaque paquet
for n in range(53):
	carte_A = jeu_A.tirer()
	carte_B = jeu_B.tirer()
	if carte_A == None or carte_B == None:
		break
	print("le joueur A a tiré:", jeu_A.nom_carte(carte_A))
	print("le joueur B a tiré:",jeu_B.nom_carte(carte_B))
	# on compare les valeurs des deux cartes et on attribue le point au joueur avec la carte la plus forte
	if carte_A[0] > carte_B[0]:
		points_A +=1

	elif carte_A[0] < carte_B[0]:
		points_B +=1

	# on affiche le total des points de chaque joueur après chaque carte tirée

	print("le joueur A a:", points_A,"point(s)")
	print("le joueur B a:",points_B, "point(s)")
	input() 
# vérification du joueur qui a le plus de points + déclaration du vainqueur
if points_A > points_B : 
	vainqueur = "A"
if points_B > points_A :
	vainqueur = "B"
print("le jeu est terminé, le vainqueur est le joueur", vainqueur)
