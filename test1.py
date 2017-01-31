import random

class questions():  # vragen op het scheerm


    def __init__(self, questions, answer1, answer2, answer3, correct):
        self.questions = questions
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct = correct



a = questions(["waar woont Haroon"], ["A : Dordrecht"], ["B : den haag"], ["C : rotterdam"], "a")
b = questions(["waar woont jawed"], ["A : rotterdam"], ["B : Rijswijk"], ["C : rotterdam"], "b")
c = questions(["waar woont pietje"], ["A : rotterdam"], ["B : Delft"], ["C : rotterdam"], "c")
d = questions(["waar woont Anie"], ["A : Zoetermeer"], ["B : Delft"], ["C : rotterdam"], "d")
e = questions(["waar woont Milad"], ["A : rotterdam"], ["B : Delft"], ["C : Delft"], "e")

l = [a,b,c,d,e]
random_selection = random.randint(0, len(l) - 1)
print (l[random_selection].questions[0],l[random_selection].answer1,l[random_selection].answer2)


"""
for myChar in range(l):
    randomNum = random.randint(97, 101)
    myChar = chr(randomNum)
"""


#print (myChar)





