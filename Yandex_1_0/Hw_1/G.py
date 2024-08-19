def get_details_count():
    N, K, M = map(int, input().split())
    if N < K or K < M:
        return 0

    details_count = 0

    while True:
        count_K = N // K
        if count_K == 0:
            return details_count
        N = N % (K * count_K)
        details = count_K * (K // M)
        details_count += details
        N += (K - ((K // M) * M)) * count_K


print(get_details_count())
