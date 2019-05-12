from gamelogic.rngsus import RNGsus
from gamelogic.bubblesort import BubbleSort

class GameState():

    def __init__(self, word = ""):
        self.__word = word
        self.__state = word
        self.__sorter = BubbleSort(self.__word)
        self.__curr_state = 0
        self.__state_progress = dict()
        self.__init_state_progress()

    def __init_state_progress(self):
        self.__state_progress[0] = True
        for i in range(1, self.__sorter.max_state + 1, 1):
            self.__state_progress[i] = False

    def _debug(self):
        print(self.__dict__)

    def check_state(self):
        curr_state = self.__sorter.match_state(self.__state)
        if curr_state > self.__curr_state:
            self.__curr_state = curr_state
            self.__state_progress[curr_state] = True

    def get_current_state_id(self):
        return self.__curr_state

    def get_starting_word(self):
        return self.__word

    @staticmethod
    def initialize():
        return GameState(
            word=RNGsus.get_word()
        )