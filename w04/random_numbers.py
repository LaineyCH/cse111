"""
creates a list of numbers, appends more numbers onto the list, and prints the list.
"""
import random


def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)

    words = []
    append_random_words(words, 6)
    print(words)


def append_random_numbers(number_list, quantity = 1):
    for i in range(quantity):
        random_number = round((random.uniform(1, 100)), 1)
        number_list.append(random_number)


def append_random_words(words_list, quanity = 1):
    random_words_list = ["family", "love", "house", "car", "kids", "dog", "cat",\
                          "fish", "bicycle", "album", "picture", "temple"]
    for i in range(quanity):
        #get random word from above list
        word = random.choice(random_words_list)
        #find index of selected word
        index = random_words_list.index(word)
        #remove word from list to avoid duplicates
        random_words_list.pop(index)
        # add the selected word to the word list passed in
        words_list.append(word)


if __name__ == "__main__":
    main()