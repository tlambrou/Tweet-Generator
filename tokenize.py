# Module for creating lists of tokens from a text

from histograms import Dictogram
import histograms

def dict_o_listo(word_list):
    dictionary = {}
    for word in word_list:
        if word not in dictionary:
            dictionary[word] = Dictogram(iterable=None)
    for i in range(0, len(word_list) - 2):
        first = word_list[i]
        second = word_list[i + 1]
        dictionary[first].update([second])
    dictionary[word_list[-1]] = {word_list[0], 1}
    return dictionary

def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()

if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    filename = arguments[0]
    text_list = read_from_file(filename)
    dictodicto = dict_o_listo(text_list)
    print(dictodicto)
    # if len(arguments) == 0:
    #     # test hisogram on letters in a word
    #     word = 'abracadabra'
    #     test_histogram(word)
    #     print()
    #     # test hisogram on words in a sentence
    #     sentence = 'one fish two fish red fish blue fish'
    #     word_list = sentence.split()
    #     test_histogram(word_list)
    # elif len(arguments) == 1:
    #     # test hisogram on text from a file
    #     filename = arguments[0]
    #     text_list = read_from_file(filename)
    #     dictodicto = dict_o_listo(text_list)
    #     print(dictodicto)
    # else:
    #     # test hisogram on given arguments
    #     test_histogram(arguments)
