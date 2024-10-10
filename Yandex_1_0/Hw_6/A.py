def binary_search(item, row):
    if len(row) == 0:
        return "NO"
    left, right = 0, len(row)
    while left != right:
        index = (right + left) // 2
        if row[index] > item:
            right = index
        elif row[index] < item:
            left = index + 1
        else:
            return "YES"

    return 'YES' if left < len(row) and row[left] == item else "NO"


n, k = map(int, input().split())
lst1 = sorted(list(map(int, input().split())))
lst2 = list(map(int, input().split()))

for item in lst2:
    print(binary_search(item, lst1))

