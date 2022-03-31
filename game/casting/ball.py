import random
from random import randint
from constants import *
from game.casting.actor import Actor 

class Ball(Actor):
    """An  object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Ball.
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super.__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the ball in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
            """Gets the ball's image.
            
            Returns:
                An instance of Image.
            """
            return self._image
    
    def release(self):
        """Release the ball in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BALL_VELOCITY * rn, BALL_VELOCITY * rn])
        vy = -BALL_VELOCITY
        velocity = vx, vy
        self._body.set_velocity(velocity)


# This is an idea I had, this should reflect the ball in the way
# it should, just not sure how to get it added
#
#     self.velocity = [randint(4,8),randint(-8,8)]  
#
#     def update(self):
#         self.x += self.velocity[0]
#         self.y += self.velocity[1]
#       
#     def bounce(self):
#         self.velocity[0] = -self.velocity[0]
#         self.velocity[1] = randint(-8,8)