import copy

def both_tasks(start_numbers, desired_turn):
    local_start_numbers = copy.deepcopy(start_numbers)

    when_was_spoken = {}

    turn_index = 1
    last_number_is_new = False
    last_number = -1

    while turn_index <= desired_turn:
        if len(local_start_numbers) > 0:
            last_number = local_start_numbers.pop(0)
        elif last_number_is_new:
            last_number = 0
        else:
            last_spoken_indexes = when_was_spoken[last_number]
            last_number = last_spoken_indexes[-1] - last_spoken_indexes[-2]

        if not last_number in when_was_spoken:
            last_number_is_new = True
            when_was_spoken[last_number] = [-1, turn_index]
        else:
            last_number_is_new = False
            when_was_spoken[last_number][0] = when_was_spoken[last_number][1]
            when_was_spoken[last_number][1] = turn_index

        turn_index += 1

    return last_number


if __name__ == "__main__":

    with open('./15.input', 'r') as f:
        lines = f.read().splitlines()

    numbers = [int(number) for number in lines[0].split(',')]

    print('first_task', both_tasks(numbers, 2020))
    print('second_task', both_tasks(numbers, 30000000))
