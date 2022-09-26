import random

# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.

class Card:
    """A pack of cards with the numbers 1 to 13.

    The responsibility of Game is to keep track of the guess picked and calculate the scores for 
    it.
   
    Attributes:
        card (int): The value of card randomly picked facing up.
        scores (int): The number of points the guess is worth.
    """
    def __init__(self):
        self.value = random.randint(1,13)
        self.next_card = 0
