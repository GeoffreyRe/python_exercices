valeur =[0,0,2,3,4,5,6,7,8,9,10,"Valet","Dame","Roi","As"]
couleur = ("coeur", "carreau","trèfle","pique")

liste = []
for j in range(4):
	for i in range(13):
		liste.append((i+2,j))

print(liste)

print("{} de {}".format(valeur[liste[12][0]],couleur[liste[12][1]]))