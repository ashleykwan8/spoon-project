from random import random, shuffle


class Card():
    def __init__(self, name, value, suit):
        self.value = value
        self.suit = suit
        self.name = name

    def __repr__(self):
        return f"card value {self.value} card suit {self.suit} card name {self.name}"


class Deck(list):
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
        values = {"Two": 2,
                  "Three": 3,
                  "Four": 4,
                  "Five": 5,
                  "Six": 6,
                  "Seven": 7,
                  "Eight": 8,
                  "Nine": 9,
                  "Ten": 10,
                  "Jack": 11,
                  "Queen": 12,
                  "King": 13,
                  "Ace": 14}
        for name in values:
            for suit in suits:
                self.cards.append(Card(name, values[name], suit))

    def __repr__(self):
        return f"Deck of cards: {self.cards}"

    def shuffle(self, times=1):
        random.shuffle(self.cards)
        print("Deck Shuffled")

    def deal(self):
        return self.cards.pop(0)
