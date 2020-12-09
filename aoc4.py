import re

def is_corrent(name, value):
    fname = 'is_correct_' + name
    if fname in globals():
        return globals()[fname](value)
    return False

def is_correct_byr(value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    pattern = re.compile("^\d{4}$")
    if pattern.match(value) and int(value) >= 1920 and int(value) <= 2002:
        return True
    return False

def is_correct_iyr(value):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    pattern = re.compile("^\d{4}$")
    if pattern.match(value) and int(value) >= 2010 and int(value) <= 2020:
        return True
    return False

def is_correct_eyr(value):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    pattern = re.compile("^\d{4}$")
    if pattern.match(value) and int(value) >= 2020 and int(value) <= 2030:
        return True
    return False

def is_correct_hgt(value):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    pattern = re.compile("^(\d*)(cm|in)$")
    if m := pattern.match(value):
        val, metric = m.groups()
        if metric == 'cm' and int(val) >= 150 and int(val) <= 193:
            return True
        elif metric == 'in' and int(val) >= 59 and int(val) <= 76:
            return True
    return False

def is_correct_hcl(value):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    pattern = re.compile("^#([0-9]|[a-f]){6}")
    if m := pattern.match(value):
        return True
    return False

def is_correct_ecl(value):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    values = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    if value in values:
        return True
    return False

def is_correct_pid(value):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # value = value.lstrip('0')
    pattern = re.compile("^\d{9}$")
    if pattern.match(value):
        return True
    return False

def is_correct_cid(value):
    # cid (Country ID) - ignored, missing or not.
    return True

if __name__ == "__main__":

    with open('./4.input', 'r') as f:
        documents = f.read().split('\n\n')

    valid = 0

    for document in documents:
        document = document.replace('\n', ' ', -1)
        fields = document.split(' ')

        required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

        for field in fields:
            try:
                name, value = field.split(':')

                if is_corrent(name, value):
                    required.remove(name)
            except Exception as e:
                pass

        if len(required) == 0 or (len(required) == 1 and 'cid' in required):
            valid += 1

    print(valid)
