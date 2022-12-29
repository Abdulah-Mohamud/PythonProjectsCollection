import random


# Card class to represent individual cards
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def __repr__(self):
        # Return a string representation of the card
        return f"{self.value} of {self.suit}"


# Deck class to represent the deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        # Create a deck of 52 cards
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.cards)

    def deal(self):
        # Deal a card from the top of the deck
        return self.cards.pop()


# Blackjack class to handle gameplay
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.dealer_hand = []

    def start_game(self):
        # Deal the initial hands to the player and dealer
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())

    def player_turn(self):
        # Allow the player to hit or stand
        while True:
            choice = input("Do you want to hit or stand? (h/s) ")
            if choice == "h":
                self.player_hand.append(self.deck.deal())
                if self.get_hand_value(self.player_hand) > 21:
                    print("You bust!")
                    return
            elif choice == "s":
                return
            else:
                print("Invalid choice. Please try again.")

    def dealer_turn(self):
        # Dealer hits on 16 and stands on 17
        while self.get_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.deal())

    def get_hand_value(self, hand):
        # Calculate the value of a hand, taking into account
        # that aces can be worth 1 or 11 points
        value = 0
        num_aces = 0
        for card in hand:
            if card.value in ["J", "Q", "K"]:
                value += 10
            elif card.value == "A":
                value += 11
                num_aces += 1
            else:
                value += int(card.value)