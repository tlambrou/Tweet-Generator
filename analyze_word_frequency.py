from collections import Counter
import string



def histogram(source):
    with open(source) as f:
        wordList = f.read().split()
        # punctuations = '''!()-;:'"\,,<>./?@#$%^&*_~'''
        # for word in wordList:
            # exclude = set(string.punctuation)
            # word = ''.join(ch for ch in word if ch not in exclude)
        #     no_punct = ""
        #     for char in word:
        #         if char not in punctuations:
        #             no_punct = no_punct + char
        #             word = no_punct
        dictionary = {}
        for word in wordList:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
        # wordcount = Counter(wordList)
    return dictionary


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
    print(histogram)
    print(unique_words(histogram))
    print(frequency("death", histogram))
