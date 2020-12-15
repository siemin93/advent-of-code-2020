# -*- coding: utf-8 -*-

import re
import copy

def first_task(lines):
    memory = {}
    mask = {}

    for line in lines:
        if line.startswith('mask ='):
            line = line.replace('mask = ', '')
            mask = line
        else:
            pattern = re.compile("^mem\[(\d*)\] = (\d*)$")
            if m := pattern.match(line):
                address, value = m.groups()

                memory[address] = (
                    (int(value)
                    & int(mask.replace('1', '0').replace('X', '1'), 2))
                    | int(mask.replace('X', '0'), 2)
                )

    print('first_task', sum(memory.values()))

def second_task(lines):
    memory = {}
    mask = {}

    for line in lines:
        if line.startswith('mask ='):
            line = line.replace('mask = ', '')
            mask = line
        else:
            pattern = re.compile("^mem\[(\d*)\] = (\d*)$")
            if m := pattern.match(line):
                address, value = m.groups()

                address = int(address) & int(mask
                    .replace('0', '1')
                    .replace('X', '0')
                    , 2)

                write_to_memory(memory, mask, address, int(value))

    print('second_task', sum(memory.values()))

def write_to_memory(memory, mask, address, value):
    try:
        i = mask.index('X')
        write_to_memory(memory, mask[:i] + '0' + mask[i+1:], address, value)
        write_to_memory(memory, mask[:i] + '1' + mask[i+1:], address, value)
    except:
        memory[int(mask, 2) | address] = value


if __name__ == "__main__":

    with open('./14.input', 'r') as f:
        lines = f.read().splitlines()

    first_task(lines)
    second_task(lines)
