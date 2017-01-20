##Random import voor dice
import random, pygame, time

pygame.init()

display_width = 500
display_hight = 400
gameDisplay = pygame.display.set_mode((display_width, display_hight))

font = pygame.font.SysFont(None, 30)
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Dobbelsteen worp")

white = (255,255,255)

#Plaatjes die de dobbelsteen getal laten zien
OneFace = pygame.image.load("images/1.png")
TwoFace = pygame.image.load("images/2.png")
ThreeFace = pygame.image.load("images/3.png")
FourFace = pygame.image.load("images/4.png")
FiveFace = pygame.image.load("images/5.png")
SixFace = pygame.image.load("images/6.png")
AllDice = pygame.image.load("images/6dicecubes.png")


# message hoe hij er uit moet zien en waar
def messages_to_screen(msg, color, lokatie1, lokatie2):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_hight / lokatie1, display_width / lokatie2])

##als width weer 800 is en height 600 1,74, 3.5
messages_to_screen("Dit is jouw dobbelsteen worp.... ", white, 4, 2.5) # 5, 5
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
        return window.blit(OneFace, (190, 250))
    elif diceCurrentImage == 2:
        return window.blit(TwoFace, (190, 250))
    elif diceCurrentImage == 3:
        return window.blit(ThreeFace, (190, 250))
    elif diceCurrentImage == 4:
        return window.blit(FourFace, (190, 250))
    elif diceCurrentImage == 5:
        return window.blit(FiveFace, (190, 250))
    elif diceCurrentImage == 6:
        return window.blit(SixFace, (190, 250))
    else:
        return window.blit(AllDice, (190, 250))


diceCurrentImage = dicecurrentimage()

pygame.display.flip()

pygame.time.wait(6000)

pygame.quit()
