import random

class Card:


    def __init__(self):

        self.card_value = 0

    def possible_value(self):
        range_value = random.randrange(1, 14, 1)
        
        self.card_value = range_value

        return self.card_value

card = Card()
print(card.possible_value())

