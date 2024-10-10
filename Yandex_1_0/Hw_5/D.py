def count_pairs(n, lst, r):
    left = 0
    right = 0
    pairs = 0

    while right < n:
        if lst[right] - lst[left] > r:
            left += 1
            pairs += n - right
        else:
            right += 1
    return pairs


n, r = map(int, input().split())
lst = list(map(int, input().split()))
print(count_pairs(n, lst, r))
