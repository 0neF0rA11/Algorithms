def create_set(string):
    numbers = list(map(int, string.split()))

    number_set = [[] for _ in range(100)]
    len_set = 0

    for number in numbers:
        hash_idx = number % 100

        for now in number_set[hash_idx]:
            if now == number:
                break
        else:
            number_set[hash_idx].append(number)
            len_set += 1

    return len_set


string = input()
print(create_set(string))