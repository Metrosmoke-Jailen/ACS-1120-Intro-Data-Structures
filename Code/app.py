from flask import Flask, request, render_template
import random
import re

app = Flask(__name__)

def load_corpus(filepath):
    with open(filepath, "r") as file:
        text = file.read().lower()

    # Clean text but keep sentence endings
    text = re.sub(r'[^a-z0-9.!? ]+', '', text)
    words = text.split()
    return words

def build_markov_chain(words):
    chain = {}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in chain:
            chain[current_word] = {}

        if next_word not in chain[current_word]:
            chain[current_word][next_word] = 0

        chain[current_word][next_word] += 1

    return chain

def build_histogram(words):
    hist = {}

    for word in words:
        if word not in hist:
            hist[word] = 0
        hist[word] += 1

    return hist


def get_start_words(words):
    start_words = []

    for i in range(len(words) - 1):
        if words[i].endswith(('.', '!', '?')):
            start_words.append(words[i + 1])

    return start_words


def choose_start(start_words, words):
    if start_words:
        return random.choice(start_words)
    return random.choice(words)

def weighted_choice(word_dict):
    total = sum(word_dict.values())
    rand = random.randint(1, total)

    cumulative = 0
    for word, count in word_dict.items():
        cumulative += count
        if rand <= cumulative:
            return word

def generate_sentence(chain, start_word, length=20):
    sentence = [start_word]
    current_word = start_word

    for _ in range(length - 1):
        if current_word not in chain:
            break

        next_word = weighted_choice(chain[current_word])
        sentence.append(next_word)
        current_word = next_word

        # Stop naturally at sentence ending
        if current_word.endswith(('.', '!', '?')):
            break

    return " ".join(sentence).capitalize()


CORPUS_PATH = "data/corpus.txt"

words = load_corpus(CORPUS_PATH)
histogram = build_histogram(words)
chain = build_markov_chain(words)
start_words = get_start_words(words)

@app.route("/")
def home():
    # Get number of sentences from query (?num=3)
    try:
        num_sentences = int(request.args.get("num", 1))
    except ValueError:
        num_sentences = 1

    # Clamp to avoid abuse
    num_sentences = max(1, min(num_sentences, 10))

    sentences = []
    for _ in range(num_sentences):
        start = choose_start(start_words, words)
        sentence = generate_sentence(chain, start)
        sentences.append(sentence)

    return render_template("index.html", sentences=sentences)


# =========================
# ▶️ RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)