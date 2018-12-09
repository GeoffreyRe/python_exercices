import pygame

map_list =[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

pygame.init()
resolution= (1000,500)

window_surface = pygame.display.set_mode(resolution)

image = pygame.image.load("perso.png").convert_alpha()

rect_perso = image.get_rect(center = (450,250))





def affichage(map_list):
	for index_l, line in enumerate(map_list):
		for index_sprite,sprite in enumerate(line):
			if sprite == 1 :
				tuples = (index_sprite*100, index_l*100)
				window_surface.blit(image,tuples)
		pygame.display.flip()

def trouver_perso(map_list):
	for index_l, line in enumerate(map_list):
		for index_sprite,sprite in enumerate(line):
			if sprite == 1 :
				position_x = index_sprite
				position_y = index_l
	return position_x, position_y


affichage(map_list)
print(map_list)


pygame.display.flip()

launched = True 

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				position_x, position_y = trouver_perso(map_list)
				if position_y == 0:
					break
				map_list[position_y][position_x] = 0
				map_list[(position_y - 1)][position_x] = 1
				window_surface.fill((0,0,0))
				affichage(map_list)
				rect_perso.y -= 100
			if event.key == pygame.K_DOWN:
				position_x, position_y = trouver_perso(map_list)
				if position_y == 4:
					break
				map_list[position_y][position_x] = 0
				map_list[position_y + 1][position_x] = 1
				window_surface.fill((0,0,0))
				affichage(map_list)
				rect_perso.y += 100
			if event.key == pygame.K_LEFT:
				position_x, position_y = trouver_perso(map_list)
				if position_x == 0:
					break
				map_list[position_y][position_x] = 0
				map_list[position_y][position_x - 1] = 1
				window_surface.fill((0,0,0))
				affichage(map_list)
				rect_perso.x -= 100
			if event.key == pygame.K_RIGHT:
				position_x, position_y = trouver_perso(map_list)
				if position_x == 9:
					break
				map_list[position_y][position_x] = 0
				map_list[position_y][position_x + 1] = 1
				window_surface.fill((0,0,0))
				affichage(map_list)
				rect_perso.x += 100









	





	
=======
>>>>>>> 43bd471d58f419397c56b87e4086eec077ec7a22
