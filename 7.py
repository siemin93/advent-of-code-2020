import re
from collections import defaultdict

def get_rules_from_input(lines):
    rules = {}
    for line in lines:
        line = line \
            .replace('bags', '') \
            .replace('bag', '') \
            .replace('.', '')

        bag_name, contain = line.split(' contain ')
        contain = contain.split(',')

        bag_name = bag_name.strip()
        contain = [c.strip() for c in contain]

        contain_with_quantity = []
        for bag in contain:
            pattern = re.compile("^(\d*) (.*)$")
            if m := pattern.match(bag):
                quantity, inner_bag_name = m.groups()
                contain_with_quantity.append((quantity, inner_bag_name))

        rules[bag_name] = contain_with_quantity

    return rules

def answear_task1(rules):
    rules_reversed = defaultdict(list)
    for bag_name, contain in rules.items():
        for bag in contain:
            _, inner_bag_name = bag
            rules_reversed[inner_bag_name].append(bag_name)

    visited = set()
    dumb_dfs(rules_reversed, 'shiny gold', visited)
    print(len(visited))

def answear_task2(rules):
    print(how_many_inside(rules, 'shiny gold') - 1)

def dumb_dfs(bags, bag, visited):
    for b in bags[bag]:
        if b not in visited:
            visited.add(b)
            dumb_dfs(bags, b, visited)

def how_many_inside(rules, bag):
    how_many = 1
    for contain in rules[bag]:
        quantity, bag_name = contain
        inside = how_many_inside(rules, bag_name)
        how_many += int(quantity) * inside
    return how_many

if __name__ == "__main__":

    with open('./7.input', 'r') as f:
        lines = f.read().splitlines()

    rules = get_rules_from_input(lines)

    answear_task1(rules)
    answear_task2(rules)
