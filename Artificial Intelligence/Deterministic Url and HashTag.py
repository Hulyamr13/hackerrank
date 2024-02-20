import os

def load_dictionary():
    dictionary = set()
    with open("words.txt", "r") as f:
        for word in f:
            dictionary.add(word.strip().lower())
    return dictionary

def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def tokenize(input_string, dictionary):
    input_string = input_string.lower()
    tokens = []
    while input_string:
        found_word = False
        for i in range(len(input_string), 0, -1):
            if input_string[:i] in dictionary or is_number(input_string[:i]):
                tokens.append(input_string[:i])
                input_string = input_string[i:].lstrip()
                found_word = True
                break
        if not found_word:
            tokens.append(input_string[0])
            input_string = input_string[1:].lstrip()
    return tokens

def segment_input(input_string, dictionary):
    if input_string.startswith("#"):
        input_string = input_string[1:]  # Remove the hashtag
    elif input_string.startswith("www."):
        input_string = input_string[4:]  # Remove the "www."
    elif "." in input_string:
        input_string = input_string.split(".")[0]  # Remove the domain extension
    tokens = tokenize(input_string, dictionary)
    return " ".join(tokens)

if __name__ == "__main__":
    dictionary = load_dictionary()
    N = int(input())
    for _ in range(N):
        input_string = input()
        segmentation = segment_input(input_string, dictionary)
        print(segmentation)
