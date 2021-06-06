# Import all the libs we need for the game
from game import Game

# Instantiate the various classes we will need to run the game
main = Game()

# Start running the game in a main control loop
main.start()
while not main.completed:
    main.guess()
