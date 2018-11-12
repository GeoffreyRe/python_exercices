"""
ENONCE EX 12.4 :
Définissez une classe Satellite() qui permette d’instancier des objets simulant des satellites
artificiels lancés dans l’espace, autour de la terre. Le constructeur de cette
classe initialisera les attributs d’instance suivants, avec les valeurs par défaut indiquées
:
masse = 100, vitesse = 0.
Lorsque l’on instanciera un nouvel objet Satellite(), on pourra choisir son nom, sa
masse et sa vitesse.
Les méthodes suivantes seront définies :
• impulsion(force, duree) permettra de faire varier la vitesse du satellite. Pour savoir
comment, rappelez-vous votre cours de physique : la variation de vitesse Δv subie
par un objet de masse m soumis à l’action d’une force F pendant un temps t vaut
v=
F×t
m . Par exemple : un satellite de 300 kg qui subit une force de 600 Newtons
pendant 10 secondes voit sa vitesse augmenter (ou diminuer) de 20 m/s.
• affiche_vitesse() affichera le nom du satellite et sa vitesse courante.
• energie() renverra au programme appelant la valeur de l’énergie cinétique du satellite.
Rappel : l’énergie cinétique se calcule à l’aide de la formule Ec=
m×v**2/2
"""

class Satellite():
	# constructeur:
	def __init__(self, nom, masse = 100, vitesse = 0):
		self.nom = nom
		self.masse = masse
		self.vitesse = vitesse
	#définition des méthodes demandées
	def impulsion(self, force, duree):
		self.vitesse = (force*duree)/self.masse + self.vitesse

	def affiche_vitesse(self):
		print("nom du satelitte : {}, vitesse courante = {}".format(self.nom, self.vitesse)) #utilisation de la méthode format

	def energie(self):
		return (self.masse*self.vitesse**2)/2 #cf. formule de l'énergie cinétique

#test :
s1 = Satellite('Zoé', masse =250, vitesse =10)
s1.impulsion(500, 15)
s1.affiche_vitesse()
print(s1.energie())
s1.impulsion(500, 15)
s1.affiche_vitesse()
print(s1.energie())