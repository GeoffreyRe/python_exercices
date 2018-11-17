""" 
Création d'un jeu de bataille sur base de l'exercice 12.7

"""
import random

class JeuDeCartes(object):

	valeurs= (0,0,2,3,4,5,6,7,8,9,10,"valet", "dame", "roi", "as")
	couleurs = ("coeur", "carreau", "trèfle", "pique")
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
		print("{} de {}".format(self.valeurs[valeur],self.couleurs[couleur]))

	# méthode qui permet de mélanger le paquet
	def battre(self):
		random.shuffle(self.jeu) # la méthode "shuffle" (importée depuis "random") permet de mélanger une liste
	# méthode qui permet de tirer la première carte du paquet
	def tirer(self):
		if len(self.jeu) == 0:
			return None
		else : 
			carte = self.jeu[0] # variable = au premier élément de la liste ( = première carte du paquet)
			self.jeu.remove(carte) # on retire la carte du jeu
			return carte

class Plateau(object):
	def __init__(self):
		self.carte_plateau =[] # liste qui représente les cartes sur la table

	# méthode qui permet de rajouter une carte à l'attribut "carte_plateau"
	def deposer(self, carte):
		self.carte_plateau.append(carte) 

	# méthode qui permet de donner toutes les cartes dans l'attribut "carte_plateau" à l'attribut "jeu" d'un joueur
	def donner_joueur(self, joueur):
		for i in self.carte_plateau:
			joueur.jeu.append(i)
		self.carte_plateau =[]


# programme principal : 
table = Plateau() 
joueur1 = JeuDeCartes()
joueur2 = JeuDeCartes()
joueur1.battre()
joueur2.battre()


while joueur1.jeu != [] or joueur2.jeu != []:
	 # on mélange le jeu des joueurs à chaque début de boucle
	joueur1.battre()
	joueur2.battre()
	carte_joueur1 = joueur1.tirer() # le joueur 1 sort une carte de son paquet
	if carte_joueur1 == None: # si le joueur n'a plus de carte, le jeu se termine
		break
	print("le joueur 1 a tiré :",end =" ") # on affiche le nom de la carte tirée
	joueur1.nom_carte(carte_joueur1) 
	table.deposer(carte_joueur1) # la carte est "mise sur la table"
	# idem pour le joueur 2
	carte_joueur2 = joueur2.tirer()
	if carte_joueur2 == None:
		break
	print("le joueur 2 a tiré :", end=" ") 
	joueur2.nom_carte(carte_joueur2)
	table.deposer(carte_joueur2)
	# comparaison des valeurs contenues dans les tuples des deux cartes pour identifier le vainqueur
	if carte_joueur1[0] > carte_joueur2[0]:
		print("le joueur 1 a gagné !")
		table.donner_joueur(joueur1)
	elif carte_joueur1[0] < carte_joueur2[0]:
		print("le joueur 2 a gagné")
		table.donner_joueur(joueur2)
	# si les deux cartes sont identiques (= mêmes valeurs), alors il y a un cas de "bataille"
	elif carte_joueur1[0] == carte_joueur2[0]:
		while carte_joueur1[0] == carte_joueur2[0]: # boucle qui permet d'avoir plusieurs cas de "bataille"
			print("Bataille !")
			# si un des joueurs n'a plus assez de cartes pour engager la bataille, alors il a perdu
			if len(joueur1.jeu) < 2:
				print("le joueur 1 n'a plus assez de cartes pour engager la bataille, il a donc perdu")
				while joueur1.jeu != []:
					joueur1.tirer()
				break
			if len(joueur2.jeu) <2:
				print("le joueur 2 n'a plus assez de cartes pour engager la bataille, il a donc perdu")
				while joueur2.jeu != []:
					joueur2.tirer()
				break
			print("Vous déposez chacun une carte face cachée")
			carte_joueur1 = joueur1.tirer()
			carte_joueur2 = joueur2.tirer()
			table.deposer(carte_joueur1)
			table.deposer(carte_joueur2)
			print("Vous deposez une nouvelle carte mais cette fois face découverte")
			carte_joueur1 = joueur1.tirer()
			carte_joueur2 = joueur2.tirer( )
			print("Le joueur 1 a tiré:", end=" ")
			joueur1.nom_carte(carte_joueur1)
			table.deposer(carte_joueur1)
			print("le joueur 2 a tiré:", end=" ")
			joueur2.nom_carte(carte_joueur2)
			table.deposer(carte_joueur2)
			# comparaison des valeurs pour déterminer le vainqueur de la bataille
			if carte_joueur1[0] > carte_joueur2[0]:
				print("le joueur 1 a gagné !")
				table.donner_joueur(joueur1)
			elif carte_joueur2[0] > carte_joueur1[0]:
				print("le joueur 2 a gagné !")
				table.donner_joueur(joueur2)

	# affichage du nombre de cartes de chaque joueur
	print("Le joueur 1 a {} carte(s) dans son paquet".format(len(joueur1.jeu)))
	print("le joueur 2 a {} carte(s) dans son paquet".format(len(joueur2.jeu)))

	# si le joueur 1 ou le joueur 2 n'a plus de carte dans son paquet, ce joueur a perdu la partie

	if joueur1.jeu == []:
		gagnant = "joueur 2"
		break 
	elif joueur2.jeu == []:
		gagnant = "joueur 1"
		break

	input()
# affichage du gagnant
print("le gagnant est le {}".format(gagnant))


