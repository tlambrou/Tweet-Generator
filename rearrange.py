import random
import sys


def random_shuffle():
    rand_index = random.randint(1, len(sys.argv) - 1)
    return sys.argv[rand_index]

# def create_array():
#     for i in sys.argv:

if __name__ == '__main__':

    for i in range(1, len(sys.argv)):
        random_word = random_shuffle()
        print(random_word + " ")

    # for i in sys.argv:
    #     print(i)
