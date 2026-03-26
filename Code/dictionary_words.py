import sys
import random

DICTIONARY_FILE = "/usr/share/dict/words"

def load_words(file_path):
    """Load all words from the dictionary file into a list."""
    with open(file_path, "r") as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def generate_sentence(words_list, num_words):
    """Return a string with num_words randomly selected words."""
    if num_words > len(words_list):
        raise ValueError("Requested more words than are available in the dictionary.")
    selected = random.sample(words_list, num_words)
    return " ".join(selected) + "."

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)

    try:
        num_words = int(sys.argv[1])
        if num_words <= 0:
            raise ValueError
    except ValueError:
        print("Please provide a positive integer for the number of words.")
        sys.exit(1)

    all_words = load_words(DICTIONARY_FILE)

    sentence = generate_sentence(all_words, num_words)
    print(sentence)