import pygame

a = pygame.init()
print(pygame)

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.update()

pygame.display.set_caption('Slither')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit= True

pygame.quit()
quit()
            
        
