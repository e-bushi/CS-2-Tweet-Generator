import random
import sys
def rearrange(array):
    new_array = array
    array_to_build = []

    while 0 < len(new_array):
        generate = random.randint(0, len(array) - 1)
        array_to_build.append(array[generate])
        new_array.pop(generate)

    return " ".join(array_to_build)


if __name__ == '__main__':
    params = sys.argv[1:]
    print(rearrange(params))
