from collections import defaultdict

def prepare_letter_count(word):
    counts = defaultdict(int)
    for letter in word:
        counts[letter] += 1
    return counts

def is_letter_at_pos(word, letter, pos):
    if pos > len(word):
        return False
    pos = pos - 1
    if word[pos] == letter:
        return True
    else:
        return False


if __name__ == "__main__":

    with open('./2.input', 'r') as f:
        lines = f.read().splitlines()

    valid = 0

    # 2a
    # for line in lines:
    #     must, word = line.split(': ')
    #     nums, letter = must.split(' ')
    #     min_num, max_num = nums.split('-')
    #     letter_count = prepare_letter_count(word)
    #     print(min_num, max_num, letter, word, letter_count)
    #     count = letter_count[letter]
    #     if count >= int(min_num) and count <= int(max_num):
    #         valid += 1

    # 2b

    for line in lines:
        must, word = line.split(': ')
        nums, letter = must.split(' ')
        min_num, max_num = nums.split('-')
        min_num = int(min_num)
        max_num = int(max_num)
        c = 0
        if is_letter_at_pos(word, letter, min_num):
            c += 1
        if is_letter_at_pos(word, letter, max_num):
            c += 1
        if c == 1:
            valid += 1
            print(line)

    print(valid)
