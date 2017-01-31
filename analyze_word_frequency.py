from collections import Counter
import string



def histogram(source):
    # punctuations = '''!()-;:'"\,,<>./?@#$%^&*_~'''
    with open(source) as f:
        wordList = f.read().split()
        # for word in wordList:
        #     no_punct = ""
        #     for char in word:
        #         if char not in punctuations:
        #             no_punct = no_punct + char
        #             word = no_punct
        wordcount = Counter(wordList)
    return dict(wordcount)


def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return "Word not in text."

if __name__ == '__main__':
    source = "bible.txt"
    histogram = histogram(source)
    print(unique_words(histogram))
    print(frequency("Lord", histogram))
