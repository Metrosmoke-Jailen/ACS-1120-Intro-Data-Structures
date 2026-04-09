import sys
import re
from collections import Counter

def histogram(source_text):
    try:
        with open(source_text, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        text = source_text

    words = re.findall(r'\b\w+\b', text.lower())
    hist = Counter(words)
    return hist

def unique_words(hist):
 return len(hist)

def frequency(word, hist):
 return hist.get(word.lower(), 0)

def most_frequent(hist, length=10):
 return hist.most_common(length)

def least_frequent(hist, length=10):
 return sorted(hist.items(), key=lambda item: item[1])[:length]

if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 histogram.py <filename>")
            sys.exit(1)

        filename = sys.argv[1]
        hist = histogram(filename)

        print(f"Total unique words: {unique_words(hist)}")
        print(f"Most frequent words: {most_frequent(hist)}")
        print(f"Least frequent words: {least_frequent(hist)}")

        word_to_check = "the"
        print(f"Frequency of '{word_to_check}': {frequency(word_to_check, hist)}")