from exercice_12_2 import CompteBanquaire

class CompteEpargne(CompteBanquaire):
	def __init__(self, nom, solde,interet = 0.003):
		CompteBanquaire.__init__(self, nom, solde)
		self.interet = interet

	def changeTaux(self,valeur):
		self.interet = valeur

	def capitalisation(self,nombreMois):
		print("le nombre de mois est de {} mois".format(nombreMois))
		print("le taux d'intérêt en vigueur: {} %".format(self.interet* 100))
		self.solde = self.solde * (1 + self.interet)**nombreMois

#programme principal :
c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
c1.capitalisation(12)
c1.affiche()
c1.changeTaux(0.005)
c1.capitalisation(12)
c1.affiche()