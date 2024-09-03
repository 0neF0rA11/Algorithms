def get_count_mean(row):
    count = 0
    for i in range(1, len(row)-1):
        if row[i-1] < row[i] > row[i+1]:
            count += 1
    return count


line = list(map(int, input().split()))
print(get_count_mean(line))
