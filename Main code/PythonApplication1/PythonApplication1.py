"""Euromaster game
COPYRIGHT 2017, groep 6 beste"""

import pygame
import math

class Game:
    def __init__(self):
        # Set up resolution
        width = 640
        height = 480
        size = (width,height)

        #Start Pygame
        pygame.init()

        #Set the resolution
        self.screen = pygame.display.set_mode(size)

        #Set up the default font
        self.font = pygame.font.Font(None,30)

    #Update game logic
    def update(self):
        #Update entities
        self.player.update()
    #Draw everything
    def draw(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the entities
        self.player.draw(self.screen)

        #Draw the score text
        self.score_text = self.font.render("Score: {}".format(self.score),1,(255, 255, 255))
        self.screen.blit(self.score_text,(16,16))

        #Flip the screen
        pygame.display.flip()

    def update_score(self):
        self.score += 1
    `#The game loop
    def game_loop(self):
        while not process_events():
            self.update()
            self.draw()

class Player:
    def __init__(self, posX, posY):
        self.score = score
        self.posX = posX
        self.posY = posY

    def update(self):
        if answer == True:
            self.score += 1
            self.posY += 1
        #elif #Hoe gaan we naar volgende speler?
    #toevoegen draw functie hier

#Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Give signal to quit
            return True
    return False

#Main program logic
def program():
    game=Game()
     

            
           
           
            


        
            
         
        


