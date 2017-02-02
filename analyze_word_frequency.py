from collections import Counter
import string


def histogram(source):
    with open(source) as f:
        dictionary = {}
        wordList = f.read().split()
        for word in wordList:
            word = re.sub('[.,:]', '', word)
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary


def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return 0

if __name__ == '__main__':
    source = "bible.txt"
    histogram = histogram(source)
    print(histogram)
    print(unique_words(histogram))
    print(frequency("death", histogram))
