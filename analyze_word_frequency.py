from collections import Counter
import string



def histogram():
    punctuations = '''!()-;:'"\,,<>./?@#$%^&*_~'''
    with open("bible.txt") as f:
        wordList = f.read().split()
        # for word in wordList:
        #     no_punct = ""
        #     for char in word:
        #         if char not in punctuations:
        #             no_punct = no_punct + char
        #             word = no_punct
        wordcount = Counter(wordList)
    return dict(wordcount)


if __name__ == '__main__':
    words = histogram()
    print(words)
