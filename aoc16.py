import re
import math
from collections import defaultdict


def get_rules(lines):
    rules_end_index = lines.index('')
    for line in lines[:rules_end_index]:
        pattern = re.compile("^(.*): (\d*)-(\d*) or (\d*)-(\d*)$")
        if m := pattern.match(line):
            name, val1, val2, val3, val4 = m.groups()
            yield (name,
                set(range(int(val1), int(val2)+1)),
                set(range(int(val3), int(val4)+1)))

def first_task(rules, my_ticket, nearby_tickets):
    bad_numbers = []

    correct_tickets = []

    def is_valid_for_some_rule(value):
        for rule in rules:
            if ((value in rule[1])) or ((value in rule[2])):
                return True
        return False

    for ticket in nearby_tickets:
        is_correct = True
        for value in ticket:
            if not is_valid_for_some_rule(value):
                bad_numbers.append(value)
                is_correct = False
        if is_correct:
            correct_tickets.append(ticket)

    print('first_task', sum(bad_numbers))
    return correct_tickets

def second_task(rules, my_ticket, tickets):
    def check_if_column_passes_rule(rule, column_index):
        for ticket in tickets:
            val = ticket[column_index]
            if val not in rule[1] and val not in rule[2]:
                return False
        return True

    column_index_to_rule = defaultdict(list)

    for rule in rules:
        for column_index in range(len(tickets[0])):
            if check_if_column_passes_rule(rule, column_index):
                column_index_to_rule[column_index].append(rule)

    columns_selected = {}
    names_selected = set()
    how_many_columns_do_i_need = len(tickets[0])
    while len(columns_selected) < how_many_columns_do_i_need:
        for column_index, rules in column_index_to_rule.items():
            if len(rules) == 1:
                # the only choice
                columns_selected[column_index] = rules[0][0]
                names_selected.add(rules[0][0])
                column_index_to_rule[column_index] = []
            elif len(rules) > 1:
                # cleanup
                for i, rule in enumerate(rules):
                    if rule[0] in names_selected:
                        del column_index_to_rule[column_index][i]

    which_indexes = []
    for index, name in columns_selected.items():
        if name.startswith('departure'):
            which_indexes.append(index)

    my_values = []
    for index in which_indexes:
        my_values.append(int(my_ticket[index]))

    print('second_task', math.prod(my_values))


if __name__ == "__main__":

    with open('./16.input', 'r') as f:
        lines = f.read().splitlines()

    rules = list(get_rules(lines))

    my_ticket_index = lines.index('your ticket:') + 1
    my_ticket = [int(n) for n in lines[my_ticket_index].split(',')]

    nearby_tickets_index = lines.index('nearby tickets:') + 1
    nearby_tickets = [
        [int(n) for n in line.split(',')]
        for line in lines[nearby_tickets_index:]
    ]

    correct_tickets = first_task(rules, my_ticket, nearby_tickets)
    second_task(rules, my_ticket, correct_tickets)
