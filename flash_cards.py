import random
import sys
import linecache


def get_word():
    filename = "/usr/share/dict/words"
    rand_index = random.randint(1, 235886)
    word = linecache.getline(filename, rand_index, module_globals=None)
    word = word.rstrip()
    return word + " "


if __name__ == '__main__':
    count = int(sys.argv[1])
    sentence = ""
    for i in range(count):
        sentence += get_word()
    print(sentence)
    
# with open('file.txt', 'r') as searchfile:
#     for line in searchfile:
#         if 'searchphrase' in line:
#             print line
