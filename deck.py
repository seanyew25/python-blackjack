from card import Card
import random
import copy

class Deck():

    def __init__ (self, cards):
        self.cards = cards
        
    def addToDeck(self, card):
        self.cards.append(card)

    def randomCard(self):
        deckSize = len(self.cards)
        cardToDraw = random.randint(0, deckSize -1)
        return self.cards.pop(cardToDraw)
    

