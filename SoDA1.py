# Дают n отрезков (1 <= n <= 1e5).  Каждый отрезок это два числа l, r (1 <= l <= r <= 1e5).
# Для каждого натурального числа x которое состоит хотя-бы в одном отрезке, 
# посчитать в скольких отрезках содержится число x. 

n = int(input())

count_dict = {}

for i in range(n):
    l, r = input().split()
    for number in range(int(l), int(r)+1):
        count_dict[number] = count_dict.get(number, 0) + 1
print()

for key, value in count_dict.items():
    print(key, value)
    