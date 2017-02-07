from flask import Flask
app = Flask(__name__)
import sample

@app.route('/')
def hello_world():
    source = "sample.txt"
    histogram = sample.analyze_word_frequency.histogram(source)
    listogram = sample.create_list(histogram)
    output = str(histogram) + " \n\n"
    for i in range(1, 10):
        output += sample.random_sample(listogram) + " "
    return output

if __name__ == '__main__':
    app.run()
