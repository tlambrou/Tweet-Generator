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

def generate_order1_sentence(dictodicto, word_count):
    sentence = ""

    # Pick a random word
    key = random.sample(dictodicto, 1)
    key = key[0]
    # Generate random word from its histogram
    print("Key value: ", key)
    #
    for i in range(0, word_count):
        dictogram = dictodicto[key]
        print(dictogram)
        word = str(sample.random_sample_dicto(dictogram))
        sentence += word
        key = word

        if i < word_count - 1: #Create spaces
            sentence += " "
        else:
            sentence += "." # Finishing period
    return sentence.capitalize()
