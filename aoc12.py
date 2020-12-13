# -*- coding: utf-8 -*-

import re

def first_task(instructions):
    all_facings = ['N', 'E', 'S', 'W']
    current_facing = 'E'

    current_position = {
        'E': 0,
        'W': 0,
        'S': 0,
        'N': 0,
    }

    for instruction in instructions:
        action, value = instruction

        if action == 'F':
            current_position[current_facing] += value
        elif action == 'L':
            current_index = all_facings.index(current_facing)
            rotation = int(value / 90)
            new_index = (current_index - rotation) % len(all_facings)
            current_facing = all_facings[new_index]
        elif action == 'R':
            current_index = all_facings.index(current_facing)
            rotation = int(value / 90)
            new_index = (current_index + rotation) % len(all_facings)
            current_facing = all_facings[new_index]
        else:
            current_position[action] += value


    a = abs(current_position['W']-current_position['E'])
    b = abs(current_position['N']-current_position['S'])
    print('first task', a, b, a+b)

def second_task(instructions):
    ship_current_position = {
        'E': 0,
        'W': 0,
        'S': 0,
        'N': 0,
    }

    all_facings = [('NE'), ('SE'), ('SW'), ('NW')]
    waypoint_current_facing = ['N', 'E']

    waypoint_relative_position = {
        'X': 10,
        'Y': 1,
    }

    for instruction in instructions:
        action, value = instruction

        if action == 'F':
            y_axis = waypoint_current_facing[0]
            x_axis = waypoint_current_facing[1]
            diff_Y = waypoint_relative_position['Y']
            diff_X = waypoint_relative_position['X']
            ship_current_position[y_axis] += value * diff_Y
            ship_current_position[x_axis] += value * diff_X
        elif action == 'L':
            current_index = all_facings.index(''.join(waypoint_current_facing))
            rotation = int(value / 90)
            if rotation % 2 == 1:
                y = waypoint_relative_position['Y']
                waypoint_relative_position['Y'] = waypoint_relative_position['X']
                waypoint_relative_position['X'] = y
            new_index = (current_index - rotation) % len(all_facings)
            waypoint_current_facing = list(all_facings[new_index])
        elif action == 'R':
            current_index = all_facings.index(''.join(waypoint_current_facing))
            rotation = int(value / 90)
            if rotation % 2 == 1:
                y = waypoint_relative_position['Y']
                waypoint_relative_position['Y'] = waypoint_relative_position['X']
                waypoint_relative_position['X'] = y
            new_index = (current_index + rotation) % len(all_facings)
            waypoint_current_facing = list(all_facings[new_index])
        else:
            if action == 'N' or action == 'S':
                if action == waypoint_current_facing[0]:
                    waypoint_relative_position['Y'] += value
                else:
                    waypoint_relative_position['Y'] -= value
                    if waypoint_relative_position['Y'] < 0:
                        waypoint_relative_position['Y'] = -waypoint_relative_position['Y']
                        waypoint_current_facing[0] = action
            if action == 'E' or action == 'W':
                if action == waypoint_current_facing[1]:
                    waypoint_relative_position['X'] += value
                else:
                    waypoint_relative_position['X'] -= value
                    if waypoint_relative_position['X'] < 0:
                        waypoint_relative_position['X'] = -waypoint_relative_position['X']
                        waypoint_current_facing[1] = action

    a = abs(ship_current_position['W']-ship_current_position['E'])
    b = abs(ship_current_position['N']-ship_current_position['S'])
    print('second task', a, b, a+b)


if __name__ == "__main__":

    with open('./12.input', 'r') as f:
        lines = f.read().splitlines()

    instructions = []
    pattern = re.compile("^(.)(\d*)$")
    for line in lines:
        if m := pattern.match(line):
            action, value = m.groups()
            instructions.append((action, int(value)))

    first_task(instructions)
    second_task(instructions)
