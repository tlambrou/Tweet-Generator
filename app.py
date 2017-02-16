from flask import Flask
app = Flask(__name__)

import sys
import histograms
import cleanup
import tokenize
import word_count
import sample
import sentence
import random

@app.route('/')
def hello_world(): #11
    filename = "bible.txt"
    sentence_length = random.randint(9, 29)
    word_list = histograms.read_from_file(filename)
    listogram = histograms.Listogram(word_list)
    output = sentence.generate_random_sentence(listogram, sentence_length)
    return output

if __name__ == '__main__':
    arguments = sys.argv[1:]
    sentence_length = random.randint(9, 29)
    filename = ""
    if len(arguments) == 0:
        filename = "fish.txt"
    elif len(arguments) == 1:
        filename = arguments[0]
    else:
        filename = arguments[0]
        sentence_length = arguments[1]
    word_list = histograms.read_from_file(filename)
    listogram = histograms.Listogram(word_list)
    output = sentence.generate_random_sentence(listogram, sentence_length)
    print(output)
    app.run()

# histogram = sample.analyze_word_frequency.histogram(source)
# listogram = sample.create_list(histogram)
# length = 0
# for word in listogram:
#     length += word[1]
# output = str(histogram) + " \n\n"
# for i in range(1, 10):
#     output += sample.random_sample(listogram) + " "
# output += "  This is the length: " + str(length)
