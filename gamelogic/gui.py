from gamelogic import constants
import pygame, os

class GUI():

    def __init__(self, word = ""):
        self._letter_sprites = []
        self._backboard = None
        self._frame = None
        self._button_left = None
        self._button_right = None
        self._button_swap = None
        self._generate(word)

    def _set_letter_positions(self):
        i = 0
        for letter in self._letter_sprites:
            letter._set_pos(constants.LETTER_BEGIN_X + i * constants.LETTER_WIDTH, constants.LETTER_BEGIN_Y)
            i += 1

    def draw(self, surface):
        surface.fill(pygame.color.THECOLORS['lightblue'])
        self._set_letter_positions()
        for letter in self._letter_sprites:
            letter.draw(surface)
        # self._frame.draw(surface)
        # self._backboard.draw(surface)
        # self._button_left.draw(surface)
        # self._button_right.draw(surface)
        # self._button_swap.draw(surface)
        pygame.display.flip()

    def report_letter_state(self):
        return ''.join([c.get_char() for c in self._letter_sprites])

    def _generate(self, word = ""):
        for c in list(word):
            self._letter_sprites.append(Letter(c))

    def _debug(self):
        print(self.__dict__)


class Letter(pygame.sprite.Sprite):
    def __init__(self, char=""):
        super().__init__()
        self.image = pygame.image.load(os.path.join(os.getcwd(), 'assets/letter_' + char + ".png"))
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