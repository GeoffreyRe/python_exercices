class CompteBanquaire(object):
	def __init__(self, nom = "Dupont", solde = 1000):
		self.nom = nom
		self.solde = solde


	def depot(self,somme):
		self.solde += somme

	def retrait(self,somme):
		self.solde -= somme

	def affiche(self):
		print("titulaire du compte :",self.nom, "/Solde restant sur le compte :", self.solde)


if __main__ == "__name__":
	compte1 = CompteBanquaire("Duchmol", 800)
	compte1.depot(350)
	compte1.retrait(200)
	compte1.retrait(200)
	compte1.depot(3000)
	compte1.affiche()

	compte2 = CompteBanquaire()
	compte2.depot(25)
	compte2.affiche()

else : 
	print(bonjour)