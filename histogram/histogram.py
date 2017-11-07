import sys
import random
import string
import time

def read_file(source_text):
    # returns a string
    list_of_words = []
    with open(source_text, 'r') as phile:
        data = list(phile.readlines())

    return data

def just_words(data):
    # takes in a string and returns a list of unique words
    word = ""
    word_array = []
    for line_array in data:

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

    return(word_array)

def histogram(array):
    histogram = {}
    array_duplicate = array

    for word in array_duplicate:
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

    return sorted(listogram)

def get_index_of_item(item, list_of_lists):
    # iterate through the listogram
    i = 0
    for list_pair in list_of_lists:
        # if we reach the item, return its index
        if list_pair[1] == item:
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

    start = time.time()
    data = read_file(fileToRead[0])
    print(time.time() - start)

    start = time.time()
    array = just_words(data)
    print(time.time() - start)
    # histogram = dictionary(array)
    start = time.time()
    listogram = list_of_lists(array)
    print(time.time() - start)
    # tuplegram = list_of_tuples(array)
    # print(listogram)
    start = time.time()
    total_tokens = token_total(listogram)
    print(time.time() - start)

    start = time.time()
    probability_dictionary = probability_token(total_tokens, listogram)
    print(time.time() - start)

    start = time.time()
    sentence = generate_sentence(10, probability_dictionary)
    print(time.time() - start)
    print(sentence)
