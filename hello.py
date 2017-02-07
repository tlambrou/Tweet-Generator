from flask import Flask
app = Flask(__name__)
import sample

@app.route('/')
def hello_world():
    source = "bible.txt"
    listogram = sample.create_list(sample.analyze_word_frequency.histogram(source))
    output = ""
    for i in range(1, 35):
        output += sample.random_sample(listogram) + " "
    return output
