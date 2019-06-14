import os
import pygame
import sys

from gamelogic import constants
from gamelogic.gamestate import GameState
from gamelogic.gui import GUI

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                action = gui.check_click(event.pos)
                if action == constants.BUTTON_LEFT_ACTION:
                    gamestate.move_frame("l")
                    gui.move_frame(gamestate.get_frame_pos())
                elif action == constants.BUTTON_RIGHT_ACTION:
                    gamestate.move_frame("r")
                    gui.move_frame(gamestate.get_frame_pos())
                elif action == constants.BUTTON_SWAP_ACTION:
                    gamestate.swap()
                    gui.swap_letters(gamestate.get_frame_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            gui.redraw_buttons_not_clicked()
        elif event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)


def game_loop():
    if gui is not None:
        gui.draw(screen)
        gui.update_swaps_left_text(gamestate.get_moves_left())


prepare_game()
# main loop
while (True):
    event_handler()
    game_loop()
    if gamestate.is_finished():
        if gamestate.is_successfully_finished():
            gui.draw_win_screen()
        else:
            gui.draw_lose_screen()
    clock.tick(constants.TICKRATE)
