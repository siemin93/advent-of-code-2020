

def bin_search(arr, code):
    if len(arr) == 1:
        return arr[0]

    if code[0] == 'F' or code[0] == 'L':
        return bin_search(arr[:int(len(arr)/2)], code[1:])
    elif code[0] == 'B' or code[0] == 'R':
        return bin_search(arr[int(len(arr)/2):], code[1:])


if __name__ == "__main__":

    with open('./5.input', 'r') as f:
        lines = f.read().splitlines()

    ids = set()

    for line in lines:
        row_code = line[:7]
        column_code = line[7:]

        row_num = bin_search(list(range(128)), row_code)
        column_num = bin_search(list(range(8)), column_code)

        uniq_id = row_num * 8 + column_num
        ids.add(uniq_id)

    print('max id is', max(ids))

    seat_ids_range = range(max(ids))
    for seat_id in seat_ids_range:
        if (seat_id not in ids) and (seat_id-1 in ids) and (seat_id+1 in ids):
            print('my seat is', seat_id)
            break
