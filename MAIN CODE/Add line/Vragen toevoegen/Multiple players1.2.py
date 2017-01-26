import random
import pygame
import time

red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 150, 200)
orange = (220, 220, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_orange = (255, 255, 0)
block_color = (53, 115, 255)
sky_blue = (135, 206, 250)
lightsky_blue = (135, 206, 250)
green = (0, 220, 0)

display_width = 720
display_height = 480
gameDisplay = pygame.display.set_mode((display_width, display_height))

diceDisplay = pygame.display.set_mode((display_width, display_height))

winDisplay = pygame.display.set_mode((display_width, display_height))

menuDisplay = pygame.display.set_mode((display_width, display_height))

window = pygame.display.set_mode((720, 480))

#Plaatjes die de dobbelsteen getal laten zien
OneFace = pygame.image.load("images/1.png")
TwoFace = pygame.image.load("images/2.png")
ThreeFace = pygame.image.load("images/3.png")
FourFace = pygame.image.load("images/4.png")
FiveFace = pygame.image.load("images/5.png")
SixFace = pygame.image.load("images/6.png")
AllDice = pygame.image.load("images/6dicecubes.png")

background = pygame.image.load('images/Euromast.jpg')
Regels = pygame.image.load('images/Regels5.jpg')

top1 = '23123'
top2 = '2313'
top3 = '123'

score_List = str(top1) + '/n' + str(top2) + '/n' + str(top3) + '/n'

clock = pygame.time.Clock()

state = 0

pygame.display.set_caption('Quiz')

font = pygame.font.SysFont(None, 30)  

class Game2Player:
    def __init__(self):
        # Set up resolution
        width = 720
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
        self.Player1 = Player(320, 470,red,1)
        self.Player2 = Player(270,470,blue,2)
        self.Player = self.Player1
        self.draw()

    #Update game logic
    def update_question(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         else:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_question2(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         else:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_question3(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         else:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_catagoryleft(self):
         if self.Player.number == 1:
                self.Player.update_catagoryleft()
                print("hoi")
                self.Player = self.Player2
         else:
                self.Player.update_catagoryleft()
                print("hoi")
                self.Player = self.Player1

    def update_catagoryright(self):
         
         if self.Player.number == 1:
                self.Player.update_catagoryright()
                print("hoi")
                self.Player = self.Player2
         else:
                self.Player.update_catagoryright()
                print("hoi")
                self.Player = self.Player1

    def nextplayer(self):

         if self.Player.number == 1:
                self.Player = self.Player2
         else:
                self.Player = self.Player1
         

    #Draw everything
    def draw(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

        #Flip the screen
        pygame.display.flip()
    def drawcorrect(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

      
        self.answer_text = self.font.render("Correct!",10,(255, 255, 255))
        self.screen.blit(self.answer_text,(400,350))

        pygame.display.flip()
    
    def drawwrong(self):

        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

        self.answer_text = self.font.render("Fout!",10,(255, 255, 255))
        self.screen.blit(self.answer_text,(400,350))
        pygame.display.flip()


    #The game loop
    def game_loop(self):
        while not process_events():

            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        answer = rollDice()                      
                        if self.Player.posX == 320:#midden-rechter lijn
                            
                            if answer == "One":
                                if askquestion1():
                                    self.update_question()
                                    self.drawcorrect()

                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()



                            elif answer == "Two":
                                if askquestion1():
                                    self.update_question()
                                    self.drawcorrect()


                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()




                            elif answer == "Three":
                                if askquestion1():
                                    self.update_question2()
                                    self.drawcorrect()
                      

                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                         

                            elif answer == "Four":
                                if askquestion1():
                                    self.update_question2()
                                    self.drawcorrect()
                        
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                       



                            else:
                                if askquestion1():
                                    self.update_question3()
                                    self.drawcorrect()
                        
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                            


                        elif self.Player.posX == 370: #rechter lijn

                            if answer == "One":
                                if askquestion1():
                                    self.update_question()
                       
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                              
                                    self.drawwrong()

                            elif answer == "Two":
                                if askquestion1():
                                    self.update_question()
                           
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                              
                                    self.drawwrong()


                            elif answer == "Three":
                                if askquestion1():
                                    self.update_question2()
                            
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                          
                                    self.drawwrong()

                            elif answer == "Four":
                                if askquestion1():
                                    self.update_question2()
                                
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                           
                                    self.drawwrong()


                            else:
                                if askquestion1():
                                    self.update_question3()
                           
                                    self.drawcorrect()
                                    print(answer)

                                else:
                                    self.nextplayer()
                        
                                    self.drawwrong()
                            

                        elif self.Player.posX == 270:#midden-linker lijn
                            if answer == "One":
                                if askquestion2():
                                    self.update_question()
                                    self.drawcorrect()
                         
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                           

                            elif answer == "Two":
                                if askquestion2():
                                    self.update_question()
                                    self.drawcorrect()
                          
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                        


                            elif answer == "Three":
                                if askquestion2():
                                    self.update_question2()
                                    self.drawcorrect()
                        
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                         

                            elif answer == "Four":
                                if askquestion2():
                                    self.update_question2()
                                    self.drawcorrect()
                              
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                                 


                            else:
                                if askquestion2():
                                    self.update_question3()
                                    self.drawcorrect()
                        
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                        
                            


                        elif self.Player.posX == 220:#linker lijn

                            if answer == "One":
                                if askquestion2():
                                    self.update_question()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()

                            elif answer == "Two":
                                if askquestion2():
                                    self.update_question()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()


                            elif answer == "Three":
                                if askquestion2():
                                    self.update_question2()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()

                            elif answer == "Four":
                                if askquestion2():
                                    self.update_question2()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()


                            else:
                                if askquestion2():
                                    self.update_question3()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()
                          


                                

                    elif event.key == pygame.K_LEFT:
                        self.update_catagoryleft()
                        self.draw()

                
                    elif event.key == pygame.K_RIGHT:
                        self.update_catagoryright()
                        self.draw()

class Game3Player:
    def __init__(self):
        # Set up resolution
        width = 720
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
        self.Player1 = Player(320, 470,red,1)
        self.Player2 = Player(270,470,blue,2)
        self.Player3 = Player(220,470,yellow,3)
        self.Player = self.Player1
        self.draw()

    #Update game logic
    def update_question(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player3
         else:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_question2(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player3
         else:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_question3(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player3
         else:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_catagoryleft(self):
         if self.Player.number == 1:
                self.Player.update_catagoryleft()
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_catagoryleft()
                self.Player = self.Player3
         else:
                self.Player.update_catagoryleft()
                self.Player = self.Player1

    def update_catagoryright(self):
         
         if self.Player.number == 1:
                self.Player.update_catagoryright()
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_catagoryright()
                self.Player = self.Player3
         else:
                self.Player.update_catagoryright()
                self.Player = self.Player1

    def nextplayer(self):

         if self.Player.number == 1:
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player = self.Player3
         else:
                self.Player = self.Player1
         

    #Draw everything
    def draw(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)
        self.Player3.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

        #Flip the screen
        pygame.display.flip()
    def drawcorrect(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)
        self.Player3.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

      
        self.answer_text = self.font.render("Correct!",10,(255, 255, 255))
        self.screen.blit(self.answer_text,(400,350))

        pygame.display.flip()
    
    def drawwrong(self):

        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)
        self.Player3.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

        self.answer_text = self.font.render("Fout!",10,(255, 255, 255))
        self.screen.blit(self.answer_text,(400,350))
        pygame.display.flip()


    #The game loop
    def game_loop(self):
        while not process_events():

            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        answer = rollDice()                      
                        if self.Player.posX == 320:#midden-rechter lijn
                            
                            if answer == "One":
                                if askquestion1():
                                    self.update_question()
                                    self.drawcorrect()

                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()



                            elif answer == "Two":
                                if askquestion1():
                                    self.update_question()
                                    self.drawcorrect()


                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()




                            elif answer == "Three":
                                if askquestion1():
                                    self.update_question2()
                                    self.drawcorrect()
                      

                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                         

                            elif answer == "Four":
                                if askquestion1():
                                    self.update_question2()
                                    self.drawcorrect()
                        
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                       



                            else:
                                if askquestion1():
                                    self.update_question3()
                                    self.drawcorrect()
                        
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                            


                        elif self.Player.posX == 370: #rechter lijn

                            if answer == "One":
                                if askquestion1():
                                    self.update_question()
                       
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                              
                                    self.drawwrong()

                            elif answer == "Two":
                                if askquestion1():
                                    self.update_question()
                           
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                              
                                    self.drawwrong()


                            elif answer == "Three":
                                if askquestion1():
                                    self.update_question2()
                            
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                          
                                    self.drawwrong()

                            elif answer == "Four":
                                if askquestion1():
                                    self.update_question2()
                                
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                           
                                    self.drawwrong()


                            else:
                                if askquestion1():
                                    self.update_question3()
                           
                                    self.drawcorrect()
                                    print(answer)

                                else:
                                    self.nextplayer()
                        
                                    self.drawwrong()
                            

                        elif self.Player.posX == 270:#midden-linker lijn
                            if answer == "One":
                                if askquestion2():
                                    self.update_question()
                                    self.drawcorrect()
                         
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                           

                            elif answer == "Two":
                                if askquestion2():
                                    self.update_question()
                                    self.drawcorrect()
                          
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                        


                            elif answer == "Three":
                                if askquestion2():
                                    self.update_question2()
                                    self.drawcorrect()
                        
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                         

                            elif answer == "Four":
                                if askquestion2():
                                    self.update_question2()
                                    self.drawcorrect()
                              
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                                 


                            else:
                                if askquestion2():
                                    self.update_question3()
                                    self.drawcorrect()
                        
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                        
                            


                        elif self.Player.posX == 220:#linker lijn

                            if answer == "One":
                                if askquestion2():
                                    self.update_question()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()

                            elif answer == "Two":
                                if askquestion2():
                                    self.update_question()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()


                            elif answer == "Three":
                                if askquestion2():
                                    self.update_question2()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()

                            elif answer == "Four":
                                if askquestion2():
                                    self.update_question2()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()


                            else:
                                if askquestion2():
                                    self.update_question3()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()
                          


                                

                    elif event.key == pygame.K_LEFT:
                        self.update_catagoryleft()
                        self.draw()

                
                    elif event.key == pygame.K_RIGHT:
                        self.update_catagoryright()
                        self.draw()

class Game4Player:
    def __init__(self):
        # Set up resolution
        width = 720
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
        self.Player1 = Player(320, 470,red,1)
        self.Player2 = Player(270,470,blue,2)
        self.Player3 = Player(220,470,yellow,3)
        self.Player4 = Player(370,470,green,4)
        self.Player = self.Player1
        self.draw()

    #Update game logic
    def update_question(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player3
         elif self.Player.number == 3:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player4

         else:
                self.Player.update_question()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_question2(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player3

         elif self.Player.number == 3:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player4

         else:
                self.Player.update_question2()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_question3(self):
        #Update entities
         if self.Player.number == 1:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win()
                else:
                    self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player3

         elif self.Player.number == 3:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player4

         else:
                self.Player.update_question3()
                if self.Player.posY <= 70:
                    win2()
                else:
                    self.Player = self.Player1

    def update_catagoryleft(self):
         if self.Player.number == 1:
                self.Player.update_catagoryleft()
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_catagoryleft()
                self.Player = self.Player3
         elif self.Player.number == 3:
                self.Player.update_catagoryleft()
                self.Player = self.Player4
   

         else:
                self.Player.update_catagoryleft()
                self.Player = self.Player1

    def update_catagoryright(self):
         
         if self.Player.number == 1:
                self.Player.update_catagoryright()
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player.update_catagoryright()
                self.Player = self.Player3
         elif self.Player.number == 3:
                self.Player.update_catagoryright()
                self.Player = self.Player4
         else:
                self.Player.update_catagoryright()
                self.Player = self.Player1

    def nextplayer(self):

         if self.Player.number == 1:
                self.Player = self.Player2
         elif self.Player.number == 2:
                self.Player = self.Player3
         elif self.Player.number == 3:
                self.Player = self.Player4
         else:
                self.Player = self.Player1
         

    #Draw everything
    def draw(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)
        self.Player3.draw(self.screen)
        self.Player4.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

        #Flip the screen
        pygame.display.flip()
    def drawcorrect(self):
        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)
        self.Player3.draw(self.screen)
        self.Player4.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

      
        self.answer_text = self.font.render("Correct!",10,(255, 255, 255))
        self.screen.blit(self.answer_text,(400,350))

        pygame.display.flip()
    
    def drawwrong(self):

        #Clear the screen
        self.screen.fill((0, 0, 0))

        #Draw the lines
        self.Line.draw(self.screen)

        #Draw the players
        self.Player1.draw(self.screen)
        self.Player2.draw(self.screen)
        self.Player3.draw(self.screen)
        self.Player4.draw(self.screen)

        self.Player.drawturn(self.screen)

        #Draw the turn indicator
        self.score_text = self.font.render("Beurt van:",10,(255, 255, 255))
        self.screen.blit(self.score_text,(390,270))

        self.answer_text = self.font.render("Fout!",10,(255, 255, 255))
        self.screen.blit(self.answer_text,(400,350))
        pygame.display.flip()


    #The game loop
    def game_loop(self):
        while not process_events():

            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        answer = rollDice()                      
                        if self.Player.posX == 320:#midden-rechter lijn
                            
                            if answer == "One":
                                if askquestion1():
                                    self.update_question()
                                    self.drawcorrect()

                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()



                            elif answer == "Two":
                                if askquestion1():
                                    self.update_question()
                                    self.drawcorrect()


                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()




                            elif answer == "Three":
                                if askquestion1():
                                    self.update_question2()
                                    self.drawcorrect()
                      

                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                         

                            elif answer == "Four":
                                if askquestion1():
                                    self.update_question2()
                                    self.drawcorrect()
                        
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                       



                            else:
                                if askquestion1():
                                    self.update_question3()
                                    self.drawcorrect()
                        
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                            


                        elif self.Player.posX == 370: #rechter lijn

                            if answer == "One":
                                if askquestion1():
                                    self.update_question()
                       
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                              
                                    self.drawwrong()

                            elif answer == "Two":
                                if askquestion1():
                                    self.update_question()
                           
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                              
                                    self.drawwrong()


                            elif answer == "Three":
                                if askquestion1():
                                    self.update_question2()
                            
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                          
                                    self.drawwrong()

                            elif answer == "Four":
                                if askquestion1():
                                    self.update_question2()
                                
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                           
                                    self.drawwrong()


                            else:
                                if askquestion1():
                                    self.update_question3()
                           
                                    self.drawcorrect()
                                    print(answer)

                                else:
                                    self.nextplayer()
                        
                                    self.drawwrong()
                            

                        elif self.Player.posX == 270:#midden-linker lijn
                            if answer == "One":
                                if askquestion2():
                                    self.update_question()
                                    self.drawcorrect()
                         
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                           

                            elif answer == "Two":
                                if askquestion2():
                                    self.update_question()
                                    self.drawcorrect()
                          
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                        


                            elif answer == "Three":
                                if askquestion2():
                                    self.update_question2()
                                    self.drawcorrect()
                        
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                         

                            elif answer == "Four":
                                if askquestion2():
                                    self.update_question2()
                                    self.drawcorrect()
                              
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                                 


                            else:
                                if askquestion2():
                                    self.update_question3()
                                    self.drawcorrect()
                        
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.drawwrong()
                        
                            


                        elif self.Player.posX == 220:#linker lijn

                            if answer == "One":
                                if askquestion2():
                                    self.update_question()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()

                            elif answer == "Two":
                                if askquestion2():
                                    self.update_question()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()


                            elif answer == "Three":
                                if askquestion2():
                                    self.update_question2()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()

                            elif answer == "Four":
                                if askquestion2():
                                    self.update_question2()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)
 
                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()


                            else:
                                if askquestion2():
                                    self.update_question3()
                                    self.draw()
                                    self.drawcorrect()
                                    print(answer)

                                else:
                                    self.nextplayer()
                                    self.draw()
                                    self.drawwrong()
                          


                                

                    elif event.key == pygame.K_LEFT:
                        self.update_catagoryleft()
                        self.draw()

                
                    elif event.key == pygame.K_RIGHT:
                        self.update_catagoryright()
                        self.draw()

class Player:
   def __init__(self, posX, posY, color,number):
       self.score = 0
       self.posX = posX
       self.posY = posY
       self.radius = 20 
       self.color = color
       self.number = number

   def update_question(self):
        self.posY -= 40

   def update_question2(self):
        self.posY -= 80

   def update_question3(self):
        self.posY -= 120

   def update_catagoryleft(self):
        if self.posX == 220:
            self.posX = 370
        else:
            self.posX -= 50

   def update_catagoryright(self):
        if self.posX == 370:
            self.posX = 220
        else:
            self.posX += 50

    
   def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.posX), int(self.posY)), int(self.radius))

   def drawturn(self,screen):
            pygame.draw.circle(screen, self.color, (440, 320), 20)
                            

class Lines:
    def draw(self,screen):
        pygame.draw.line(screen,red,(320,70),(320,470),10)
        pygame.draw.line(screen,yellow,(270,70),(270,470),10) 
        pygame.draw.line(screen,green,(220,70),(220,470),10)
        pygame.draw.line(screen,blue,(370,70),(370,470),10)
    
    
class questions():  # vragen op het scherm
    def __init__(self, questions, answer1, answer2, answer3, correct):
        self.questions = questions
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct = correct

  
    
def askquestion1(): #categorie vragen 1

        a = questions(["waar woont Haroon"], ["A : Dordrecht-"], ["B : den haag"], ["C : rotterdam"], [pygame.K_a])
        b = questions(["waar woont jawed"], ["A : rotterdam"], ["B : Rijswijk-"], ["C : rotterdam"], [pygame.K_b])
        c = questions(["waar woont pietje"], ["A : rotterdam-"], ["B : Delft"], ["C : Haarlem"], [pygame.K_a])
        d = questions(["waar woont Anie"], ["A : Zoetermeer-"], ["B : Delft"], ["C : rotterdam"], [pygame.K_a])
        e = questions(["waar woont Milad"], ["A : rotterdam"], ["B : Delft-"], ["C : haarlem"], [pygame.K_b])
            
        def messages_to_screen(msg, color, lokatie1, lokatie2):  # massage hoe hij er uit moet zien en waar
                screen_text = font.render(msg, True, color)
                gameDisplay.blit(screen_text, [display_height / lokatie1, display_width / lokatie2])
        gameExit = False

        l = [a,b,c,d,e]
        random_selection = random.randint(0, len(l) - 1)

        while not gameExit:
                # vragen op de scherm krijgen
            gameDisplay.fill(red)
            messages_to_screen(l[random_selection].questions[0], black, 20, 50)
            messages_to_screen(l[random_selection].answer1[0], black, 20, 5)
            messages_to_screen(l[random_selection].answer2[0], black, 2, 5)
            messages_to_screen(l[random_selection].answer3[0], black, 1, 5)
            messages_to_screen("Kies A , B , C ", black, 9, 4)
            pygame.display.update()
        # knopjes linken
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if pygame.K_a == l[random_selection].correct[0]:
                            return True
                        else:
                            return False

                    if event.key == pygame.K_b:
                        if pygame.K_b == l[random_selection].correct[0]:
                            return True
                        else:
                            return False
                    if event.key == pygame.K_c:
                        if pygame.K_c == l[random_selection].correct[0]:
                            return True
                        else:
                            return False
                    if event.key == pygame.K_q:
                            break
        
def askquestion2(): #categorie vragen 2

        a = questions(["waar doet Haroon"], ["A : Dordrecht-"], ["B : den haag"], ["C : rotterdam"], [pygame.K_a])
        b = questions(["waar doet jawed"], ["A : rotterdam"], ["B : Rijswijk-"], ["C : rotterdam"], [pygame.K_b])
        c = questions(["waar doet pietje"], ["A : rotterdam-"], ["B : Delft"], ["C : Haarlem"], [pygame.K_a])
        d = questions(["waar doet Anie"], ["A : Zoetermeer-"], ["B : Delft"], ["C : rotterdam"], [pygame.K_a])
        e = questions(["waar doet Milad"], ["A : rotterdam"], ["B : Delft-"], ["C : haarlem"], [pygame.K_b])
            
        def messages_to_screen(msg, color, lokatie1, lokatie2):  # massage hoe hij er uit moet zien en waar
                screen_text = font.render(msg, True, color)
                gameDisplay.blit(screen_text, [display_height / lokatie1, display_width / lokatie2])
        gameExit = False

        l = [a,b,c,d,e]
        random_selection = random.randint(0, len(l) - 1)

        while not gameExit:
                # vragen op de scherm krijgen
            gameDisplay.fill(white)
            messages_to_screen(l[random_selection].questions[0], black, 20, 50)
            messages_to_screen(l[random_selection].answer1[0], black, 20, 5)
            messages_to_screen(l[random_selection].answer2[0], black, 2, 5)
            messages_to_screen(l[random_selection].answer3[0], black, 1, 5)
            messages_to_screen("Kies A , B , C ", black, 9, 4)
            pygame.display.update()
        # knopjes linken
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if pygame.K_a == l[random_selection].correct[0]:
                            return True
                        else:
                            return False

                    if event.key == pygame.K_b:
                        if pygame.K_b == l[random_selection].correct[0]:
                            return True
                        else:
                            return False
                    if event.key == pygame.K_c:
                        if pygame.K_c == l[random_selection].correct[0]:
                            return True
                        else:
                            return False
                    if event.key == pygame.K_q:
                            break

def rollDice():

     # message hoe hij er uit moet zien en waar
    def messages_to_screen(msg, color, lokatie1, lokatie2):
        screen_text = font.render(msg, True, color)
        diceDisplay.blit(screen_text, [display_height / lokatie1, display_width / lokatie2])

    ##als width weer 800 is en height 600 1,74, 3.5
    messages_to_screen("Jouw worp: ", white, 10,5) # 5, 5
    pygame.display.update()

    #
    GameLoop = True
    def game_loop():
        while GameLoop:
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    GameLoop=False
                    window.fill(white)


    def dicecurrentimage():
        diceCurrentImage = random.randint(1, 6)

        if diceCurrentImage == 1:
            return window.blit(OneFace, (60, 200))
        elif diceCurrentImage == 2:
            return window.blit(TwoFace, (60, 200))
        elif diceCurrentImage == 3:
            return window.blit(ThreeFace, (60, 200))
        elif diceCurrentImage == 4:
            return window.blit(FourFace, (60, 200))
        elif diceCurrentImage == 5:
            return window.blit(FiveFace, (60, 200))
        elif diceCurrentImage == 6:
            return window.blit(SixFace, (60, 200))


    diceCurrentImage = dicecurrentimage()

    pygame.display.flip()

    pygame.time.wait(3000)

    if diceCurrentImage == window.blit(OneFace, (60, 200)):
        return "One"
    elif diceCurrentImage == window.blit(TwoFace, (60, 200)):
        return "Two"
    elif diceCurrentImage == window.blit(ThreeFace, (60, 200)):
        return "Three"
    elif diceCurrentImage == window.blit(FourFace, (60, 200)):
        return "Four"
    elif diceCurrentImage == window.blit(FiveFace, (60, 200)):
        return "Five"
    else:
        return "Six"

 
def win():
       def messages_to_screen(msg, color, lokatie1, lokatie2):  # massage hoe hij er uit moet zien en waar
                screen_text = font.render(msg, True, color)
                winDisplay.blit(screen_text, [display_height / lokatie1, display_width / lokatie2])
       gameExit=False

       while not gameExit:
                # vragen op de scherm krijgen
            winDisplay.fill(red)
            messages_to_screen("Player 1 wins!", black, 9, 4)
            messages_to_screen("Press Q to return to main menu", black, 50, 10)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                            main_menu()

def win2():
       def messages_to_screen(msg, color, lokatie1, lokatie2):  # massage hoe hij er uit moet zien en waar
                screen_text = font.render(msg, True, color)
                winDisplay.blit(screen_text, [display_height / lokatie1, display_width / lokatie2])
       gameExit=False

       while not gameExit:
                # vragen op de scherm krijgen
            winDisplay.fill(red)
            messages_to_screen("Player 2 wins!", black, 9, 4)
            messages_to_screen("Press Q to return to main menu", black, 50, 10)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                            print("doei")            
    

#MENU------------------------------------------------------------
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    backgroundText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects(text, backgroundText)
    TextRect.center = ((display_width/2), (display_height/2))
    menuDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(1)

def text_Buttons(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()

def Button(message, x_coordinaat, y_coordinaat, breedte, hoogte, inactive, active, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_coordinaat + breedte > mouse[0] > x_coordinaat and y_coordinaat + hoogte > mouse[1] > y_coordinaat:
        pygame.draw.rect(menuDisplay, active, (x_coordinaat, y_coordinaat, breedte, hoogte))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(menuDisplay, inactive, (x_coordinaat, y_coordinaat, breedte, hoogte))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_Buttons(message, smallText)
    textRect.center = (x_coordinaat + (breedte / 2), y_coordinaat + (hoogte / 2))
    menuDisplay.blit(textSurf, textRect)
    if state == 1:
        textSurf, textRect = text_objects(score_List, smallText)
        textRect.center = (x_coordinaat + (display_width / 2), y_coordinaat + (display_height * 0.8))
        menuDisplay.blit(textSurf, textRect)

def state0(): #Main
    global state
    state = 0

def state1(): #Rules
    global state
    state = 1

def state2(): #Score
    global state
    state = 2

def state3(): #Game
    global state
    state = 3

def main_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if state == 0:
            menuDisplay.blit(pygame.transform.scale(background, (display_width, display_height)), (0, 0))
            Button('Start', 50, 100, 200, 50, green, bright_green,state3)
            Button('Rules', 50, 200, 200, 50, blue, bright_blue, state1)
            Button('Score', 50, 300, 200, 50, orange, bright_orange, state2)
            Button("Quit", 50, 400, 200, 50, red, bright_red, quitgame)

            largeText = pygame.font.Font('freesansbold.ttf', 60)
            TextSurf, TextRect = text_objects('The Euromaster', largeText)
            TextRect.center = ((display_width / 2), (display_height * 0.08))
            menuDisplay.blit(TextSurf, TextRect)

        elif state == 1:
            menuDisplay.blit(pygame.transform.scale(background, (display_width, display_height)), (0, 0))
            menuDisplay.blit(pygame.transform.scale(Regels, (display_width, display_height)), (10, 10))
            Button('Back', 500, 200, 200, 50, red, bright_red, state0)
        elif state == 2:
            menuDisplay.blit(pygame.transform.scale(background, (display_width, display_height)), (0, 0))
            Button(score_List, (display_width * 0.02), (display_height * 0.02),(display_width - (display_width * 0.04)), ((display_height * 0.7) - (display_width * 0.04)), sky_blue, lightsky_blue)
            Button('Back', 200, 400, 200, 50, red, bright_red, state0)

        elif state == 3:
            gameDisplay.blit(pygame.transform.scale(background, (display_width, display_height)), (0, 0))
            Button('Met hoeveel Spelers wilt U spelen?', (display_width * 0.2), 50, 500, 100, sky_blue, lightsky_blue)
            Button('2 Spelers', display_width * 0.1, (display_height/2), 200, 50, green, bright_green,playgame2)
            Button('3 Spelers', display_width * 0.4, (display_height / 2), 200, 50, green, bright_green,playgame3)
            Button('4 Spelers', display_width * 0.7, (display_height / 2), 200, 50, green, bright_green,playgame4)
            Button('Back', 50, 500, 200, 50, red, bright_red, state0)
            

        pygame.display.flip()


#Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Give signal to quit
            return True
    return False




#Main program logic
def playgame2():
    game=Game2Player()
    game.game_loop()

def playgame3():
    game=Game3Player()
    game.game_loop()

def playgame4():
    game=Game4Player()
    game.game_loop()
 
main_menu()

