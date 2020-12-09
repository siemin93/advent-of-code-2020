import math

def find_two(needed_sum, arr):
    needed_on_index = {}
    for i in range(len(arr)):
        needed_on_index[needed_sum-arr[i]] = i

    for i in range(len(arr)):
        if arr[i] in needed_on_index:
            j = needed_on_index[arr[i]]
            return ((i, j), (arr[i], arr[j]))

    return ((None, None), (None, None))

def find_three(needed_sum, arr):
    for i in range(len(arr)):
        current = numbers[i]
        needed = needed_sum - current
        new_numbers = numbers[:i] + [needed_sum+1] + numbers[i+1:]
        i1, i2 = find_two(needed, new_numbers)[0]
        if i1 is not None:
            return ((i, i1, i2), (numbers[i], numbers[i1], numbers[i2]))

if __name__ == "__main__":

    with open('./1.input', 'r') as f:
        lines = f.read().splitlines()

    numbers = [int(i) for i in lines]

    indexes, values = find_two(2020, numbers)
    print(math.prod(values))
    indexes, values = find_three(2020, numbers)
    print(math.prod(values))
