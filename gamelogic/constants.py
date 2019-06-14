import os, pygame

RESOLUTION = (1920,1080)
WINDOW_TITLE = "Projekt zaliczeniowy"
TICKRATE = 30
ALPHABET = "ABCDEFGHJKNOPRSXZ"

LETTER_WIDTH = 100
LETTER_BEGIN_X = 535
LETTER_BEGIN_Y = 182

BUTTON_LEFT_POS = (550, 325)
BUTTON_RIGHT_POS = (700, 325)
BUTTON_SWAP_POS = (850, 325)
TEXT_MOVES_LEFT_POS = (1050, 360)

BUTTON_LEFT_ACTION = "left"
BUTTON_RIGHT_ACTION = "right"
BUTTON_SWAP_ACTION = "swap"

MOVE_LEFT_ACTION = "l"
MOVE_RIGHT_ACTION = "r"

COLOR_BLACK = pygame.color.Color("#000000")
COLOR_WHITE = pygame.color.Color("#ffffff")
COLOR_GREEN = pygame.color.Color("#00ff00")
COLOR_RED = pygame.color.Color("#ff0000")

TEXT_MOVES_LEFT = "Pozostało zamian:"

TEXT_WIN = "Wygrana!"
TEXT_WIN_SUB = "Udało Ci się otworzyć skrzynię!"

TEXT_LOSE = "Przegrana!"
TEXT_LOSE_SUB = "Nie udało Ci się otworzyć skrzyni w odpowiedniej ilości ruchów!"

TEXT_QUIT_HINT = "Aby wyjść, naciścij ESCAPE"

def get_path(relative_path = ""):
    return os.path.join(os.getcwd(), relative_path)
