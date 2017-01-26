import random
import sys


def random_shuffle():
    rand_index = random.randint(0, len(sys.argv) - 1)
    return sys.argv[rand_index]

if __name__ == '__main__':
    for i in range(len(sys.argv) - 1):
        random_word = random_shuffle()
        print random_word + str(" ")
