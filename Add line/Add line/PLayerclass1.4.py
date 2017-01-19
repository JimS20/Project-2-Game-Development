
import pygame

red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)



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

        #Create Line
        self.Line = Lines()
        
        #Create player
        self.Player = Player(320, 470,red,Player(290,470,blue,Empty()))
        self.Current = self.Player

        self.draw()

    #Update game logic
    def update_question(self):
        #Update entities
         self.Player.update_question()
         if not self.IsEmpty == True:
            self.Player = self.Player.tail
         else:
            self.Player = self.Player

    def update_catagoryleft(self):
         self.Player.update_catagoryleft()
         if not self.Current == Empty:
            self.Current = self.Player.tail
         else:
            self.Current = self.Player

    def update_catagoryright(self):
         self.Player.update_catagoryright()
         if not self.Current == Empty:
            self.Current = self.Player.tail
         else:
            self.Current = self.Player
         

    #Draw everything
    def draw(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player.draw(self.screen)

        #Draw the score text
        #self.score_text = self.font.render("Score: {}".format(self.score),1,(255, 255, 255))
        #self.screen.blit(self.score_text,(16,16))

        #Flip the screen
        pygame.display.flip()

    #The game loop
    def game_loop(self):
        while not process_events():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.update_question()
                self.draw()

            if keys[pygame.K_LEFT]:
                self.update_catagoryleft()
                self.draw()

            if keys[pygame.K_RIGHT]:
                self.update_catagoryright()
                self.draw()

class Player:
   def __init__(self, posX, posY, color, tail):
       self.IsEmpty = False
       self.score = 0
       self.posX = posX
       self.posY = posY
       self.radius = 20 
       self.color = color
       self.tail = tail

   def update_question(self):
      
            if answer == True:
                self.score += 1
                self.posY += 0.25
                #next player here
   def update_catagoryleft(self):
        self.posX += 0.25

   def update_catagoryright(self):
        self.posX -= 0.25

    
   def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.posX), int(self.posY)), int(self.radius))
                            

class Lines:
    def draw(self,screen):
        pygame.draw.line(screen,red,(320,70),(320,470),10)
        pygame.draw.line(screen,yellow,(270,70),(270,470),10) 
        pygame.draw.line(screen,green,(220,70),(220,470),10)
        pygame.draw.line(screen,blue,(370,70),(370,470),10)

class Empty:
    def __init__(self):
        self.IsEmpty = True

empty = Empty()
    
    




    

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
    game.game_loop()
 
program()

