from random import randrange
from Deque import Deque


class GameBoard:
    def __init__(self):
        self.deck = self._generate_deck()
        self.dominos = Deque()

    # Removes a random domino from the deck and returns it
    def draw_domino(self):
        return self.deck.pop(randrange(len(self.deck)))

    # Places domino on the board and returns true if it is playable
    # Otherwise doesn't do anything and returns false
    def place_domino(self, domino):
        if self.dominos.is_empty():
            self.dominos.add_front(domino)

        elif self.dominos.get(0).split("|")[0] == domino.split("|")[1]:
            self.dominos.add_rear(domino)

        elif self.dominos.get(-1).split("|")[1] == domino.split("|")[0]:
            self.dominos.add_front(domino)

        elif self.dominos.get(0).split("|")[0] == domino.split("|")[0]:
            self.dominos.add_rear(self._flip_domino(domino))

        elif self.dominos.get(-1).split("|")[1] == domino.split("|")[1]:
            self.dominos.add_front(self._flip_domino(domino))

        else:
            return False

        return True

    # Returns a list of dominos of a specified size
    # Removes those dominos from the deck as well
    def deal_hand(self, size: int):
        hand = []
        while len(hand) < size:
            hand.append(self.draw_domino())

        return hand

    def __str__(self):
        return self.dominos.pprint()

    def _flip_domino(self, domino):
        return domino.split("|")[1] + "|" + domino.split("|")[0]

    def _generate_deck(self):
        output = []
        counter = 0

        for i in range(12, -1, -1):
            second_dice = 12 - counter

            for j in range(counter+1):
                dice = str(second_dice) + '|' + str(i)
                output.append(dice)
                second_dice += 1
            counter += 1

        return output
