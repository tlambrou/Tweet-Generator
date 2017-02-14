from flask import Flask
app = Flask(__name__)
import sample

@app.route('/')
def hello_world(): #11
    source = "bible.txt"
    histogram = sample.analyze_word_frequency.histogram(source)
    listogram = sample.create_list(histogram)
    length = 0
    for word in listogram:
        length += word[1]
    output = str(histogram) + " \n\n"
    for i in range(1, 10):
        output += sample.random_sample(listogram) + " "
    output += "  This is the length: " + str(length)
    return output

if __name__ == '__main__':
    app.run()
