import re
import copy
import math

import numpy as np

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

def orientations(tile):
    already_exists = set()
    result = []

    fns = [
        [],

        [flip_horizontal],
        [flip_vertical],

        [flip_horizontal, flip_vertical],
        [flip_vertical, flip_horizontal],

        [rotate_right],
        [rotate_right, flip_horizontal],
        [rotate_right, flip_vertical],
        [rotate_right, flip_horizontal, flip_vertical],
        [rotate_right, flip_vertical, flip_horizontal],

        [rotate_right, rotate_right],
        [rotate_right, rotate_right, flip_horizontal],
        [rotate_right, rotate_right, flip_vertical],
        [rotate_right, rotate_right, flip_horizontal, flip_vertical],
        [rotate_right, rotate_right, flip_vertical, flip_horizontal],

        [rotate_right, rotate_right, rotate_right],
        [rotate_right, rotate_right, rotate_right, flip_horizontal],
        [rotate_right, rotate_right, rotate_right, flip_vertical],
        [rotate_right, rotate_right, rotate_right, flip_horizontal, flip_vertical],
        [rotate_right, rotate_right, rotate_right, flip_vertical, flip_horizontal],
    ]

    for transformations in fns:
        new_tile = copy.deepcopy(tile)
        for f in transformations:
            f(new_tile)

        if not ''.join(new_tile) in already_exists:
            result.append(new_tile)
            already_exists.add(''.join(new_tile))

    return result

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

        tiles_original_map[tile_id] = line
        tiles_map[tile_id] = get_borders(line)

    for tile_id, tile in tiles_map.items():
        tiles_map[tile_id] = orientations(tile)

    # board_size = int(math.sqrt(len(tiles_map)))

    # final_board = None

    # for tile_id, tile_orientations in tiles_map.items():
    #     if final_board != None:
    #         break
    #     for i, o in enumerate(tile_orientations):
    #         board = [[None for i in range(board_size)] for j in range(board_size)]
    #         board[0][0] = (tile_id, i)

    #         boards = [board]

    #         for column in range(0, len(board)):
    #             new_boards = []
    #             for b in boards:
    #                 new_boards.extend(fill_column(b, column, tiles_map))
    #             boards = new_boards

    #         if len(boards) > 0:
    #             dd = boards[0]
    #             print(dd[0][0][0] * dd[-1][-1][0] * dd[0][-1][0] * dd[-1][0][0])
    #             final_board = dd
    #             break

    # print(final_board)

    final_board = [[(1951, 2), (2311, 2), (3079, 0)], [(2729, 2), (1427, 2), (2473, 6)], [(2971, 2), (1489, 2), (1171, 1)]]
    for elem in final_board:
        tile_id, tile_orientation = elem
        print(tiles_original_map[tile_id])
