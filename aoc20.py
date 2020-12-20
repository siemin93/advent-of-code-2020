import re
import copy
import math

import numpy as np

# GIVE ME BACK MY SUNDAY

def flip_horizontal(borders):
    borders[1], borders[3] = borders[3], borders[1]
    borders[0] = borders[0][::-1]
    borders[2] = borders[2][::-1]
    return borders

def flip_vertical(borders):
    borders[0], borders[2] = borders[2], borders[0]
    borders[1] = borders[1][::-1]
    borders[3] = borders[3][::-1]
    return borders

def rotate_right(borders):
    borders[0], borders[1], borders[2], borders[3] = borders[3], borders[0], borders[1], borders[2]
    borders[0] = borders[0][::-1]
    borders[2] = borders[2][::-1]
    return borders

def get_borders(tile):
    right_border = []
    left_border = []
    for l in line:
        left_border.append(l[0])
        right_border.append(l[-1])

    return [
        ''.join(line[0]),
        ''.join(right_border),
        ''.join(line[-1]),
        ''.join(left_border)
    ]

def orientations(tile, original_tile):
    already_exists = set()
    result = []
    original_tiles = []

    fns = [
        [],

        [flip_horizontal],

        [rotate_right],
        [rotate_right, flip_horizontal],

        [rotate_right, rotate_right],
        [rotate_right, rotate_right, flip_horizontal],

        [rotate_right, rotate_right, rotate_right],
        [rotate_right, rotate_right, rotate_right, flip_horizontal],
    ]

    for transformations in fns:
        new_tile = copy.deepcopy(tile)
        new_original_tile = np.array(copy.deepcopy(original_tile))
        for f in transformations:
            f(new_tile)

            if f.__name__ == 'flip_horizontal':
                new_original_tile = np.flip(new_original_tile, axis=1)

            if f.__name__ == 'flip_vertical':
                new_original_tile = np.flip(new_original_tile, axis=0)

            if f.__name__ == 'rotate_right':
                new_original_tile = np.rot90(new_original_tile, 3)

        if not ''.join(new_tile) in already_exists:
            result.append(new_tile)
            original_tiles.append(new_original_tile)
            already_exists.add(''.join(new_tile))

    return result, original_tiles

def find_matching_to_my_bottom(my_tile_id, my_tile, tiles_map, already_used=None):
    if already_used == None:
        already_used = set()
    matching = []
    for tile_id, tile_orientations in tiles_map.items():
        if tile_id == my_tile_id:
            continue
        if tile_id in already_used:
            continue

        for i, o in enumerate(tile_orientations):
            if o[0] == my_tile[2]:
                matching.append((tile_id, i))
    return matching

def find_matching_to_my_right(my_tile_id, my_tile, tiles_map, already_used=None):
    if already_used == None:
        already_used = set()
    matching = []
    for tile_id, tile_orientations in tiles_map.items():
        if tile_id == my_tile_id:
            continue
        if tile_id in already_used:
            continue
        for i, o in enumerate(tile_orientations):
            if o[3] == my_tile[1]:
                matching.append((tile_id, i))
    return matching


def fill_column(board, column, tiles_map):
    possible_boards = [board]

    for row in range(0, len(board)-1):
        new_possible_boards = []

        if column == 0:
            for b in possible_boards:
                my_tile_id, orientation = b[row][column]
                possible_on_the_bottom = find_matching_to_my_bottom(my_tile_id, tiles_map[my_tile_id][orientation], tiles_map)

                if len(possible_on_the_bottom) == 0:
                    return []

                for p in possible_on_the_bottom:
                    id, orient = p
                    new_b = copy.deepcopy(b)
                    new_b[row+1][column] = (id, orient)
                    new_possible_boards.append(new_b)
        else:
            if row == 0:
                my_tile_id, orientation = board[row][column-1]
                possible_on_the_right = find_matching_to_my_right(my_tile_id, tiles_map[my_tile_id][orientation], tiles_map)

                if len(possible_on_the_right) == 0:
                    return []

                for p in possible_on_the_right:
                    id, orient = p
                    new_b = copy.deepcopy(board)
                    new_b[row][column] = (id, orient)
                    possible_boards = [new_b]

            for b in possible_boards:
                my_tile_id, orientation = b[row+1][column-1]
                allowed_on_the_right = find_matching_to_my_right(my_tile_id, tiles_map[my_tile_id][orientation], tiles_map)

                my_tile_id, orientation = b[row][column]
                possible_on_the_bottom = find_matching_to_my_bottom(my_tile_id, tiles_map[my_tile_id][orientation], tiles_map)
                added = 0
                for p in possible_on_the_bottom:
                    if p in allowed_on_the_right:
                        added += 1
                        id, orient = p
                        new_b = copy.deepcopy(b)
                        new_b[row+1][column] = (id, orient)
                        new_possible_boards.append(new_b)

                if added == 0:
                    return []

        possible_boards = new_possible_boards

    return possible_boards

if __name__ == '__main__':

    with open('./20.input', 'r') as f:
        lines = f.read().split('\n\n')

    tiles_map = {}
    tiles_original_map = {}

    for line in lines:
        line = line.split('\n')
        tile_id = int(line[0].replace('Tile ', '').replace(':', ''))
        if line[-1] == '':
            line.pop(-1)
        line.pop(0)

        tiles_original_map[tile_id] = [list(l) for l in line]
        tiles_map[tile_id] = get_borders(line)

    for tile_id, tile in tiles_map.items():
        tiles_map[tile_id], tiles_original_map[tile_id] = orientations(tile, tiles_original_map[tile_id])

    board_size = int(math.sqrt(len(tiles_map)))

    final_board = None

    for tile_id, tile_orientations in tiles_map.items():
        if final_board != None:
            break
        for i, o in enumerate(tile_orientations):
            board = [[None for i in range(board_size)] for j in range(board_size)]
            board[0][0] = (tile_id, i)

            boards = [board]

            for column in range(0, len(board)):
                new_boards = []
                for b in boards:
                    new_boards.extend(fill_column(b, column, tiles_map))
                boards = new_boards

            if len(boards) > 0:
                dd = boards[0]
                print(dd[0][0][0] * dd[-1][-1][0] * dd[0][-1][0] * dd[-1][0][0])
                final_board = dd
                break

    final_image = [[None for i in range(board_size)] for j in range(board_size)]
    for i, row in enumerate(final_board):
        for j, column in enumerate(row):
            tile_id, tile_orientation = column

            a = np.array(tiles_original_map[tile_id][tile_orientation])
            a = np.delete(a, 0, 0)
            a = np.delete(a, -1, 0)
            a = np.delete(a, -1, 1)
            a = np.delete(a, 0, 1)

            final_image[i][j] = a

    new_final_image = []
    for row in final_image:
        new_final_image.append(np.concatenate(row, axis=1))

    np_final = np.concatenate(new_final_image)

    monster = [
        '..................#.',
        '#....##....##....###',
        '.#..#..#..#..#..#...',
    ]

    def image_rotations(np_image):
        for _ in range(4):
            yield np_image
            yield np.flip(np_image, axis=1)
            np_image = np.rot90(np_image, 3)

    for np_image in image_rotations(np_final):
        image = []
        for l in np_image:
            image.append(''.join(l))

        count_monsters = 0

        for y in range(len(image)-len(monster)):
            for x in range(len(image)-len(monster[0])):
                match = True
                for i in range(len(monster)):
                    for j in range(len(monster[i])):
                        if monster[i][j] == '#' and image[y+i][x+j] != '#':
                            match = False
                            break

                    if not match:
                        break

                if match:
                    count_monsters += 1

        if count_monsters > 0:
            break

    final_strings = []
    for l in np_final:
        final_strings.append(''.join(l))

    print(f'monsters {count_monsters}')
    hash_all = ''.join(final_strings).count('#')
    hash_monster = ''.join(monster).count('#')
    print(hash_all - hash_monster * count_monsters)
