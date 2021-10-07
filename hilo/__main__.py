# TODO: Add entry point code here
import random
from game.director import director
#main gameplay loop
continuing = True
while (continuing):
    continuing = director.display(0)