class Domino:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2


# Returns a deck of 91 dominos
def generate_deck():
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


# Returns the highest double in a given hand
# If no doubles exist, it returns the domino with the highest sum
def get_highest_domino(hand: list):
    highest_double = -1
    highest_sum = 0
    highest_non_double_domino = ""

    for domino in hand:
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
