from collections import deque


def combat(cards_p1, cards_p2):
    cards_player_1 = list(cards_p1)
    cards_player_2 = list(cards_p2)

    while len(cards_player_1) > 0 and len(cards_player_2) > 0:
        p1 = cards_player_1.pop(0)
        p2 = cards_player_2.pop(0)

        if p1 > p2:
            cards_player_1.extend([p1, p2])
        else:
            cards_player_2.extend([p2, p1])

    to_multiply = list(cards_player_1) or list(cards_player_2)
    print(sum([a[0] * a[1] for a in zip(to_multiply, range(len(to_multiply), 0, -1))]))


def recursive_combat(cards_player_1, cards_player_2, cache):
    cards_player_1 = list(cards_player_1)
    cards_player_2 = list(cards_player_2)

    if cache == None:
        cache = set()

    while len(cards_player_1) > 0 and len(cards_player_2) > 0:
        if ((str(cards_player_2), str(cards_player_1))) in cache:
            return ('p1-wins', cards_player_1, cards_player_2)
        cache.add((str(cards_player_2), str(cards_player_1)))

        p1 = cards_player_1.pop(0)
        p2 = cards_player_2.pop(0)

        if p1 <= len(cards_player_1) and p2 <= len(cards_player_2):
            result = recursive_combat(cards_player_1[:p1], cards_player_2[:p2], None)
            if result[0] == 'p1-wins':
                cards_player_1.extend([p1, p2])
            else:
                cards_player_2.extend([p2, p1])
        else:
            if p1 > p2:
                cards_player_1.extend([p1, p2])
            else:
                cards_player_2.extend([p2, p1])

    if len(cards_player_1) == 0:
        return ('p2-wins', cards_player_1, cards_player_2)
    else:
        return ('p1-wins', cards_player_1, cards_player_2)


if __name__ == '__main__':

    with open('./22.input', 'r') as f:
        lines = f.read().splitlines()

    p2_index = lines.index('Player 2:')

    cards_player_1 = list(map(int, lines[1:p2_index-1]))
    cards_player_2 = list(map(int, lines[p2_index+1:]))

    # first task
    combat(cards_player_1, cards_player_2)

    # second task
    result = recursive_combat(cards_player_1, cards_player_2, None)
    to_multiply = list(result[1]) or list(result[2])
    print(sum([a[0] * a[1] for a in zip(to_multiply, range(len(to_multiply), 0, -1))]))
