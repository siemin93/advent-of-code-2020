from aoc1 import find_two

PREAMBLE_LENGTH = 25

def find_first_weakness(numbers):
    # O(n^2)
    preamble = numbers[:PREAMBLE_LENGTH]
    numbers_tail = numbers[PREAMBLE_LENGTH:]

    for number in numbers_tail:
        indexes, values = find_two(number, preamble)
        if indexes == (None, None):
            return number
        preamble.pop(0)
        preamble.append(number)

    return -1

def find_second_weakness(numbers, first_weakness):
    # O(n)
    i, j = sub_array_sum(numbers, first_weakness)
    contiguous_subsequence = numbers[i:j]
    smallest, largest = min(contiguous_subsequence), max(contiguous_subsequence)
    return smallest+largest

def sub_array_sum(numbers, target_sum):
    current_sum = numbers[0]
    left_index = 0

    for i in range(1, len(numbers)):
        while current_sum > target_sum and left_index < i - 1:
            current_sum = current_sum - numbers[left_index]
            left_index += 1

        if current_sum == target_sum:
            return (left_index, i - 1)

        if i < len(numbers):
            current_sum = current_sum + numbers[i]

    return (None, None)


if __name__ == "__main__":

    with open('./9.input', 'r') as f:
        lines = f.read().splitlines()

    numbers = [int(line) for line in lines]

    first_weakness = find_first_weakness(numbers)
    print('first_weakness', first_weakness)

    second_weakness = find_second_weakness(numbers, first_weakness)
    print('second_weakness', second_weakness)
