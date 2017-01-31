import random
import sys

def random_shuffle():
    rand_index = random.randint(1, len(sys.argv) - 1)
    return sys.argv[rand_index]

if __name__ == '__main__':
    print(random_shuffle())
