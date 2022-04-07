from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        #Move the first paddle
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - RACKET_WIDTH):
            position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
            
        body.set_position(position)
        
        #Move the second paddle
        racket2 = cast.get_first_actor(RACKET2_GROUP)
        body2 = racket2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        x = position2.get_x()
        
        position2 = position2.add(velocity2)

        if x < 0:
            position2 = Point(0, position2.get_y())
        elif x > (SCREEN_WIDTH - RACKET2_WIDTH):
            position2 = Point(SCREEN_WIDTH - RACKET2_WIDTH, position2.get_y())
            
        body2.set_position(position2)