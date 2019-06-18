from gamelogic import constants
from gamelogic.bubblesort import BubbleSort
from gamelogic.rngsus import RNGsus


class GameState():

    def __init__(self, word=""):
        self.__word = word
        self.__state = word
        self.__sorter = BubbleSort(self.__word)
        self.__curr_state = 0
        self.__frame_pos = 0
        self.__finished = False
        self.__finish_success = False

    def _debug(self):
        print(self.__dict__)

    def check_state(self):
        self.__curr_state += 1
        print(f"{self.__curr_state}/{self.__sorter.max_state}")
        if self.__curr_state >= self.__sorter.max_state:
            if self.__state == self.__sorter.sorted:
                print("wygrana")
                self.__finish_success = True
            else:
                print("nie udało się")
                self.__finish_success = False
            self.__finished = True

    def get_moves_left(self):
        return self.__sorter.max_state - self.__curr_state

    def set_state(self, newstate):
        self.__state = newstate
        self.check_state()

    def get_starting_word(self):
        return self.__word

    def move_frame(self, direction: str):
        if direction == constants.MOVE_LEFT_ACTION:
            if self.__frame_pos - 1 < 0:
                return
            else:
                self.__frame_pos -= 1
        elif direction == constants.MOVE_RIGHT_ACTION:
            if self.__frame_pos + 2 >= len(self.__word):
                return
            else:
                self.__frame_pos += 1

    def get_frame_pos(self):
        return self.__frame_pos

    def swap(self):
        word = list(self.__state)
        word[self.__frame_pos], word[self.__frame_pos + 1] = word[self.__frame_pos + 1], word[self.__frame_pos]
        self.set_state(''.join(word))

    def is_finished(self):
        return self.__finished

    def is_successfully_finished(self):
        return self.__finish_success

    @staticmethod
    def initialize():
        return GameState(word=RNGsus.get_word_unique())
