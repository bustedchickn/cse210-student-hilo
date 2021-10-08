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
        
        if (card1<card2 and guess == "h"):
            score = score + 100
            return score
        elif(card2 < card1 and guess =="l"):
            score = score + 100
            return score

        else:
            score = score - 75
            return score


    def end_game(self,play_again, score):
        if play_again == True and score <= 0:
            print('sorry you have no more points, the game is over')
            play_again = False
        return play_again


    
    def display(self):
        val1 = cards.possible_value()
        val2 = cards.possible_value()
        if (val1 == val2):
            val2 = cards.possible_value()
        print(f"The card is {val1}")
        hilo = player.choose_hilo()
        self.comparision(val1, val2, hilo)
        print(f"The next card was {val2}")
        print(f"Your score is: {score}")
        play_again = player.play_again()
        #conditional end the game is the player has no more points
        if play_again == True and score <= 0:
            play_again = False
            print('sorry you have no more points, the game is over')
        

        
        return play_again

    


        
        
    