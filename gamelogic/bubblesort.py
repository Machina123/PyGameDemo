class BubbleSort():

    def __init__(self, word = ""):
        self.word = list(word)
        self.states = dict()
        self.states[0] = ''.join(self.word)
        self.max_state = len(word) - 1
        self.prepare_states()

    def prepare_states(self):
        curr_state = 1
        for i in range(len(self.word) - 1):
            for j in range(i+1, len(self.word), 1):
                if self.word[i] > self.word[j]:
                    self.word[i], self.word[j] = self.word[j], self.word[i]
            self.states[curr_state] = ''.join(self.word)
            curr_state += 1

    def match_state(self, needle = ""):
        for k, v in self.states.items():
            if needle == v:
                return k
        return -1