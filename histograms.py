#!python

from __future__ import division, print_function
import cleanup

class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            item = cleanup.clean(item)
            self.tokens += 1
            if item not in self:
                self[item] = 1
                self.types += 1
            else:
                self[item] += 1


    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if item in self:
            if self[item] > 0:
                return self[item]
        else:
            return 0

class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            item = cleanup.clean(item)
            self.tokens += 1
            if len(self) > 0:
                contained = False
                for word in self:
                    if word[0] == item:
                        tup = (word[0], word[1] + 1)
                        self.remove(word)
                        self.append(tup)
                        contained = True
                        break
                if contained == False:
                    word = (item, 1)
                    self.append(word)
                    self.types += 1
            elif len(self) == 0:
                word = (item, 1)
                self.append(word)
                self.types += 1


    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        for word in self:
            if word[0] == item:
                return word[1]
        return 0


    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        for word in self:
            if word[0] == item:
                return True
        return False

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        for count, item in self:
            if item[0] == target:
                return (target, count)
        return None


def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)

    hist_list = Listogram(text_list)
    print('listogram:', hist_list)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
