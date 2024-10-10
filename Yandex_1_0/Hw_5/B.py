def count_sum_eq_k(N, K, car_num_list):
    car_num_list = list(map(int, car_num_list.split()))
    sum_list = [0]
    for idx in range(len(car_num_list)):
        sum_list.append(sum_list[idx] + car_num_list[idx])

    count_sum = 0
    left = 0
    i = 0
    while i < len(sum_list):
        if sum_list[i] - sum_list[left] == K:
            count_sum += 1
        elif sum_list[i] - sum_list[left] > K:
            left += 1
            continue
        i += 1

    return count_sum


n, k = map(int, input().split())
car_list = input()
print(count_sum_eq_k(n, k, car_list))
