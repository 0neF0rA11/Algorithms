def is_increasing(lst):
    for i in range(1, len(lst)):
        if lst[i-1] >= lst[i]:
            return "NO"
    return "YES"


lst = list(map(int, input().split()))
print(is_increasing(lst))
