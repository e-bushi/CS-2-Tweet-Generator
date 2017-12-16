import sys
import random
import string
import histogram_one
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

    return(word_array)


# def first_dict_of_key_value_tuples(word_list):
#     word_dict = {}
#     for i in range(0, len(word_list) - 1):
#         first_word_in_tup = word_list[i]
#         if word_list[i+1] is None:
#             break
#         second_word_in_tup = word_list[i+1]
#
#         key_tuple = tuple([first_word_in_tup, second_word_in_tup])
#         if key_tuple in word_dict:
#             word_dict[key_tuple].append(word_list[get_index_of_item(second_word_in_tup, word_list) + 1])
#         else:
#             word_dict[key_tuple] = [word_list[get_index_of_item(second_word_in_tup, word_list) + 1]]
#
#     return word_dict

def tuple_array_dict(word_list):
    list_of_tuples = []
    word_dict = {}
    for i in range(0, len(word_list) - 1):
        list_of_tuples.append(tuple([word_list[i], word_list[i+1]]))

    for i in range(0, len(list_of_tuples) - 1):
        if list_of_tuples[i] in word_dict:
            word_dict[list_of_tuples[i]].append(list_of_tuples[i+1][1])
        else:
            word_dict[list_of_tuples[i]] = [list_of_tuples[i+1][1]]

    return word_dict


def histogram_of_histogram_value_counts(dict_):
    histogram_of_histogram_counts = {}

    for k, v in dict_.items():
        histogram_of_histogram_counts[k] = histogram_one.histogram_dict(v)

    return histogram_of_histogram_counts


def generate_a_word(key, parent_dict):
    nested_histogram = parent_dict[key]
    total_keys_n_histogram = histogram_one.token_total(nested_histogram)
    random_number = random.randint(0, total_keys_n_histogram)

    for word in nested_histogram:
        if random_number > nested_histogram[word]:
            random_number -= nested_histogram[word]
        else:
            return word


def generate_a_sentence(number_of_words, parent_dict):
    sentence = []
    list_of_keys = []

    for keys in parent_dict.keys():
        list_of_keys.append(keys)

    random_n = random.randint(0, len(list_of_keys) - 1)
    key_tuple_pair = list_of_keys[random_n]

    for _ in range(0, number_of_words):
        new_word = generate_a_word(key_tuple_pair, parent_dict)
        sentence.append(new_word)
        second_word_in_tup = key_tuple_pair[1]
        key_tuple_pair = tuple([second_word_in_tup, new_word])

    return ' '.join(sentence)


if __name__ == '__main__':
    # word_list = ["one", "fish", "two", "fish", "blue", "fish", "red", "fish"]
    # dictiona = first_dict_of_key_value_tuples(word_list)
    # histogram_of_histograms = histogram_of_histogram_value_counts(dictiona)
    # clear_sentence = generate_a_sentence(8, histogram_of_histograms)
    # print(clear_sentence)

    # file_argument = sys.argv[1:]
    start = time.time()
    data = read_file("corpus.txt")
    print(time.time() - start)

    start = time.time()
    array_of_words = just_words(data)
    print(time.time() - start)

    start = time.time()
    diction = tuple_array_dict(array_of_words)
    print(time.time() - start)

    start = time.time()
    histogram_of_histograms = histogram_of_histogram_value_counts(diction)
    print(time.time() - start)

    start = time.time()
    random_number = random.randint(0, 50)
    sentence = generate_a_sentence(random_number, histogram_of_histograms)
    print(time.time() - start)

    print(sentence)
    # start = time.time()
    # dict_of_tuples = first_dict_of_key_value_tuples(array_of_words)
    # print(time.time() - start)
    #
    # start = time.time()
    # histogram_of_histograms = histogram_of_histogram_value_counts(dict_of_tuples)
    # print(time.time() - start)
    #
    # start = time.time()
    # sentence = generate_a_sentence(12, histogram_of_histograms)
    # print(time.time() - start)
    #
    #
    # print(sentence)
