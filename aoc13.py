# -*- coding: utf-8 -*-

def first_task(my_timestamp, buses):
    buses_without_x = [int(bus_id) for bus_id in lines[1].split(',') if bus_id != 'x']

    check_timestamp = my_timestamp
    while True:
        for bus in buses_without_x:
            if check_timestamp % bus == 0:
                print('first_task:', (check_timestamp-my_timestamp)*bus)
                return
        check_timestamp += 1

def second_task(buses):
    buses_with_position = []
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        buses_with_position.append((int(bus), i))

    buses_with_position.sort(reverse=True)

    check_timestamp = 0
    current_step = 1
    for bus, departure_offset in buses_with_position:
        while True:
            if (check_timestamp + departure_offset) % bus == 0:
                current_step *= bus
                break
            check_timestamp += current_step

    print('second_task', check_timestamp)

if __name__ == "__main__":

    with open('./13.input', 'r') as f:
        lines = f.read().splitlines()

    my_timestamp = int(lines[0])
    buses = [bus_id for bus_id in lines[1].split(',')]

    first_task(my_timestamp, buses)
    second_task(buses)
