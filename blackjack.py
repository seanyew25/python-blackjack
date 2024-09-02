from card import Card
from deck import Deck
from player import Player
from dealer import Dealer

# card = Card("Diamonds", "King", 12)
suits = ['Spades', 'Diamonds','Clubs', 'Hearts']
deck = Deck([])
for suit in suits:
    for x in range(1, 15):
        if x < 11:
            card = Card(suit, x, x)
        elif x == 11:
            card = Card(suit, 'Jack', 10)
        elif x == 12:
            card = Card(suit, 'Queen', 10)
        elif x == 13:
            card = Card(suit, 'King', 10)
        else:
            card = Card(suit, 'Ace', 11)

        deck.addToDeck(card)



print("Welcome to Very Simplified Blackjack! First to 21 wins!")
# name = input("What is your name? ")
player = Player([])
dealer = Dealer([])
dealer.deal(deck, [player])
print("You have", end="")
for card in player.cards:
    print(f" {card.rank} of {card.suit},", end="")

action = input("\nWhat do you want to do next? (hit or stand)")
dealerAction = dealer.action(deck)

while action == "hit" or dealerAction == "hit":
    if dealerAction == "hit":
        dealer.addCard(deck.randomCard())
        print("Dealer drew a card")
    
    else:
        print("Dealer choose to stand")

    if action == "hit":
        player.addCard(deck.randomCard())
        print("You received a card")
        print("Now, you have", end="")
        for card in player.cards:
            print(f" {card.rank} of {card.suit},", end="")

    action = input("\nWhat do you want to do next? (hit or stand)")
    dealerAction = dealer.action(deck)

playerTotal = player.calculateValue()
dealerTotal = dealer.calculateValue()

if playerTotal > 21 and dealerTotal > 21:
    print ("ALL BUSTED.")

else: 
    if playerTotal > 21:
        print("YOU BUSTED.")

    if dealerTotal > 21:
        print("DEALER BUSTED.")

    if (dealerTotal < 21 and (21 - dealerTotal  < 21 - playerTotal)):
        print(f"Dealer wins. He got {dealerTotal}. You got {playerTotal}.")

    else:
        print(f"You win. He got {dealerTotal}. You got {playerTotal}.")









# print(deck.cards)

# for card in deck.cards:
#     print((card.suit, card.rank, card.value))

# card_dealt = deck.dealCard()
# print((card_dealt.suit, card_dealt.rank, card_dealt.value))
# print(deck.dealCard())