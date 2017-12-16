import sys
import random
import string
import time

def read_file(source_text):
    # returns a string
    with open(source_text, 'r') as phile:
        data = list(phile.readlines())
        # data = phile.read().split()
    return data

def just_words(data):
    # takes in a string and returns a list of unique words
    word_array = []
    for line_array in data:
        word = ""
        for character in line_array:
            if character in string.ascii_letters:
                word += character.lower()
            else:
                if word == "":
                    continue
                else:
                    word_array.append(word)
                    word = ""
                    continue

    # word_array = []
    # for a_word in data:
    #     word = ""
    #     for character in a_word:
    #         if character not in string.punctuation:
    #             word += character.lower()
    #     word_array.append(word)

    return(word_array)


def histogram_dict(array):
    '''Make histogram. '''

    histogram = {}

    for word in array:
        if word not in histogram:
            histogram[word] = array.count(word)

    return(histogram)


def list_of_lists(words):
    "To Do: Add a familiarity array that logs every word once to prevent repetition"
    listogram = []

    for word in words:
        if [1, word] not in listogram:
            listogram.append([1, word])
        else:
            listogram[get_index_of_item(word, listogram)][0] += 1

    return listogram

def get_index_of_item(item, list_of_lists):
    # iterate through the listogram
    i = 0
    for word in list_of_lists:
        # if we reach the item, return its index
        # if list_pair[1] == item:
        if word is item:
            return i
        else:
            i += 1

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
    histogram = gram
    for word in histogram:
        token_tot += histogram[word]
    '''listgram'''
    # listogram = gram
    # for word in listogram:
    #     token_tot += word[0]

    '''tuplegram'''
    # tuplegram = gram
    # for a_tuple in tuplegram:
    #     for count, word in a_tuple:
    #             token_tot += count

    return token_tot


def probability_token(total, gram):
    """histogram"""
    random_num = random.randint(0, total)
    histogram = gram
    for word in histogram:
        if random_num > histogram[word]:
            random_num - histogram[word]
        else:
            return word



    """listogram"""
    # listogram = gram
    # proba_list = []
    # for word in listogram:
    #     proba_list.append([word[0] / total, word[1]])
    #
    # proba_range = []
    # for index in range(0, len(proba_list)):
    #     if index == 0:
    #         proba_range.append(proba_list[index])
    #     elif index == len(proba_list) - 1:
    #         proba_range.append([round(proba_range[index-1][0]+proba_list[index][0], 2), proba_list[index][1]])
    #     else:
    #         proba_range.append([proba_range[index-1][0]+proba_list[index][0], proba_list[index][1]])

    """tuplegram"""
    # proba_list_of_tuples = []
    # for word in histogram:
    #     proba_list_of_tuples.append(tuple([word, histogram[word] / total]))

    return(raw_proba_dict)


def generate_word(total, gram):
    random_num = random.randint(0, total)

    for word in gram:
        if random_num > gram[word]:
            random_num -= gram[word]
        else:
            return word


def generate_sentence(number_of_words_to_generate, list_, total_tokens):
    sentence = ""
    for _ in range(0, number_of_words_to_generate):
        word = generate_word(total_tokens, list_)

        sentence += "{} ".format(word)

    return sentence


def main():

    start = time.time()
    data = read_file("military_service.txt")
    print(time.time() - start)

    start = time.time()
    array = just_words(data)
    print(time.time() - start)

    start = time.time()
    histo = histogram_dict(array)
    # listogram = list_of_lists(array)
    # tuplegram = list_of_tuples(array)
    print(time.time() - start)

    # print(listogram)
    # start = time.time()
    total_tokens = token_total(histo)
    # print(time.time() - start)
    #
    # start = time.time()
    # probability_dictionary = probability_token(total_tokens, histo)
    # print(time.time() - start)

    start = time.time()
    sentence = generate_sentence(50, histo, total_tokens)
    print(time.time() - start)
    print(sentence)


if __name__ == '__main__':
    main()
