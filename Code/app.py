"""Main script, uses other modules to generate sentences."""
from flask import Flask
import dictionary_words

app = Flask(__name__)

words_file = "/usr/share/dict/words"
word_list = dictionary_words.load_words(words_file)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = dictionary_words.generate_sentence(word_list, 7)
    return f"<h1>{sentence}</h1>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)