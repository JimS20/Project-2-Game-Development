import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width, display_hight))
pygame.display.set_caption('Quiz')

font = pygame.font.SysFont(None, 30)


class questions():  # vragen op het scheerm
    def __init__(self, questions, answer1, answer2, answer3, correct):
        self.questions = questions
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct = correct


a = questions(["waar woont Haroon"], ["A : Dordrecht"], ["B : den haag"], ["C : rotterdam"], [pygame.K_a])
b = questions(["waar woont jawed"], ["A : rotterdam"], ["B : Rijswijk"], ["C : rotterdam"], [pygame.K_c])
c = questions(["waar woont pietje"], ["A : rotterdam"], ["B : Delft"], ["C : rotterdam"], [pygame.K_b])
d = questions(["waar woont Anie"], ["A : Zoetermeer"], ["B : Delft"], ["C : rotterdam"], [pygame.K_c])
e = questions(["waar woont Milad"], ["A : rotterdam"], ["B : Delft"], ["C : Delft"], [pygame.K_b])

l = [a,b,c,d,e]
random_selection = random.randint(0, len(l) - 1)
print(l[random_selection].questions)




def messages_to_screen(msg, color, lokatie1, lokatie2):  # massage hoe hij er uit moet zien en waar
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_hight / lokatie1, display_width / lokatie2])


def gameLoop():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
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
                        print("Goed")
                    else:
                        print ("fout")
                if event.key == pygame.K_b:
                    if pygame.K_b == l[random_selection].correct[0]:
                            print("goed")
                    else:
                            print("fout")
                if event.key == pygame.K_c:
                    if pygame.K_c == l[random_selection].correct[0]:
                            print("goed")
                    else:
                            print("fout")
                if event.key == pygame.K_q:
                        gameExit = True


gameLoop()

