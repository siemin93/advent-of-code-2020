# -*- coding: utf-8 -*-

def first_task(numbers):
    difference_one = 0
    difference_three = 0

    for i in range(1, len(numbers)):
        if numbers[i-1] == numbers[i] - 1:
            difference_one += 1
        if numbers[i-1] == numbers[i] - 3:
            difference_three += 1

    print('first_task', difference_one * difference_three)

def second_task(numbers):
    print('second_task', count_paths(numbers, 0, [-1] * len(numbers)))

def count_paths(numbers, start_index, cache):
    if start_index == len(numbers) - 1:
        return 1

    if cache[start_index] != -1:
        return cache[start_index]

    paths = 0
    for i in range(start_index+1, len(numbers)):
        if numbers[i] - numbers[start_index] <= 3:
            c_paths = count_paths(numbers, i, cache)
            paths += 1 * c_paths

    cache[start_index] = paths
    return paths

if __name__ == "__main__":

    with open('./10.input', 'r') as f:
        lines = f.read().splitlines()

    numbers = [int(line) for line in lines]
    numbers.sort()
    numbers.insert(0, 0)
    numbers.append(numbers[len(numbers)-1]+3)

    first_task(numbers)
    second_task(numbers)
