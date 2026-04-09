import sys
import random
from histogram import histogram

def sample_random(hist):
    words = list(hist.keys())
    return random.choice(words)

def sample_weighted(hist):
    words = list(hist.keys())
    weights = list(hist.values())
    return random.choices(words, weights=weights, k=1)[0]

if __name__ == "__main__":
    if len(sys.argv) <2:
        print("Usage: python3 stochastic_sampling.py <text_or_file>")
    sys.exit(1)

    input_data = sys.argv[1]

    hist = histogram(input_data)

    print("Pure random sample:", sample_random(hist))
    print("Weighted sample:", sample_weighted())
