class Card:
    # can define a class attribute here
    card_type = "playing cards"
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        
