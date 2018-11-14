from random import randrange

liste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


for i in range(len(liste)):
	a,b = randrange(len(liste)), randrange(len(liste))
	liste[a], liste[b] = liste[b], liste[a]

print(liste)