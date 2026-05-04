import random

def build_markov_chain(words):
    chain = {}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in chain:
            chain[current_word] = []
        
        chain[current_word].append(next_word)
    
    return chain

def markov_sample(chain, start_word, length=10):
    sentence = [start_word]
    current_word = start_word

    for _ in range(length - 1):
        if current_word not in chain:
            break

        next_words = chain[current_word]
        current_word = random.choice(next_words)
        sentence.append(current_word)

    return " ".join(sentence)

if __name__ == "__main__":
    corpus = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
    words = corpus.split()

    chain = build_markov_chain(words)

    start_word = random.choice(words)

    print(markov_sample(chain, start_word, 15))