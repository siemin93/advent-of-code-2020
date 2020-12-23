if __name__ == '__main__':

    with open('./23.input', 'r') as f:
        lines = f.read().splitlines()

    cups = list(map(int, lines[0]))
    print('cups', cups)
    current_cup = cups[0]
    current_cup_index = cups.index(current_cup)

    cups = cups + list(range(max(cups)+1, 1000001))

    for i in range(10000000):
        if i % 100000 == 0:
            print(i)

        picked_cups = cups[current_cup_index+1:current_cup_index+4]
        cups = cups[:current_cup_index+1] + cups[current_cup_index+4:]

        if len(picked_cups) < 3:
            left = 3 - len(picked_cups)
            picked_cups = picked_cups + cups[:left]
            cups = cups[left:]

        # print(picked_cups)
        # print(cups)

        destination_cup_index = None
        destination_value = current_cup - 1
        while destination_cup_index == None:
            if destination_value in cups:
                destination_cup_index = cups.index(destination_value)
            else:
                destination_value -= 1
                if destination_value < min(cups):
                    destination_value = max(cups)

        # print('destination_cup_index', destination_cup_index)

        cups = cups[:destination_cup_index+1] + picked_cups + cups[destination_cup_index+1:]
        # print(cups)

        current_cup_index = (cups.index(current_cup) + 1) % len(cups)
        current_cup = cups[current_cup_index]

        # print('current_cup_index', current_cup_index)
        # print('current_cup', current_cup)

    ind = cups.index(1)
    print(cups[ind+1], cups[ind+2], cups[ind+1]*cups[ind+2])
