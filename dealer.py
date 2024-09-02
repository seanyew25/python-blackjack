from player import Player

class Dealer(Player):
    # def __init__ (self, cards):
    #     self.cards = cards


    def deal(self, deck, players):
        self.cards.append(deck.randomCard())
        self.cards.append(deck.randomCard())       
        for player in players:
            for x in range(2):
                player.addCard(deck.randomCard())


    def hit(deck, player):
        player.addCard(deck.randomCard())

    def action(self, deck):
        if self.calculateValue() < 18:
            self.cards.append(deck.randomCard())
            return "hit"
        
        else:
            return "stand"




        



    

