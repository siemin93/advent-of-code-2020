import re


class aoc_int1(int):
    # the operators have the same precedence
    def __mul__(self, other):
        return aoc_int1(int(self) * other)

    def __truediv__(self, other):
        return aoc_int1(int(self) + other)

    @staticmethod
    def change_operators(line):
        return line \
            .replace('+', '/')


class aoc_int2(int):
    # the addition before the multiplication
    def __mul__(self, other):
        return aoc_int2(int(self) + other)

    def __sub__(self, other):
        return aoc_int2(int(self) * other)

    @staticmethod
    def change_operators(line):
        return line \
            .replace('*', '-') \
            .replace('+', '*')


def run_task(task, lines, cls):
    result = sum([eval_task(line, cls) for line in lines])
    print(f'{task} task', result)

def eval_task(line, cls):
    line_with_aoc_int = re.sub(r'\d+', lambda match: f'{cls.__name__}({match.group()})' , line)
    line_with_aoc_int = cls.change_operators(line_with_aoc_int)
    return eval(line_with_aoc_int)


if __name__ == "__main__":

    with open('./18.input', 'r') as f:
        lines = f.read().splitlines()

    run_task('first', lines, aoc_int1)
    run_task('second', lines, aoc_int2)
