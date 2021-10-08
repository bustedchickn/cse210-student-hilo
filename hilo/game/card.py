import random

class Card:


    def __init__(self):

        self.card_value = 0
#only logical values are between 1 and 13
    def possible_value(self):
        range_value = random.randrange(1, 14, 1)
        
        self.card_value = range_value

        return self.card_value



