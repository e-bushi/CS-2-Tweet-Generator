import sys
import random

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
                word += character.lower()
            else:
                if word == "":
                    continue
                else:
                    word_array.append(word)
                    word = ""
                    continue

    return(word_array)

def dictionary(array):
    histogram = {}
    array_duplicate = array

    for word in array_duplicate:
        histogram[word] = array.count(word)

    return(histogram)


def list_of_lists(array):
    "To Do: Add a familiarity array that logs every word once to prevent repetition"
    listogram = []
    array_duplicate = array

    for word in array_duplicate:
        word_count = array.count(word)

        if [word_count, word] not in listogram:
            listogram.append([word_count, word])
        else:
            continue

    return sorted(listogram)

def list_of_tuples(array):
    tuplegram = []
    array_duplicate = array

    for word in array_duplicate:
        word_count = array.count(word)

        if tuple([word_count, word]) not in tuplegram:
            tuplegram.append(tuple([word_count, word]))
        else:
            continue

    return tuplegram


def token_total(gram):
    token_tot = 0

    '''histogram'''
    # histogram = gram
    # for word in histogram:
    #     token_tot += histogram[word]
    '''listgram'''
    listogram = gram
    for word in listogram:
        token_tot += word[0]

    '''tuplegram'''
    # tuplegram = gram
    # for a_tuple in tuplegram:
    #     for count, word in a_tuple:
    #             token_tot += count

    return token_tot


def probability_token(total, gram):
    """histogram"""
    # histogram = gram
    # proba_dict = {}
    # for word in histogram:
    #     proba_dict[word] = histogram[word] / total

    """listogram"""
    listogram = gram
    proba_list = []
    for word in listogram:
        proba_list.append([word[0] / total, word[1]])

    proba_range = []
    for index in range(0, len(proba_list)):
        if index == 0:
            proba_range.append(proba_list[index])
        elif index == len(proba_list) - 1:
            proba_range.append([round(proba_range[index-1][0]+proba_list[index][0], 2), proba_list[index][1]])
        else:
            proba_range.append([proba_range[index-1][0]+proba_list[index][0], proba_list[index][1]])

    """tuplegram"""
    # proba_list_of_tuples = []
    # for word in histogram:
    #     proba_list_of_tuples.append(tuple([word, histogram[word] / total]))

    return(proba_range)

def generate_word(list_):
    random_number = random.uniform(0, 1)

    for word in list_:
        if random_number < word[0]:
            return [word[1], word[0]]
        else:
            continue

def generate_sentence(number_of_words, list_):
    sentence = ""
    for _ in range(0, number_of_words):
        word = generate_word(list_)

        sentence += "{} =>> {}\n".format(word[0], word[1])

    return sentence

if __name__ == '__main__':
    fileToRead = sys.argv[1:]
    data = histogram(fileToRead[0])
    array = unique_words(data)
    # histogram = dictionary(array)
    listogram = list_of_lists(array)
    # tuplegram = list_of_tuples(array)
    # print(listogram)
    total_tokens = token_total(listogram)
    probability_dictionary = probability_token(total_tokens, listogram)
    sentence = generate_sentence(10, probability_dictionary)
    print(sentence)
