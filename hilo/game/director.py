from game.player import PLAYER
from game.card import Card
cards = Card()
player = PLAYER()

class director():
    
    global score
    def __init__(self):
        global score
        beginning_score = 300
        score = beginning_score

    def comparision(self, card1, card2, guess):
        global score
        if (card1<card2 and guess == "h" or card1>card2 and not guess == "l"):
            score = score + 100
            return score
        else:
            score = score - 75
            return score
    
    def display(self):
        val1 = cards.possible_value()
        val2 = cards.possible_value()
        print(f"The card is {val1}")
        hilo = player.choose_hilo()
        self.comparision(val1, val2, hilo)
        print(f"The next card was {val2}")
        print(f"Your score is: {score}")
        return player.play_again()
        
        
    