import random

class JeuDeCartes(object):
	def __init__(self):
		self.jeu =[]
		i = 2
		j = 0
		while len(self.jeu) < 52:
			while i <= 14:
				self.jeu.append((i,j))
				if i ==14:
					i = 2
					break
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
print(jeu.jeu)
"""
jeu.battre() # mélange des cartes
for n in range(53): # tirage des 52 cartes :
	c = jeu.tirer()
	if c == None: # il ne reste plus aucune carte
		print("il n'y a plus de cartes à tirer") # dans la liste
	else:
		print(jeu.nom_carte(c))
		input()

"""




	

