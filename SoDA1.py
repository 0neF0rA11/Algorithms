# Дают n отрезков (1 <= n <= 1e5).  Каждый отрезок это два числа l, r (1 <= l <= r <= 1e5).
# Для каждого натурального числа x которое состоит хотя-бы в одном отрезке, 
# посчитать в скольких отрезках содержится число x. 

n = int(input())
count_list = [0]*int(1e5)

for i in range(n):
    l, r = input().split()
    count_list[int(l)] += 1
    count_list[int(r)+1] -= 1

for i in range(len(count_list)):
    count_list[i] += count_list[i-1]

print()
for i in range(len(count_list)):
    if count_list[i] > 0:
        print(i, count_list[i])

# Изначальная сложность была O(n*n), нынешняя O(n+m)
