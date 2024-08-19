A, B, C = int(input()), int(input()), int(input())
D, E = int(input()), int(input())

min_side_1 = min(A, B, C)
min_side_2 = A + B + C - max(A, B, C) - min_side_1

if min_side_1 <= min(D, E) and min_side_1 <= max(D, E):
    print("YES")
else:
    print("NO")
