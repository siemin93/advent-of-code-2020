# -*- coding: utf-8 -*-

from enum import Enum
import copy

class CheckType(Enum):
    NEAREST = 1
    WHOLE_ANGLE = 2

def first_task(seats):
    changed_count = 1
    while changed_count > 0:
        seats, changed_count = change_state(seats, 4, CheckType.NEAREST)
    print('first_task', how_many_occupied(seats))

def second_task(seats):
    changed_count = 1
    while changed_count > 0:
        seats, changed_count = change_state(seats, 5, CheckType.WHOLE_ANGLE)
    print('second_task', how_many_occupied(seats))

def check_occupied(seats, row, column, angles, check_type):
    i = row
    j = column
    row_inc, column_inc = angles
    while True:
        i += row_inc
        j += column_inc

        if (i < 0) or (j < 0) or (i == len(seats)) or (j == len(seats[0])):
            return False

        if seats[i][j] == '#':
            return True
        elif seats[i][j] == 'L':
            return False

        if check_type == CheckType.NEAREST:
            return False

def change_state(seats, occupied_flip_cond, check_type):
    new_seats = copy.deepcopy(seats)
    angles = [
        (0, -1), (0, 1),
        (-1, 0), (-1, -1), (-1, 1),
        (1, 0), (1, -1), (1, 1)
    ]
    changed_count = 0

    for row in range(len(seats)):
        for column in range(len(seats[0])):
            if seats[row][column] == '.':
                continue

            occupied = 0
            for angle in angles:
                occupied += 1 if check_occupied(seats, row, column, angle, check_type) else 0

            if occupied == 0 and seats[row][column] == 'L':
                new_seats[row][column] = '#'
                changed_count += 1
            elif occupied >= occupied_flip_cond and seats[row][column] == '#':
                new_seats[row][column] = 'L'
                changed_count += 1

    return (new_seats, changed_count)

def print_seats(seats):
    for row in range(len(seats)):
        print(''.join(seats[row]))

def how_many_occupied(seats):
    occupied = 0
    for row in range(len(seats)):
        for column in range(len(seats[0])):
            if seats[row][column] == '#':
                occupied += 1
    return occupied

if __name__ == "__main__":

    with open('./11.input', 'r') as f:
        lines = f.read().splitlines()

    seats = [list(l) for l in lines]

    first_task(seats)
    second_task(seats)
