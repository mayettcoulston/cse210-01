from game.hilo import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Game]): A list of Game instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.score = 300
        self.user_guess = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        Ask the user if they want to play.
        
        Args:
            self (Director): an instance of Director.
        """
        replay= "y"

        while self.score>0 and replay=="y":
            card = self.get_inputs()
            self.do_updates(card)
            self.do_outputs()

            if self.score<=0:
                print("Game Over!")
            else:
                replay = input("Do you want to play again?(y/n): ")

    def get_inputs(self):
        """get the input from the user.

        Args:
            self (Director): An instance of Director.
        """
        current_card = Card()
        self.user_guess = input("Guess card? [h/l]: ")
        return current_card
       
    def do_updates(self, current_card):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        card = Card()
        print(f"This card is: {card.value}")
        if current_card.value > card.value and self.user_guess=="h":
            self.score -=75
        elif current_card.value < card.value and self.user_guess=="l":
            self.score -= 75
        else:
            self.score +=100

    def do_outputs(self):
        """Displays the score. 

        Args:
            self (Director): An instance of Director.
        """
        print("Your score is: {self.score}")
    