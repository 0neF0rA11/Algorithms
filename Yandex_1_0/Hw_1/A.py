def get_temp(tr, tc, mode):
    if mode == 'fan' \
            or (mode == 'heat' and (tr > tc)) \
            or (mode == 'freeze' and (tr < tc)):
        return tr

    return tc


tr, tc = map(int, input().split())
mode = input()
print(get_temp(tr, tc, mode))
