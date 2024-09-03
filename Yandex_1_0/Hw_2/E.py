def get_places(n, results):
    farmer = 0
    winner = 0
    for idx in range(n-1):
        if results[idx] > winner:
            farmer = 0
            winner = results[idx]
            continue

        if results[idx] % 10 == 5 and results[idx+1] < results[idx] and results[idx] > farmer:
            farmer = results[idx]

    if farmer == 0:
        return 0

    place = 1
    for result in results:
        if result > farmer:
            place += 1

    return place


n = int(input())
lst = list(map(int, input().split()))
print(get_places(n, lst))


