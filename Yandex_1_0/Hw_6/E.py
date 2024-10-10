def correcting_scoring(a, b, c):
    left, right = 0, a + b + c
    while left < right:
        count = (left + right) // 2
        amount = a + b + c + count
        if (2 * a + 3 * b + 4 * c + 5 * count) / amount >= 3.5:
            right = count
        else:
            left = count + 1
    return left


a, b, c = int(input()), int(input()), int(input())
print(correcting_scoring(a, b, c))
