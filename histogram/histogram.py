import sys

def histogram(source_text):
    list_of_words = []
    with open(source_text, 'r') as phile:
        data = list(phile.readlines())

    return data

def unique_words(data):
    ascii_numbers = [int(n) for n in range(32, 65)]
    punctuation_and_numbers = [chr(n) for n in ascii_numbers]

    more_ascii_numbers = [int(n) for n in range(91, 97)]
    more_puncts = [chr(n) for n in more_ascii_numbers]

    last_set_of_ascii = [int(n) for n in range(123, 127)]
    last_puncts = [chr(n) for n in last_set_of_ascii]

    frequency = 0
    word = ""
    word_array = []
    for line_array in data:

        for character in line_array:
            if character not in punctuation_and_numbers and character is not "\n" and character is not "\t" and character not in more_puncts and character not in last_puncts:
                word += character
            else:
                if word == "":
                    continue
                else:
                    word_array.append(word)
                    word = ""
                    continue

    return(word_array)

def word_frequency(array):
    word_dictionary = {}
    array_duplicate = array

    for word in array_duplicate:
        word_dictionary[word] = array.count(word)

    return(word_dictionary)


def word_frequency_arr(array):
    "To Do: Add a familiarity array that logs every word once to prevent repetition"
    words_arr = []
    array_duplicate = array

    for word in array_duplicate:
        word_count = array.count(word)

        if [word_count, word] not in words_arr:
            words_arr.append([word_count, word])
        else:
            continue

    return words_arr

def word_frequency_tuple(array):
    words_arr = []
    array_duplicate = array

    for word in array_duplicate:
        word_count = array.count(word)

        if tuple([word_count, word]) not in words_arr:
            words_arr.append(tuple([word_count, word]))
        else:
            continue

    return words_arr


if __name__ == '__main__':
    fileToRead = sys.argv[1:]
    data = histogram(fileToRead[0])
    array = unique_words(data)
    # dictionary = word_frequency(array)
    new_array = word_frequency_tuple(array)
    print(new_array)
