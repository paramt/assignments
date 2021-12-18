from random import randrange
from Domino import Domino, generate_deck


class GameBoard:
    def __init__(self):
        self.deck = generate_deck()
        self.domino = ""

    # Removes a random domino from the deck and returns it
    def draw_domino(self):
        return self.deck.pop(randrange(len(self.deck)))

    # Places domino on the board and returns true if it is playable
    # Otherwise doesn't do anything and returns false
    def place_domino(self, domino):
        if not self.domino:
            self.domino = domino
            return True
        elif self.domino.split("|")[0] == domino.split("|")[0] or self.domino.split("|")[0] == domino.split("|")[1] or self.domino.split("|")[1] == domino.split("|")[1]:
            self.domino = domino
            return True
        else:
            return False

    # Returns a list of dominos of a specified size
    # Removes those dominos from the deck as well
    def deal_hand(self, size: int):
        hand = []
        while len(hand) < size:
            hand.append(self.draw_domino())

        return hand
