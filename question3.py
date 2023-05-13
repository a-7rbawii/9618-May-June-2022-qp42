class Card:
    def __init__(self, num, clr):
        self.__Number = num
        self.__Colour = clr
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

def ChooseCard():
    global TakenCards
    flagContinue = True
    while flagContinue == True:
        choice = int(input("Choose you card, 1-30: "))
        if choice < 1 or choice > 30:
            print("Number must be between 1 to 30")
        elif TakenCards[choice - 1] == True:
            print("Card already taken")
        else:
            print("Valid")
            flagContinue = False
    TakenCards[choice - 1] = True
    return (choice-1)

cardList = [Card(-1, None) for i in range(30)]
TakenCards = [False for i in range(30)]

try:
    filename = r"C:\Users\Abood\Desktop\School\Final Revision Files\Computer Science\Past paper python\P4 Papers\May June 2022 - 42\CardValues.txt"
    file = open(filename, "r")
    for i in range(30):
        num = int(file.readline())
        clr = file.readline().strip()
        cardList[i] = Card(num, clr)
    file.close
except IOError:
    print("File not found")

Player1 = []
for i in range(4):
    selectCard = ChooseCard()
    Player1.append(cardList[selectCard])
for i in range(4):
    print(Player1[i].GetNumber())
    print(Player1[i].GetColour())