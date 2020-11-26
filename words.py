def print_upper_words(words, start_with):
    for word in words:
        if word[0] in start_with:
            print(word.upper())


print_upper_words(['hello', 'hey', 'yo', 'goodbye', 'yes'], ['h', 'y'])