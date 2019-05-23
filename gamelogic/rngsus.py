from gamelogic import constants
import random

class RNGsus():

    @staticmethod
    def get_word(length=10):
        selected_letters = []
        for i in range(length):
            letter = constants.ALPHABET[random.randrange(len(constants.ALPHABET))]
            selected_letters.append(letter)
        return ''.join(selected_letters)

    @staticmethod
    def get_word_unique(length=10):
        selected_letters = []
        for i in range(length):
            letter = constants.ALPHABET[random.randrange(len(constants.ALPHABET))]
            while letter in selected_letters:
                letter = constants.ALPHABET[random.randrange(len(constants.ALPHABET))]
            selected_letters.append(letter)
        return ''.join(selected_letters)