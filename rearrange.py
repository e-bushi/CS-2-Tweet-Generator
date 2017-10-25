import random
import sys
def rearrange(first_word, second_word, third_word, fourth_word):
    array = [first_word, second_word, third_word, fourth_word]
    new_array = []
    for word in array:
        generate = random.randint(0, 3)
        new_array.append(array[generate])

    print("{} {} {} {}".format(new_array[0], new_array[1], new_array[2], new_array[3]))


if __name__ == '__main__':
    params = sys.argv[1:]
    first_word = str(params[0])
    second_word = str(params[1])
    third_word = str(params[2])
    fourth_word = str(params[3])

    rearrange(first_word, second_word, third_word, fourth_word)
