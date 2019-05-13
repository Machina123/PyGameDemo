import os

RESOLUTION = (1920, 1080)
WINDOW_TITLE = "Projekt zaliczeniowy"
TICKRATE = 30
ALPHABET = "ABCDEFGHJKNOPRSXZ"
LETTER_WIDTH = 100
LETTER_BEGIN_X = 535
LETTER_BEGIN_Y = 182
BUTTON_LEFT_POS = (550, 325)
BUTTON_RIGHT_POS = (700, 325)
BUTTON_SWAP_POS = (850, 325)

def get_path(relative_path = ""):
    return os.path.join(os.getcwd(), relative_path)
