

def get_neighbours(cube):
    x, y, z, w = cube
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range (-1, 2):
                for l in range (-1, 2):
                    new_cube = (x+i, y+j, z+k, w+l)
                    if new_cube != cube:
                        yield new_cube

def one_cycle(active):
    active_to_check = list(active)
    was_checked = set()
    new_active = set()

    for cube in active_to_check:
        neighbours = get_neighbours(cube)

        parent_how_many_active = 0

        for neigh in neighbours:
            if neigh in active:
                parent_how_many_active += 1
            if neigh in was_checked:
                continue

            inner_neighbours = get_neighbours(neigh)

            how_many_active_neigh = 0
            for inner_neigh in inner_neighbours:
                if inner_neigh in active:
                    how_many_active_neigh += 1

            if how_many_active_neigh == 3:
                new_active.add(neigh)

        if parent_how_many_active == 2 or parent_how_many_active == 3:
            new_active.add(cube)

        was_checked.add(cube)

    return new_active


if __name__ == "__main__":

    with open('./17.input', 'r') as f:
        lines = f.read().splitlines()

    active = set()
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            if val == '#':
                active.add((i, j, 0, 0))

    for i in range(6):
        active = one_cycle(active)

    print('second_task', len(active))
