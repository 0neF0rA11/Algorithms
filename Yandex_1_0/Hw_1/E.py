def get_entrance_and_floor(f1, f2, floors):
    floors_before = (f1 - 1) // f2
    entrance = floors_before // floors + 1
    floor = floors_before % floors + 1
    return entrance, floor


def check(k1, m, k2, p2, n2, flat):
    ent, fl = get_entrance_and_floor(k2, flat, m)
    if ent == p2 and fl == n2:
        return get_entrance_and_floor(k1, flat, m)
    return -1, -1


def slow(k1, m, k2, p2, n2):
    ent = -1
    floor = -1
    good_flag = False
    for flat in range(1, 1000001):
        nent, nfloor = check(k1, m, k2, p2, n2, flat)
        if nent != -1:
            good_flag = True
            if ent == -1:
                ent, floor = nent, nfloor
            elif ent != nent and ent != 0:
                ent = 0
            elif floor != nfloor and floor != 0:
                floor = 0
    if good_flag:
        return f"{ent} {floor}"
    else:
        return "-1 -1"


k1, m, k2, p2, n2 = map(int, input().split())
print(slow(k1, m, k2, p2, n2))
