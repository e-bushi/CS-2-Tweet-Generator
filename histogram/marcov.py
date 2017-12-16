import histogram
import random

def key_word_value_array_dict(word_list):
    word_dict = {}
    for i in range(0, len(word_list) - 1):
        if word_list[i] in word_dict:
            word_dict[word_list[i]].append(word_list[i+1])
        else:
            word_dict[word_list[i]] = [word_list[i+1]]
    print(word_dict)
    return word_dict


def dictionary_of_list_counts(word_dict):
    dict_to_return = {}
    for k, v in word_dict.items():
        dict_to_return[k] = histogram.histogram_dict(v)
        # for i in v:
        #     if k in dict_to_return:
        #     dict_to_return[k] = {i: v.count(i)}
    # print(dict_to_return)
    return dict_to_return


def generate_word(key_value, dict_):
    a_histogram = dict_[key_value] #this line returns the values of dict_ which is a histogram
    total = histogram.token_total(a_histogram) # returns the total number of tokens in the histogram
    random_num = random.randint(0, total)

    for word in a_histogram:
        if random_num > a_histogram[word]: #if the random number generated is greater than the frequency of the word
            random_num -= a_histogram[word] #then we will subtract the frequency of the word from the random number
        else:
            return word


def generate_(number_of_words, dict_):
    sentence = []
    list_of_keys = []
    # for i in dict_:
    #     word = generate_word(i, dict_)
    #     sentence.append(word)
    #     number += 1
    #
    #     if number == number_of_words:
    #         break
    #
    # return sentence
    for k in dict_.keys():
        list_of_keys.append(k)

    random_num = random.randint(0, len(list_of_keys) - 1)
    word = list_of_keys[random_num]

    for _ in range(0, number_of_words):
        new_word = generate_word(word, dict_)
        sentence.append(new_word)
        word = new_word

    return ' '.join(sentence)









if __name__ == '__main__':
    word_list = ["one", "fish", "two", "fish", "blue", "fish", "red", "fish"]
    dictiona = key_word_value_array_dict(word_list)
    # print(dictiona)
    new_diction = dictionary_of_list_counts(dictiona)
    # print(new_diction)
    # string = generate_sentence(new_diction)
    # print(string)
    sentence = generate_(10, new_diction)
    print(sentence)
