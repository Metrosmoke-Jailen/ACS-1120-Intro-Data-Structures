import re
from collections import Counter
import sys

def histogram(source_text):
    """
    Build a histogram (word frequency dictionary) from source_text.
    source_text can be a filename (str) or the text itself.
    """
    try:
        with open(source_text, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        text = source_text

    words = re.findall(r'\b\w+\b', text.lower())

    hist = Counter(words)
    return hist

def unique_words(hist):
    """Return the number of unique words in the histogram."""
    return len(hist)

def frequency(word, hist):
    """Return the number of times 'word' appears in the histogram."""
    return hist.get(word.lower(), 0)

def most_frequent(hist, n=10):
    """Return the n most common words."""
    return hist.most_common(n)

def least_frequent(hist, n=10):
    """Return the n least common words."""
    # Sort by frequency ascending
    return sorted(hist.items(), key=lambda x: x[1])[:n]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 word_frequency.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    hist = histogram(filename)

    print(f"Total unique words: {unique_words(hist)}")
    print(f"Most frequent words: {most_frequent(hist)}")
    print(f"Least frequent words: {least_frequent(hist)}")
    
    word_to_check = "the"
    print(f"Frequency of '{word_to_check}': {frequency(word_to_check, hist)}")