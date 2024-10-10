def get_max_len(N, K, lengths):
    left, right = 0, 10 ** 7
    while left < right:
        index = (left + right + 1) // 2
        if sum([length // index for length in lengths]) >= K:
            left = index
        else:
            right = index - 1
    return left


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
print(get_max_len(n, k, arr))

