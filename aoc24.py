import re

from collections import defaultdict

def is_to_flip(floor, pos):
    how_many_black = 0
    for delta_x, delta_y in [(2, 0), (-2, 0), (+1, -1), (-1, +1), (+1, +1), (-1, -1)]:
        if floor.get((pos[0]+delta_x, pos[1]+delta_y)):
            how_many_black += 1

    if not floor[pos] and how_many_black == 2:
        return True

    if floor[pos] and (how_many_black == 0 or how_many_black > 2):
        return True

    return False

if __name__ == "__main__":

    with open('./24.input', 'r') as f:
        lines = f.read().splitlines()

    # (posX, posY) -> is black
    floor = defaultdict(lambda: False)

    for line in lines:
        cords = re.findall(r'e|se|sw|w|nw|ne', line)

        def replace(c):
            if c == 'e':
                return '→'
            if c == 'w':
                return '←'
            if c == 'se':
                return '↘'
            if c == 'sw':
                return '↙'
            if c == 'nw':
                return '↖'
            if c == 'ne':
                return '↗'

        cords = list(map(replace, cords))

        X = cords.count('↗') - cords.count('↙') + cords.count('↘') - cords.count('↖') \
            - 2 * cords.count('←') + 2 * cords.count('→')
        Y = cords.count('↖') - cords.count('↘') + cords.count('↗') - cords.count('↙')

        floor[(X, Y)] = not floor[(X, Y)]

    print('first_task', sum(floor.values()))

    for i in range(100):
        to_flip = set()
        was_checked = set()
        k = list(floor.keys())
        for pos in k:
            if is_to_flip(floor, pos):
                to_flip.add(pos)

            for delta_x, delta_y in [(2, 0), (-2, 0), (+1, -1), (-1, +1), (+1, +1), (-1, -1)]:
                pos2 = (pos[0]+delta_x, pos[1]+delta_y)
                if pos2 in was_checked:
                    continue

                if is_to_flip(floor, pos2):
                    to_flip.add(pos2)

                was_checked.add(pos2)

        for pos in to_flip:
            floor[pos] = not floor[pos]

        print('day', i,  sum(floor.values()))
