from game.player import PLAYER
from game.card import Card
class director():
    
    global score
    def __init__(self):
        global score
        beginning_score = 300
        score = beginning_score

    def comparision(self, val1, val2, guess):
        global score
        if (val1<val2 and guess == "h" or val1>val2 and not guess == "l"):
            score = score + 100
            return score
        else:
            score = score - 75
            return score
    
    def display(self):
        val1 = Card.possible_value()
        val2 = Card.possible_value()
        print(f"The card is {val1}")
        hilo = PLAYER.choose_hilo()
        director.comparision(val1, val2, hilo)
        print(f"The next card was {val2}")
        print(f"Your score is: {score}")
        return PLAYER.play_again()
        
        
    