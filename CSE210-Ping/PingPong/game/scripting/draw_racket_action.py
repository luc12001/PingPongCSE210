from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        #Draws the first paddle
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()

        if racket.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = racket.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        #Draws the second paddle
        racket2 = cast.get_first_actor(RACKET2_GROUP)
        body2 = racket2.get_body()

        if racket2.is_debug():
            rectangle2 = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle2, PURPLE)
            
        animation2 = racket2.get_animation()
        image2 = animation2.next_image()
        position2 = body2.get_position()
        self._video_service.draw_image(image2, position2)