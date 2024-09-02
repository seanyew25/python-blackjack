class Player():
    def __init__(self, cards):
        self.cards = cards

    def addCard(self, card):
        self.cards.append(card)

    def calculateValue(self):
        score = 0
        for card in self.cards:
            score += card.value
        return score
