from sys import stdin


def find_anagram_occurrences():
    g, s = map(int, stdin.readline().strip().split())
    w = stdin.readline().rstrip()
    seq = stdin.readline().rstrip()

    result = 0

    main_key = {}
    for char in w:
        if char not in main_key:
            main_key[char] = 0
        main_key[char] += 1

    window_dict = {}
    for char in seq[:g]:
        if char not in window_dict:
            window_dict[char] = 0
        window_dict[char] += 1

    matches = 0
    for k in main_key:
        if k in window_dict and main_key[k] == window_dict[k]:
            matches += 1

    if matches == len(main_key):
        result += 1

    ind = 0
    for char in seq[g:]:
        temp = seq[ind]
        if temp in main_key and main_key[temp] == window_dict[temp]:
            matches -= 1
        window_dict[temp] -= 1
        if temp in main_key and main_key[temp] == window_dict[temp]:
            matches += 1

        if char not in window_dict:
            window_dict[char] = 0
        if char in main_key and main_key[char] == window_dict[char]:
            matches -= 1
        window_dict[char] += 1
        if char in main_key and main_key[char] == window_dict[char]:
            matches += 1

        if matches == len(main_key):
            result += 1
        ind += 1

    print(result)


find_anagram_occurrences()
