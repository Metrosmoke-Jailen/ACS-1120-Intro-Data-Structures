import sys
import random

def rearrange_words(words):
    """Return a new list with the words shuffled."""
    shuffled = words[:]  # copy to avoid modifying original
    random.shuffle(shuffled)
    return shuffled

if __name__ == '__main__':
    # Grab all command-line arguments after the script name
    args = sys.argv[1:]
    
    if not args:
        print("Usage: python3 rearrange.py word1 word2 word3 ...")
    else:
        shuffled = rearrange_words(args)
        print(" ".join(shuffled))