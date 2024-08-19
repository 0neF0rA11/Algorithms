def get_result(a, b, c):
    if (c < 0) or (a == 0 and b != c * c):
        return "NO SOLUTION"
    if (a == 0 and b == c * c):
        return "MANY SOLUTIONS"

    x = int((c * c - b) / a)
    if a * x + b != c * c:
        return "NO SOLUTION"
    return x


a, b, c = int(input()), int(input()), int(input())
print(get_result(a, b, c))
