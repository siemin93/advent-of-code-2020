import re

def run_task(rules, messages):
    rules_map = parse_rules(rules)
    regex_0 = create_regex('0', rules_map)
    how_many = 0
    for line in messages:
        if re.match(f'^{regex_0}$', line):
            how_many += 1
    return how_many

def parse_rules(rules):
    rules_map = {}

    for line in rules:
        rule_index, rule_resolves_to = line.split(': ')

        if '"a"' in rule_resolves_to:
            rules_map[rule_index] = 'a'
        elif '"b"' in rule_resolves_to:
            rules_map[rule_index] = 'b'
        else:
            options = rule_resolves_to.split(' | ')
            rules_map[rule_index] = [
                [r_index for r_index in option.split(' ')]
                for option in options
            ]

    return rules_map

def create_regex(rule_index, rules_map, recursion_depth=0):
        if rules_map[rule_index] in ['a', 'b']:
            return rules_map[rule_index]

        if recursion_depth == 128:
            return ''

        options = []
        for option in rules_map[rule_index]:
            option_regexes = [
                create_regex(i, rules_map, recursion_depth+1)
                for i in option
            ]
            options.append(''.join(option_regexes))

        return f'({"|".join(options)})'


if __name__ == '__main__':

    with open('./19.input', 'r') as f:
        lines = f.read().splitlines()

    rules_and_messages_separator = lines.index('')

    rules = lines[:rules_and_messages_separator]
    messages = lines[rules_and_messages_separator+1:]

    print(run_task(rules, messages))

    rules[rules.index('8: 42')] = '8: 42 | 42 8'
    rules[rules.index('11: 42 31')] = '11: 42 31 | 42 11 31'

    print(run_task(rules, messages))
