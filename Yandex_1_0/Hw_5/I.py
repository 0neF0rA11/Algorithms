def count_repeating_substrings(k, string):
    total_count = 0
    consecutive_count = 0

    for index in range(k, len(string)):
        if string[index] == string[index - k]:
            consecutive_count += 1
            total_count += consecutive_count
        else:
            consecutive_count = 0

    return total_count


k = int(input())
input_string = input()
result = count_repeating_substrings(k, input_string)
print(result)
