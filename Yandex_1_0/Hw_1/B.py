def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a) \
            and (a > 0 and b > 0 and c > 0):
        return "YES"
    return "NO"


a = int(input())
b = int(input())
c = int(input())
print(is_triangle(a, b, c))
