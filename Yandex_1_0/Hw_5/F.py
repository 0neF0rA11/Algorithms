def calculate_sum(n, power_list, m, price_list):
    power_list = list(map(int, power_list.split()))
    power_list = sorted(power_list)
    price_list = sorted(price_list, key=lambda x: (x[1], x[0]))

    amount = 0
    left = 0
    for power in power_list:
        while price_list[left][0] < power:
            left += 1
        amount += price_list[left][1]

    return amount


n = int(input())
power_list = input()
m = int(input())
price_list = []
for i in range(m):
    price_list.append(list(map(int, input().split())))
print(calculate_sum(n, power_list, m, price_list))
