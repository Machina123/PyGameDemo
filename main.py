from gamelogic import constants
from gamelogic.gamestate import GameState
from gamelogic.gui import GUI
import pygame, os, sys

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# enable double buffering and hardware acceleration for better performance
flags = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.HWACCEL

# macOS specific - fullscreen gives *significantly* better performance
if sys.platform.lower().startswith("darwin"):
    flags |= pygame.FULLSCREEN

screen = pygame.display.set_mode(constants.RESOLUTION, flags=flags)
pygame.display.set_caption(constants.WINDOW_TITLE)
clock = pygame.time.Clock()

gamestate = GameState.initialize()
gui = GUI(gamestate.get_starting_word())

def prepare_game():
    gui._debug()
    gamestate._debug()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)

def game_loop():
    if gui is not None:
        gui.draw(screen)

prepare_game()
# main loop
while(True):
    event_handler()
    game_loop()
    clock.tick(constants.TICKRATE)
