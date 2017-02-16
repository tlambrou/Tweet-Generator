# Module for generating a sample word from a histogram
import random
import analyze_word_frequency
import sys


def random_shuffle(count): #2
    # Creates a random number between 1 and the total number of tokens
    rand_index = random.randint(1, count)
    return rand_index


def create_list(histogram): #5
    listogram = []
    for key, value in histogram.iteritems():
        pair = [key,value]
        listogram.append(pair)
    return listogram


def random_sample(listogram): #10
    sumToRand = 0
    random = random_shuffle(listogram.tokens)
    for index, word in enumerate(listogram):
        sumToRand += word[1]
        if sumToRand >= random:
            return word[0]

if __name__ == '__main__':  #11
    source = sys.argv[1]
    histogram = analyze_word_frequency.histogram(source)
    listogram = create_list(histogram)
    length = 0
    for word in listogram:
        length += word[1]
    output = str(histogram) + " \n\n"
    for i in range(1, 10):
        output += random_sample(listogram) + " "
    output += "  This is the length: " + str(length)
    print(output)
