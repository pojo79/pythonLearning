import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
GRAY = (155, 155, 155)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 1)
FPS = 20
NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270
FONT_SMALL = 50
FONT_LARGE = 85

game_display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.update()

pygame.display.set_caption('Slither')

snakeHeadimg = pygame.image.load('snakehead.png')
snakeBodyimg = pygame.image.load('snakebody.png')
mouseImg = pygame.image.load('mouse.png')

def message_to_screen(msg, color, y_displace=0, size=FONT_SMALL):
    textSurf, textRect = textObjects(msg, color, size)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [gameDisplay.get_width()/2, gameDisplay.get_height()/2])
    textRect.center = (game_display.get_width()/2, game_display.get_height()/2+y_displace)
    game_display.blit(textSurf, textRect)
    return textRect

def textObjects(msg, color, size):
    font = pygame.font.SysFont("kinnari", size)
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()

def getImage(img, direction):

    return

def getAppleLocation(block_size):
    randAppleX = round(random.randrange(0, game_display.get_width()-block_size)/10)*10
    randAppleY = round(random.randrange(0, game_display.get_height()-block_size)/10)*10
    return (randAppleX, randAppleY)

def drawSnake(block_size, snakelist):
    place = 0
    for XnY in snakelist:
        if XnY != snakelist[len(snakelist)-1]:
            rotatedBodyImg = pygame.transform.rotate(snakeBodyimg, XnY[2])
            game_display.blit(rotatedBodyImg, (XnY[0], XnY[1]))
        else:
            rotatedHeadimg = pygame.transform.rotate(snakeHeadimg, XnY[2])
            game_display.blit(rotatedHeadimg, (XnY[0], XnY[1]))

def game_intro():

    intro = True

    while intro:
        game_display.fill(WHITE)
        message_to_screen("Welcome to Slither",
                          GREEN,
                          -100,
                          FONT_LARGE)

        message_to_screen("Eat the mouse to grow the snake.",
                          BLACK,
                          0,
                          size=FONT_SMALL)

        message_to_screen("Don't eat yourself or leave the screen",
                          BLACK,
                          +40,
                          size=FONT_SMALL)

        message_to_screen("Press any key to start",
                          BLACK,
                          +80,
                          FONT_SMALL)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                  return

def pause():
    pause = True

    while pause:
        rect = message_to_screen("Game Paused", RED, 0, FONT_LARGE)
        pygame.display.update()
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pause = False
                        gameOver = True
                        gameExit = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pause = False

def gameLoop():
    
    gameExit = False
    gameOver = False
    lead_x = game_display.get_width()/2
    lead_y = game_display.get_height()/2
    x_change = 0
    y_change = -10
    block_size = 20
    apple_size = 30
    direction = NORTH

    appleLocation = getAppleLocation(apple_size)
    #randAppleX = round(random.randrange(0, gameDisplay.get_width()-apple_size))
    #randAppleY = round(random.randrange(0, gameDisplay.get_height()-apple_size))
    
    snakeList = []
    
    
    
    while not gameExit:

        while gameOver == True:
            rect1 = message_to_screen("Game Over", RED, -70, size=FONT_LARGE)
            rect2 = message_to_screen("Press 'C' to play again or 'Q' to quit", BLACK)
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
                    direction = EAST
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                    direction = WEST
                elif event.key == pygame.K_UP:
                    y_change = 0- block_size
                    x_change = 0
                    direction = NORTH
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0
                    direction = SOUTH
                elif event.key == pygame.K_SPACE:
                    pause()
            


        lead_x += x_change
        lead_y += y_change

        if lead_x < 0 or lead_x >= game_display.get_width() or lead_y < 0 or lead_y >= game_display.get_height():
            gameOver = True

      
        
        game_display.fill(WHITE)
        game_display.blit(mouseImg, appleLocation)
        #pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, apple_size, apple_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeHead.append(direction)
        snakeList.append(snakeHead)  
        drawSnake(block_size, snakeList)

        for snakePart in snakeList[:-1]:
            if snakePart[0] == snakeHead[0] and snakePart[1] == snakeHead[1]:
                gameOver = True

        if (lead_x > appleLocation[0] and lead_x < appleLocation[0] + apple_size or lead_x +block_size > appleLocation[0] and lead_x+block_size < appleLocation[0]+apple_size) \
            and (lead_y > appleLocation[1] and lead_y < appleLocation[1] + apple_size or lead_y +block_size > appleLocation[1] and lead_y+block_size < appleLocation[1] +apple_size):
                appleLocation = getAppleLocation(apple_size)
        else:
            del snakeList[0]
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()      
gameLoop()     