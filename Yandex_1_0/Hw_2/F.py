def is_symmetrical(seq, additional):
    check = seq + ''.join(additional)
    return check == check[::-1]


def make_symmetric_sequence(seq):
    seq = seq.replace(" ", "")
    count_add = 0
    additional = []

    for i in seq:
        if is_symmetrical(seq, additional):
            return count_add, ' '.join(additional)

        count_add += 1
        additional = [i] + additional
    return count_add, ' '.join(additional)


n = int(input())
sequence = input()
count, add_seq = make_symmetric_sequence(sequence)
print(count)
print(add_seq)
