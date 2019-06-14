from gamelogic.rngsus import RNGsus
from gamelogic.bubblesort import BubbleSort
from gamelogic import constants

class GameState():

    def __init__(self, word = ""):
        self.__word = word
        self.__state = word
        self.__sorter = BubbleSort(self.__word)
        self.__curr_state = 0
        self.__state_progress = dict()
        self.__tickcount = 0
        self.__init_state_progress()
        self.__frame_pos = 0

    def __init_state_progress(self):
        self.__state_progress[0] = True
        for i in range(1, self.__sorter.max_state + 1, 1):
            self.__state_progress[i] = False

    def _debug(self):
        print(self.__dict__)

    def check_state(self):
        curr_state = self.__sorter.match_state(self.__state)
        print(curr_state)
        if curr_state > self.__curr_state:
            self.__curr_state = curr_state
            self.__state_progress[curr_state] = True

    def set_state(self, newstate):
        self.__state = newstate
        self.check_state()

    def get_current_state_id(self):
        return self.__curr_state

    def get_starting_word(self):
        return self.__word

    def tick(self):
        self.__tickcount += 1

    def move_frame(self, direction:str):
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

    @staticmethod
    def initialize():
        return GameState(
            word=RNGsus.get_word_unique()
        )