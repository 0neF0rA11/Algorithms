def find_temperature_range(n, initial_temp, measurements):
    left = 30.0
    right = 4000.0
    prev = initial_temp

    for i in range(n - 1):
        new_temp, direction = measurements[i]
        if direction == 'closer':
            if new_temp < prev:
                right = min(right, (new_temp + prev) / 2)
            else:
                left = max(left, (new_temp + prev) / 2)
        else:  # direction == 'further'
            if new_temp > prev:
                right = min(right, (new_temp + prev) / 2)
            else:
                left = max(left, (new_temp + prev) / 2)
        prev = new_temp

    return left, right

n = int(input())
initial_temp = float(input())
measurements = [input().strip().split() for _ in range(n-1)]
measurements = [(float(temp), direction) for temp, direction in measurements]

left, right = find_temperature_range(n, initial_temp, measurements)
print(left, right)