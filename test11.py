import pygame
import time

pygame.init()
state = 0

display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 220, 0)
red = (200, 0, 0)
blue = (0, 150, 200)
orange = (220, 220, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_orange = (255, 255, 0)
block_color = (53, 115, 255)


gameDisplay = pygame.display.set_mode((display_width, display_height)) #resolutie
pygame.display.set_caption('Euromast GAME') #naam van de game op de balkje
clock = pygame.time.Clock() #tijd bijhouden

background = pygame.image.load('Euromast.jpg')
gameDisplay.blit(pygame.transform.scale(background, (display_width, display_height)), (0, 0)) #backrground stretchen vanaf punt (0, 0) (links boven)
pygame.display.flip()
pygame.display.update()

state = 0

def text_objects(text, font): #stukjes text om de naam van de knoppen aan te geven
    textSurface = font.render(text, True, black) #oppervlakte van de tekst = de text zelf en het zwart printen
    return textSurface, textSurface.get_rect() #de data van de oppervlakte terug sturen en het een blok maken

def message_display(text): #de naam van de pagina weer te geven
    backgroundText = pygame.font.Font('freesansbold.ttf', 80) #lettertype en grootte
    TextSurf, TextRect = text_objects(text, backgroundText) #text oppervlakte en blok = de text knoppen en ook de pagina text
    TextRect.center = ((display_width/2), (display_height/2)) #precies in het midden van de knop beginnen met printen van de naam van de knop
    gameDisplay.blit(TextSurf, TextRect) #texten weergeven

    pygame.display.update()

    time.sleep(1)

def quitgame():
    pygame.quit()
    quit()

def Button(message, x_coordinaat, y_coordinaat, breedte, hoogte, inactive, active, action=None): #start knop = naam van de knop, x, y, breedte van de knop en hoogte, inactive (als je niet met de muis overheen gaat), action is momenteel nog niks (zie game_intro en aan het einde van quitbutton)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_coordinaat + breedte > mouse[0] > x_coordinaat and y_coordinaat + hoogte > mouse[1] > y_coordinaat:
        pygame.draw.rect(gameDisplay, active, (x_coordinaat, y_coordinaat, breedte, hoogte)) #x + breedte van de knop is groter van de positie van de muis, muis pos is groter van x, en het zelfde met de y coordinaat
        if click[0] == 1 and action != None: #als click nog niet is gedrukt en daarna wel en er is nog geen actie uitgevoerd, dan een functie uitvoeren zoals quitgame()
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive, (x_coordinaat, y_coordinaat, breedte, hoogte)) #is niks veranderen (ook niet van kleur verandert

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(message, smallText)
    textRect.center = (x_coordinaat + (breedte / 2), y_coordinaat + (hoogte / 2))
    gameDisplay.blit(textSurf, textRect)

def stateblah():
    global state
    state = 1

def rules_menu():



    Button('Options', 50, 100, 200, 50, green, bright_green)
    Button('Rules', 50, 200, 200, 50, blue, bright_blue)
    Button('Control', 50, 300, 200, 50, orange, bright_orange)
    Button('Back', 50, 400, 200, 50, red, bright_red)

    pygame.display.update()

def main_menu():
    intro = True #om gewoon voor te zorgen dat hij meteen naar de while loop moet gaan en uitvoeren
    while intro:
        for event in pygame.event.get(): #functies uivoeren
            if event.type == pygame.QUIT: #zodat je met de kruisje altijd kan afsluiten
                pygame.quit()
                quit()


        #if state = 0
        #  draw screen 1
        #    if btn in screen 1 is pressed change to state 2
        #if state = 2
        #  draw screen 2

        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects('Rotterdam Toren', largeText) #hier word eindelijk de naam van de pagina weergegeven
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        if state == 0:
            Button('Start', 50, 100, 200, 50, green, bright_green)
            Button('Rules', 50, 200, 200, 50, blue, bright_blue, rules_menu)
            Button('Score', 50, 300, 200, 50, orange, bright_orange)
            Button("Quit", 50, 400, 200, 50, red, bright_red, quitgame) #def quitButton(message=quit, x=50, y=400, breedte=200, hoogte=50, inactive=rood, active=licht rood, action=quitgame)
            Button("Lambda test ", 50, 500, 200, 50, red, bright_red, stateblah)
        elif state == 1:
            Button('Hoi', 50, 100, 200, 50, green, bright_green)

        pygame.display.flip()
        clock.tick(60)


main_menu() #de verschillende def's uivoeren
quitgame()
pygame.quit()
quit()