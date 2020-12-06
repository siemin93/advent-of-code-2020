if __name__ == "__main__":

    with open('./6.input', 'r') as f:
        lines = f.read().split('\n\n')
        lines[-1] = lines[-1][:-1]
    groups = [g.split('\n') for g in lines]

    counts = []

    for group in groups:
        answered_yes = set()
        for answers in group:
            answered_yes.update(set(answers))
        counts.append(len(answered_yes))

    print(sum(counts))

    counts = []

    for group in groups:
        group_answers = [set(guy) for guy in group]
        answered_yes = group_answers[0].intersection(*group_answers)
        counts.append(len(answered_yes))

    print(sum(counts))
