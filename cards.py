import numpy as np
from random import shuffle

COLORCHARTABLE=("\u2665", #coeur
                "\u2666", #carreau
                "\u2660", #pique
                "\u2663") #trefle
VALCHARTABLE=("2","3","4","5","6","7","8","9","10","V","D","R","A")

def card_val_to_string(card):
    return "{}{} ".format(VALCHARTABLE[card[0]],COLORCHARTABLE[card[1]])

def generate_deck():

    deck = [(i, j) for i in range(0, 13) for j in range(0, 4)]

    return deck

BASEDECK=generate_deck()


class Hand:

    def generate_hand(handSize,deck=None):
        if not deck:
            deck = BASEDECK.copy()
            shuffle(deck)
        cards = [deck.pop() for _ in range(handSize)]
        print("\n",cards,"\n")
        return Hand(*cards)

                    
    def __init__(self, *args):

        self.cards=np.zeros((7,17))
        for i, (cardVal, cardColor) in enumerate(args):
            self.cards[i][cardVal]=1
            self.cards[i][13+cardColor]=1
        
        self.handSize=len(args)



    def analyse(self):

        




    def __str__(self):
        finalString=""
        for i in range(7):
            val=np.where(self.cards[i]==1)[0]
            if val.size!=0:
                print(val)
                finalString+=card_val_to_string((val[0],13-val[1]))
            else:
              finalString+="\u25A7 "  
        return finalString








    
    

a=Hand.generate_hand(5)

print(a)

deck1=generate_deck()
