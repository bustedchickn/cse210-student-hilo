class director():
    global score
    def __init__(self):
        global score
        beginning_score = 300
        score = beginning_score

    def comparision(val1, val2, guess):
        global score
        if (val1<val2 and guess or val1>val2 and not guess):
            score = score + 100
            return score
        else:
            score = score - 75
            return score
    
    def display(val1, val2):
        print(f"The card is {val1}")
        input("Is the next card higher or lower?   [h/l]")#input function here
        print(f"The next card was {val2}")
        #keep playing stuff
        
    