class BubbleSort():

    def __init__(self, word=""):
        self.word = list(word)
        self.states = dict()
        self.states[0] = ''.join(self.word)
        self.max_state = 0
        self.sorted = None
        self.prepare_states()

    def prepare_states(self):
        self.experimental_sort()

    def experimental_sort(self):
        curr_state = 0
        for i in range(len(self.word) - 1):
            for j in range(len(self.word) - 1):
                if self.word[j] > self.word[j + 1]:
                    self.word[j], self.word[j + 1] = self.word[j + 1], self.word[j]
                    curr_state += 1

        self.max_state = curr_state
        self.sorted = ''.join(self.word)

    def standard_sort(self):
        curr_state = 0
        for i in range(len(self.word) - 1):
            for j in range(i + 1, len(self.word), 1):
                if self.word[i] > self.word[j]:
                    self.word[i], self.word[j] = self.word[j], self.word[i]
                    curr_state += 1
        self.max_state = curr_state
        self.sorted = ''.join(self.word)
