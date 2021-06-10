import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        brick = cast["brick"]
        for brick in brick:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text("")
        """ ball.set_text("")
        for brick in brick:
            if paddle.get_position().equals(brick.get_position()):
                description = brick.get_description()
                ball.set_text(description) """