import sys
import random
from collections import defaultdict, Counter

DICTIONARY_FILE = "/usr/share/dict/words"

def load_words(file_path):

    with open(file_path, "r") as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def signature(word):
    return "".join(sorted(word))

def build_anagram_index(words):
    index = defaultdict(list)

    for word in words:
        index[signature(word)].append(word)

    return index

def can_form(word, letter_counts):
    wc = Counter(word)
    for ch, count in wc.items():
        if letter_counts[ch] < count:
            return False
    return True

def generate_sentence(words_list, num_words):

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