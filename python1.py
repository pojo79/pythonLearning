import pygame
import time
import random

a = pygame.init()

WHITE = (255,255,255)
GRAY = (155,155,155)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,155,0)
FPS = 15

gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

pygame.display.update()

pygame.display.set_caption('Slither')

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [gameDisplay.get_width()/2, gameDisplay.get_height()/2])

def eatApple(block_size):
    randAppleX = round(random.randrange(0, gameDisplay.get_width()-block_size)/10)*10
    randAppleY = round(random.randrange(0, gameDisplay.get_height()-block_size)/10)*10

def drawSnake(block_size, snakelist):
    place = 0
    for XnY in snakelist:
        if XnY != snakelist[len(snakelist)-1]:
            place+=1
            if place % 2 == 0:
                drawColor = BLACK
            else:
                drawColor = GRAY
            pygame.draw.rect(gameDisplay, drawColor, [XnY[0],XnY[1],block_size,block_size])
        else:
            pygame.draw.rect(gameDisplay, GREEN, [XnY[0],XnY[1],block_size,block_size])
    
def gameLoop():
    
    gameExit = False
    gameOver = False
    lead_x = gameDisplay.get_width()/2
    lead_y = gameDisplay.get_height()/2
    x_change = 0
    y_change = 0
    block_size = 10

    randAppleX = round(random.randrange(0, gameDisplay.get_width()-block_size)/10)*10
    randAppleY = round(random.randrange(0, gameDisplay.get_height()-block_size)/10)*10
    
    snakeList = []
    
    
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(GRAY)
            message_to_screen("Game over, press 'C' to play again or 'Q' to quit", BLACK)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit= True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 0 - block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = 0- block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0
            


        lead_x += x_change
        lead_y += y_change

        if lead_x < 0 or lead_x >= gameDisplay.get_width() or lead_y < 0 or lead_y >= gameDisplay.get_height():
            gameOver = True

      
        
        gameDisplay.fill(WHITE)
        pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)  
        drawSnake(block_size, snakeList)

        for snakePart in snakeList[:-1]:
            if snakePart == snakeHead:
                gameOver = True
        

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, gameDisplay.get_width()-block_size)/10)*10
            randAppleY = round(random.randrange(0, gameDisplay.get_height()-block_size)/10)*10
        else:
            del snakeList[0]
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
            
gameLoop()     
