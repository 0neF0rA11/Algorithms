def calculate_combinations(n, k, arr):
    frequency_count = {}
    for number in arr:
        frequency_count[number] = frequency_count.get(number, 0) + 1
    unique_numbers = sorted(frequency_count.keys())
    right_pointer = 0
    total_combinations = 0
    duplicate_count = 0

    for left_pointer in range(len(unique_numbers)):
        while right_pointer < len(unique_numbers) and unique_numbers[left_pointer] * k >= unique_numbers[right_pointer]:
            if frequency_count[unique_numbers[right_pointer]] > 1:
                duplicate_count += 1
            right_pointer += 1
        range_length = right_pointer - left_pointer
        if frequency_count[unique_numbers[left_pointer]] > 1:
            total_combinations += (range_length - 1) * 3
        if frequency_count[unique_numbers[left_pointer]] > 2:
            total_combinations += 1
        total_combinations += (range_length - 1) * (range_length - 2) * 3
        if frequency_count[unique_numbers[left_pointer]] > 1:
            duplicate_count -= 1
        total_combinations += duplicate_count * 3

    return total_combinations


n, k = map(int, input().split())
array = list(map(int, input().split()))
result = calculate_combinations(n, k, array)
print(result)
