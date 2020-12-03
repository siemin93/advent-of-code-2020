import math

if __name__ == "__main__":

    with open('./3.input', 'r') as f:
        lines = f.read().splitlines()

    rows = len(lines)
    columns = len(lines[0])

    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    cases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    trees_sizes = set()

    for case in cases:
        trees = 0
        from_left_index = 0
        from_top_index = 0
        right, down = case
        while True:
            from_left_index += right
            from_top_index += down

            if lines[from_top_index][from_left_index % columns] == '#':
                trees += 1

            if from_top_index == rows - 1:
                break

        trees_sizes.add(trees)

    print(trees_sizes)
    print(math.prod(trees_sizes))
