def find_max_product(str):
    nums = list(map(int, str.split()))

    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if min2 * min1 > max1 * max2:
        return f"{min1} {min2}"
    else:
        return f"{max2} {max1}"


str = input()
result = find_max_product(str)
print(result)
