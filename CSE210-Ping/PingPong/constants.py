import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Ping Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "PingPong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "PingPong/assets/sounds/boing.wav"
WELCOME_SOUND = "PingPong/assets/sounds/start.wav"
OVER_SOUND = "PingPong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
LEFT2 = "a"
RIGHT2 = "d"


# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "PingPong/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_SCORE = 0
MAXIMUM_SCORE = 5

# HUD
HUD_MARGIN = 15
PLAYER1_GROUP = "player1score"
PLAYER2_GROUP = "player2score"
SCORE_GROUP = "score"
PLAYER1_FORMAT = "PLAYER 1 SCORE: {}"
PLAYER2_FORMAT = "PLAYER 2 SCORE: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "PingPong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 5

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"PingPong/assets/images/{n:03}.png" for n in range(50, 53)]
print(RACKET_IMAGES)
RACKET_WIDTH = 300
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 7

# RACKET2
RACKET2_GROUP = "rackets2"
RACKET2_IMAGES = [f"PingPong/assets/images/{n:03}.png" for n in range(60, 63)]
print(RACKET2_IMAGES)
RACKET2_WIDTH = 300
RACKET2_HEIGHT = 28
RACKET2_RATE = 6
RACKET2_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = f"PRESS ENTER TO START\nFIRST TO REACH {MAXIMUM_SCORE} POINTS IS THE WINNER!"
PREP_TO_LAUNCH = "PREPARING TO PLAY"
WAS_GOOD_GAME = "GAME OVER, CONGRATS TO THE WINNER"