# Module for generating a sentence from a histogram

import sample
import random

def generate_random_sentence(listogram, word_count):
    sentence = ""
    for i in range(0, word_count):
        sentence += str(sample.random_sample(listogram))
        if i < word_count - 1:
            sentence += " "
        else:
            sentence += "."
    return sentence.capitalize()
