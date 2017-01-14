import pygame

a = pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.update()

pygame.display.set_caption('Slither')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit= True

    gameDisplay.fill(WHITE)
    pygame.display.update()

    
pygame.quit()
quit()
            
        
