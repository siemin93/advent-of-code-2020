import re

from collections import defaultdict

def find_loop_size(public_key):
    start_value = 1
    for i in range(1, 100000000):
        start_value *= 7
        start_value %= 20201227
        if start_value == public_key:
            return i

    return -1

def transform(subject_number, loop_size):
    start_value = 1
    for _ in range(loop_size):
        start_value *= subject_number
        start_value %= 20201227

    return start_value

if __name__ == "__main__":

    with open('./25.input', 'r') as f:
        lines = f.read().splitlines()

    # card_public_key = 5764801
    # doors_public_key = 17807724
    card_public_key = 10943862
    doors_public_key = 12721030

    card_loop_size = find_loop_size(card_public_key)
    print(transform(doors_public_key, card_loop_size))
