import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

BALL_SIZE = 5
FRAME_RATE = 40
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Ping Pong Game"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    ball = Actor()
    ball.set_text("@")
    ball.set_font_size(FONT_SIZE)
    ball.set_color(WHITE)
    ball.set_position(Point(MAX_X // 2, MAX_Y // 2))
    ball.set_velocity(Point(1, 1))
    cast.add_actor("ball", ball)
    
    
    # create the robot
       
    # make the paddles
    y = MAX_Y // 2
    for i in range(5):
        paddle = Actor()
        x = CELL_SIZE
        y = y + (15)
        position = Point(x, y)
        paddle.set_text("|")
        paddle.set_font_size(FONT_SIZE)
        paddle.set_color(WHITE)
        paddle.set_font_size(FONT_SIZE)
        paddle.set_position(position)
        cast.add_actor("paddle1", paddle)
        
        
    y = MAX_Y // 2
    for i in range(5):
        paddle = Actor()
        x = MAX_X - CELL_SIZE
        y = y + (15)
        position = Point(x, y)
        paddle.set_text("|")
        paddle.set_font_size(FONT_SIZE)
        paddle.set_color(WHITE)
        paddle.set_font_size(FONT_SIZE)
        paddle.set_position(position)
        cast.add_actor("paddle2", paddle)
        
    
    
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
