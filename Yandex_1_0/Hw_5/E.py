def calculate_min_row(N, K, row):
    row = list(map(int, row.split()))

    min_len, mleft, mright = N, 1, N
    trees_list = [0 for i in range(K+1)]

    left, right = 0, 0
    unique_trees = 0

    while right < N or unique_trees == K:
        if unique_trees == K:
            cur_len = right - left
            if cur_len < min_len:
                mleft = left + 1
                mright = right
                min_len = cur_len

            trees_list[row[left]] -= 1
            if trees_list[row[left]] == 0:
                unique_trees -= 1
            left += 1
        else:
            if right < N:
                if trees_list[row[right]] == 0:
                    unique_trees += 1
                trees_list[row[right]] += 1
                right += 1
            else:
                break
    return mleft, mright


n, k = map(int, input().split())
row = input()
print(*calculate_min_row(n, k, row))
