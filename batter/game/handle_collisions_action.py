import random
from game import constants
from game.action import Action
from game.point import Point

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
            if ball.get_position().equals(brick.get_position()) and brick.get_text() == "*":
                ball.set_velocity(Point(Point.get_x(ball.get_velocity()), Point.get_y(ball.get_velocity()) * -1))
            if ball.get_position().equals(brick.get_position()):
                brick.set_text("")
        if ((Point.get_x(ball.get_position()) >= Point.get_x(paddle.get_position()) and Point.get_x(ball.get_position()) <= Point.get_x(paddle.get_position()) + len(paddle.get_text())) and Point.get_y(ball.get_position()) == Point.get_y(paddle.get_position())):
            ball.set_velocity(Point(Point.get_x(ball.get_velocity()), -1))
        if Point.get_x(ball.get_position()) >= constants.MAX_X - 1 or Point.get_x(ball.get_position()) <= 1:
            ball.set_velocity(Point(Point.get_x(ball.get_velocity()) * -1, Point.get_y(ball.get_velocity())))
        if Point.get_y(ball.get_position()) <= 1:
            ball.set_velocity(Point(Point.get_x(ball.get_velocity()), Point.get_y(ball.get_velocity()) * -1))
        if Point.get_y(ball.get_position()) >= constants.MAX_Y - 1 and Point.get_y(ball.get_velocity()) == 1:
            return "End"
        """ ball.set_text("")
        for brick in brick:
            if paddle.get_position().equals(brick.get_position()):
                description = brick.get_description()
                ball.set_text(description) """