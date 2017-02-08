import pygame
import time
import random

pygame.init()

white  = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width,display_hight))
pygame.display.set_caption('slang zoekt eten')





clock = pygame.time.Clock()

block_size = 10
FPS = 10

font = pygame.font.SysFont(None,30)

def messages_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [display_hight/2, display_width/2])

def  gameLoop ():
    gameExit = False
    gameOver = False

    lead_x = display_hight /2
    lead_y = display_width /2

    lead_x_change = 0
    lead_y_change = 0

    randAppelX = random.randrange (0, display_width-block_size)
    randAppely = random.randrange (0, display_hight-block_size)

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            messages_to_screen("drup op q om te stoppen of druk op c om opnieuwe te beginnen",black)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver =False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = - block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = - block_size
                    lead_x_change =  0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_hight or lead_y <0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change


        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay,red,[randAppelX, randAppely,block_size, block_size])
        pygame.draw.rect(gameDisplay,black, [lead_x,lead_y,10,10])





        pygame.draw.rect(gameDisplay, black, [790,0,10,600])
        pygame.draw.rect(gameDisplay, black, [0, 0, 10, 600])
        pygame.draw.rect(gameDisplay, black, [0, 0, 800, 10])
        pygame.draw.rect(gameDisplay, black, [0, 590, 800, 10])

        pygame.display.update()

        clock.tick(FPS)


    pygame.quit()
    quit()

gameLoop()