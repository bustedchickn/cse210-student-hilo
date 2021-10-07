# TODO: Add entry point code here
import random
from game.director import director
game_director = director()
#main gameplay loop
continuing = True
while (continuing):
    continuing = game_director.display()