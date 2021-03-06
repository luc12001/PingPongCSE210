from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._p1score = DEFAULT_SCORE
        self._p2score = DEFAULT_SCORE
        #self._score = 0

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_SCORE:
            self._lives += 1 

    def add_points(self):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        if self._p1score < MAXIMUM_SCORE:
            self._p1score += 1

        
    def add_points2(self):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        if self._p2score < MAXIMUM_SCORE:
            self._p2score += 1


    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._p1score

    def get_score2(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._p2score

    def get_winner(self):

        if self._p1score > self._p2score:
            WINNER = "PLAYER 1 (BLUE) HAS WON THE GAME!"
        elif self._p1score < self._p2score:
            WINNER = "PLAYER 2 (GREEN) HAS WON THE GAME!"
        return WINNER

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1
    
    def next_level(self):
        """Adds one level."""
        if self._level < MAXIMUM_SCORE:
            self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = DEFAULT_SCORE
        self._lives = DEFAULT_SCORE
        #self._score = 0