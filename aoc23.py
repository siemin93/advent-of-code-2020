
def run_task(lines, which_one=1):
    cups = list(map(int, lines[0]))
    if which_one == 2:
        cups = cups + list(range(max(cups)+1, 1000001))

    linked_list = {}
    value_to_pointer = {}
    for index, elem in enumerate(cups):
        linked_list[index] = (elem, index+1 if index+1 < len(cups) else 0)
        value_to_pointer[elem] = index

    run_moves(10000000 if which_one == 2 else 100, linked_list, value_to_pointer)

    if which_one == 1:
        result = []
        next_pointer = value_to_pointer[1]
        while True:
            result.append(linked_list[next_pointer][0])
            next_pointer = linked_list[next_pointer][1]

            if next_pointer == value_to_pointer[1]:
                break

        print('first_task', ''.join(map(str, result[1:])))
    else:
        a = linked_list[linked_list[value_to_pointer[1]][1]]
        b = linked_list[a[1]]
        print('second_task', a[0], b[0], a[0] * b[0])


def run_moves(moves_number, linked_list, value_to_pointer):
    max_value = max(value_to_pointer)
    new_addr = len(linked_list) + 1

    current_cup_pointer = 0

    for i in range(moves_number):
        picked_cups = [-1]*3

        current_value, next_pointer = linked_list[current_cup_pointer]
        for i in range(3):
            current_pointer = next_pointer
            value, next_pointer = linked_list[current_pointer]
            del linked_list[current_pointer]
            del value_to_pointer[value]
            picked_cups[i] = value

        linked_list[current_cup_pointer] = (current_value, next_pointer)

        destination_value = current_value - 1
        while True:
            if destination_value < 1:
                destination_value = max_value
            if destination_value in picked_cups:
                destination_value -= 1
            else:
                break

        destination_pointer = value_to_pointer[destination_value]

        for i in range(2, -1, -1):
            linked_list[new_addr] = (
                picked_cups[i], linked_list[destination_pointer][1])
            linked_list[destination_pointer] = (
                linked_list[destination_pointer][0], new_addr)
            value_to_pointer[picked_cups[i]] = new_addr
            new_addr += 1

        current_cup_pointer = linked_list[value_to_pointer[current_value]][1]


if __name__ == '__main__':

    with open('./23.input', 'r') as f:
        lines = f.read().splitlines()

    run_task(lines, 1)
    run_task(lines, 2)
