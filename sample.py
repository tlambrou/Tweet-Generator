import random
import analyze_word_frequency
import sys


def random_shuffle(count):
    # Creates a random number between 1 and the total number of tokens
    rand_index = random.randint(1, count)
    return rand_index


def create_list(histogram):
    listogram = []
    for key, value in histogram.iteritems():
        pair = [key,value]
        listogram.append(pair)
    return listogram


def random_sample(listogram):
    sumToRand = 0
    random = random_shuffle(len(listogram) + 1)
    for word in listogram:
        if sumToRand >= random:
            return word[0]
        else:
            sumToRand += word[1]

if __name__ == '__main__':
    source = sys.argv[1]
    histogram = analyze_word_frequency.histogram(source)
    listogram = create_list(histogram)
    print(random_sample(listogram))
