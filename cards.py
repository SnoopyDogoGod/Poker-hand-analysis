import numpy as np

class Hand:
    colorCharTable=("\u2665", #coeur
                    "\u2666", #carreau
                    "\u2660", #pique
                    "\u2663") #trefle
    valCharTable=("2","3","4","5","6","7","8","9","10","V","D","R","A")
                    
    def __init__(self, *args):
        if len(args)%2!=0 and len(args)>7:
            raise Exception("Nombre d'arguments incorrects")
        self.cards=np.zeros((7,17))
        for i, (cardVal, cardColor) in enumerate(zip(args[::2], args[1::2])):
            self.cards[i][cardVal]=1
            self.cards[i][13+cardColor]=1
        
        self.handSize=int(len(args)/2)


        pass


    def __str__(self):
        finalString=""
        for i in range(7):
            val=np.where(self.cards[i]==1)[0]
            if val.size!=0:
                print(val)
                finalString+="{}{} ".format(Hand.valCharTable[val[0]],Hand.colorCharTable[13-val[1]])
            else:
              finalString+="\u25A7 "  
        return finalString
        
    
    

a=Hand(0,1,2,2,12,3)

print(a)
