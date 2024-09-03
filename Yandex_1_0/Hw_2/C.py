def get_nearest():
    n = int(input())
    row = list(map(int, input().split()))
    x = int(input())

    diff = 2001
    number = 0
    for i in range(n):
        if abs(x-row[i]) < diff:
            diff = abs(x - row[i])
            number = row[i]

    return number


print(get_nearest())
