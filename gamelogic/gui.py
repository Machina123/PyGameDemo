from gamelogic import constants
import pygame, os

class GUI():

    def __init__(self, word = ""):
        self._letter_sprites = []
        self._backboard = Backboard()
        self._frame = Frame()
        self._button_left = ButtonLeft()
        self._button_right = ButtonRight()
        self._button_swap = ButtonSwap()
        self._winscreen = WinScreen()
        self._losescreen = LoseScreen()
        self._winscreen_visible = False
        self._losescreen_visible = False
        self._text_swaps_left = None
        self._generate(word)

    def _set_letter_positions(self):
        i = 0
        for letter in self._letter_sprites:
            letter._set_pos(constants.LETTER_BEGIN_X + i * constants.LETTER_WIDTH, constants.LETTER_BEGIN_Y)
            i += 1

    def draw(self, surface):
        self._backboard.draw(surface)
        self._set_letter_positions()
        for letter in self._letter_sprites:
            letter.draw(surface)
        self._frame.draw(surface)
        self._button_left.draw(surface)
        self._button_right.draw(surface)
        self._button_swap.draw(surface)
        if self._winscreen_visible:
            self._winscreen.draw(surface)
        elif self._losescreen_visible:
            self._losescreen.draw(surface)
        if self._text_swaps_left is not None:
            text_rect = self._text_swaps_left.get_rect()
            text_rect.topleft = constants.TEXT_MOVES_LEFT_POS
            surface.blit(self._text_swaps_left, text_rect)
        pygame.display.flip()

    def report_letter_state(self):
        return ''.join([c.get_char() for c in self._letter_sprites])

    def _generate(self, word = ""):
        for c in list(word):
            self._letter_sprites.append(Letter(c))

    def _debug(self):
        print(self.__dict__)

    @staticmethod
    def load_image(path = ""):
        return pygame.image.load(constants.get_path(path))

    def move_frame(self, idx):
        self._frame.set_pos(constants.LETTER_BEGIN_X + idx * constants.LETTER_WIDTH, constants.LETTER_BEGIN_Y)

    def swap_letters(self, idx):
        self._letter_sprites[idx], self._letter_sprites[idx + 1] = self._letter_sprites[idx + 1], self._letter_sprites[idx]

    def check_click(self, pos):
        x, y = pos
        if self._button_left.clicked(x,y):
            self._button_left.redraw_clicked()
            return constants.BUTTON_LEFT_ACTION
        if self._button_right.clicked(x,y):
            self._button_right.redraw_clicked()
            return constants.BUTTON_RIGHT_ACTION
        if self._button_swap.clicked(x,y):
            self._button_swap.redraw_clicked()
            return constants.BUTTON_SWAP_ACTION

    def redraw_buttons_not_clicked(self):
        self._button_swap.redraw_not_clicked()
        self._button_right.redraw_not_clicked()
        self._button_left.redraw_not_clicked()

    def draw_win_screen(self):
        self._winscreen_visible = True

    def draw_lose_screen(self):
        self._losescreen_visible = True

    def update_swaps_left_text(self, swaps_left):
        self._text_swaps_left = Text.get_text(constants.TEXT_MOVES_LEFT + " " + str(swaps_left), "Arial", 48)

class Letter(pygame.sprite.Sprite):
    def __init__(self, char=""):
        super().__init__()
        self.image = GUI.load_image('assets/letter_' + char + ".png")
        self.rect = self.image.get_rect()
        self.__char = char
        pass

    def get_char(self):
        return self.__char

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Backboard(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = GUI.load_image("assets/chest.png")
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Frame(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = GUI.load_image("assets/frame.png")
        self.rect = self.image.get_rect()
        self.rect.x = constants.LETTER_BEGIN_X
        self.rect.y = constants.LETTER_BEGIN_Y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, clicked_image_path, initial_pos = None):
        super().__init__()
        self._img_path = image_path
        self._clicked_img_path = clicked_image_path
        self.image = GUI.load_image(self._img_path)
        self.rect = self.image.get_rect()
        if initial_pos is not None:
            self.initial_pos = initial_pos
            self.set_pos(initial_pos[0], initial_pos[1])
        else:
            self.initial_pos = (0,0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def clicked(self, event_x, event_y):
        return self.rect.collidepoint(event_x, event_y)

    def redraw_clicked(self):
        self.image = GUI.load_image(self._clicked_img_path)
        self.rect = self.image.get_rect()
        x, y = self.initial_pos
        self.set_pos(x-20, y-20)

    def redraw_not_clicked(self):
        self.image = GUI.load_image(self._img_path)
        self.rect = self.image.get_rect()
        x, y = self.initial_pos
        self.set_pos(x, y)

class ButtonLeft(Button):

    def __init__(self):
        super().__init__("assets/button_L.png", "assets/button_L_light.png", constants.BUTTON_LEFT_POS)

class ButtonRight(Button):

    def __init__(self):
        super().__init__("assets/button_R.png", "assets/button_R_light.png", constants.BUTTON_RIGHT_POS)

class ButtonSwap(Button):

    def __init__(self):
        super().__init__("assets/button_O.png","assets/button_O_light.png", constants.BUTTON_SWAP_POS)

class Text:

    @staticmethod
    def get_text(text, font_name, font_size, colour = constants.COLOR_BLACK, bold = False, italic = False) -> pygame.Surface:
        pygame.font.init()
        font_obj = pygame.font.SysFont(font_name, font_size, bold=bold, italic=italic)
        return font_obj.render(text, True, colour)

class WinScreen(pygame.Surface):

    def __init__(self):
        self.text1 = Text.get_text(constants.TEXT_WIN, "arial", 48, colour=constants.COLOR_GREEN, bold=True)
        self.text1_rect = self.text1.get_rect()
        self.text2 = Text.get_text(constants.TEXT_WIN_SUB, "arial", 36, colour=constants.COLOR_WHITE)
        self.text2_rect = self.text2.get_rect()
        self.text3 = Text.get_text(constants.TEXT_QUIT_HINT, "Arial", 36, colour=constants.COLOR_WHITE)
        self.text3_rect = self.text3.get_rect()
        self.text1_rect.center = (960, 360)
        self.text2_rect.center = (960, 480)
        self.text3_rect.center = (960, 800)

    def draw(self, surface):
        surface.fill(constants.COLOR_BLACK)
        surface.blit(self.text1, self.text1_rect)
        surface.blit(self.text2, self.text2_rect)
        surface.blit(self.text3, self.text3_rect)

class LoseScreen(pygame.Surface):

    def __init__(self):
        self.text1 = Text.get_text(constants.TEXT_LOSE, "arial", 48, colour=constants.COLOR_RED, bold=True)
        self.text1_rect = self.text1.get_rect()
        self.text2 = Text.get_text(constants.TEXT_LOSE_SUB, "arial", 36, colour=constants.COLOR_WHITE)
        self.text2_rect = self.text2.get_rect()
        self.text3 = Text.get_text(constants.TEXT_QUIT_HINT, "Arial", 36, colour=constants.COLOR_WHITE)
        self.text3_rect = self.text3.get_rect()
        self.text1_rect.center = (960, 360)
        self.text2_rect.center = (960, 480)
        self.text3_rect.center = (960, 800)

    def draw(self, surface):
        surface.fill(constants.COLOR_BLACK)
        surface.blit(self.text1, self.text1_rect)
        surface.blit(self.text2, self.text2_rect)
        surface.blit(self.text3, self.text3_rect)