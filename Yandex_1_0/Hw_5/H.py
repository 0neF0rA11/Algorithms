def find_longest_substring(n, k, string):
    char_count = {letter: 0 for letter in 'qazwsxedcrfvtgbyhnujmikolp'}
    right = 0
    max_length = -10**9
    starting_position = 0
    
    for left in range(n):
        while right < n and char_count[string[right]] < k:
            char_count[string[right]] += 1
            right += 1
        if right - 1 - left > max_length:
            max_length = right - 1 - left
            starting_position = left + 1
        char_count[string[left]] -= 1
    return max_length + 1, starting_position


n, k = map(int, input().split())
input_string = input()
result_length, starting_index = find_longest_substring(n, k, input_string)
print(result_length, starting_index)
