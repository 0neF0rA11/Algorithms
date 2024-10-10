def approximate_number(number, row):
    if len(row) == 0:
        print("Not row")

    left, right = 0, len(row) - 1
    while left < right:
        index = (left + right + 1) // 2
        if row[index] <= number:
            left = index
        else:
            right = index - 1

    if abs(number - row[left]) <= abs(number - row[min(left + 1, len(row) - 1)]):
        return row[left]
    else:
        return row[left+1]


n, k = map(int, input().split())
lst1 = sorted(list(map(int, input().split())))
lst2 = list(map(int, input().split()))

for item in lst2:
    print(approximate_number(item, lst1))
