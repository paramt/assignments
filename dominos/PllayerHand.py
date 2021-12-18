from Domino import Domino


class PlayerHand:
    def __init__(self, dominos=[]):
        self.hand = dominos

    def add_domino(self, domino):
        self.hand.append(domino)

    def remove_domino(self, domino):
        if domino in self.hand:
            return self.hand.remove(domino)
        else:
            return self.hand.remove(self._flip_domino(domino))

    def __str__(self):
        return ", ".join(self.hand)

    # Returns true if self.hand contains domino
    def contains(self, domino):
        return domino in self.hand or self._flip_domino(domino) in self.hand

    # Returns the highest double in a given hand
    # If no doubles exist, it returns the domino with the highest sum
    def get_highest_domino(self):
        highest_double = -1
        highest_sum = 0
        highest_non_double_domino = ""

        for domino in self.hand:
            side1 = int(domino.split("|")[0])
            side2 = int(domino.split("|")[1])
            domino_sum = side1 + side2

            if side1 == side2 and side1 > highest_double:
                highest_double = side1

            elif domino_sum > highest_sum:
                highest_sum = domino_sum
                highest_non_double_domino = domino

        if highest_double > -1:
            return f"{highest_double}|{highest_double}"
        else:
            return highest_non_double_domino

    def _flip_domino(self, domino):
        return domino.split("|")[1] + "|" + domino.split("|")[0]
