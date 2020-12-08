import re
import copy

def run_code(instructions, index, accumulator, is_main_branch):
    terminated = False

    while True:
        if index == len(instructions):
            terminated = True
            break

        operation, argument, was_visited = instructions[index]

        if was_visited:
            break

        if operation == 'nop':
            if is_main_branch:
                new_instructions = copy.deepcopy(instructions)
                new_instructions[index][2] = 1
                new_instructions[index][0] = 'jmp'
                run_code(new_instructions, index+argument, accumulator, False)

            instructions[index][2] = 1
            index += 1
            continue

        if operation == 'jmp':
            if is_main_branch:
                new_instructions = copy.deepcopy(instructions)
                new_instructions[index][2] = 1
                new_instructions[index][0] = 'nop'
                run_code(new_instructions, index+1, accumulator, False)

            instructions[index][2] = 1
            index += argument
            continue

        if operation == 'acc':
            instructions[index][2] = 1
            accumulator += argument
            index += 1
            continue

    if terminated:
        print('terminated', accumulator)

if __name__ == "__main__":

    with open('./8.input', 'r') as f:
        lines = f.read().splitlines()

    instructions = []

    for line in lines:
        pattern = re.compile("^(nop|acc|jmp) (\-?\+?\d*)$")
        if m := pattern.match(line):
            operation, argument = m.groups()
            instructions.append([operation, int(argument), 0])

    run_code(instructions, 0, 0, True)
