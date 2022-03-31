class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        velocity = self._keyboard_service.get_direction() 
        paddle = cast.get_actors("paddle1")
        for segment in paddle:
            segment.set_velocity(velocity)    
            
        paddle = cast.get_actors("paddle2")
        for segment in paddle:
            segment.set_velocity(velocity)    

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        paddle = cast.get_actors("paddle1")
        paddle2 = cast.get_actors("paddle2")
        ball = cast.get_first_actor("ball")
        
        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        ball.move_next(max_x, max_y)
        
        for segment in paddle:
            segment.move_next(max_x, max_y)
            
            
            #x = segment.get_position().get_x()
            #y = segment.get_position().get_y()
            #if x - BALL_SIZE >= ball.get_position().get_x() and x + 10 <= ball.get_position().get_x() and y - 10 >= ball.get_position().get_y() and y + 10 <= ball.get_position().get_y():
           #     ball.get_velocity().reverse()
            
                 
                
            
        for segment in paddle2:
            segment.move_next(max_x, max_y)
            
        
        
        
            
   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()