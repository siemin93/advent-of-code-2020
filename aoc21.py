from collections import defaultdict

if __name__ == '__main__':

    with open('./21.input', 'r') as f:
        lines = f.read().splitlines()

    parsed = []
    for line in lines:
        ing, allerg = line.split(' (contains ')
        ing = ing.split(' ')
        allerg = allerg.replace(')', '').split(', ')
        parsed.append((ing, allerg))

    allergen_can_be_in = {}

    for p in parsed:
        ings, allerg = p

        for a in allerg:
            if a in allergen_can_be_in:
                allergen_can_be_in[a] = allergen_can_be_in[a].intersection(set(ings))
            else:
                allergen_can_be_in[a] = set(ings)

    s = allergen_can_be_in.items()
    s = sorted(s, key=lambda a: len(a[1]))

    how_many_do_i_need = len(allergen_can_be_in.keys())
    is_used = {}
    while len(is_used) < how_many_do_i_need:
        for i in s:
            allerg, ings = i
            for a in is_used.keys():
                if a in ings:
                    ings.remove(a)
            if len(ings) == 1:
                is_used[list(ings)[0]] = allerg

    all_ings = sum([p[0] for p in parsed], [])
    for i in is_used.keys():
        all_ings = [x for x in all_ings if x != i]

    a2 = sorted(is_used.items(), key=lambda a: a[1])

    print('first_task', len(all_ings))
    print('second_task', ','.join([a[0] for a in a2]))
