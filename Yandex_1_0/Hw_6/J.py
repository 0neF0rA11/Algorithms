def find_left_median(seq1, seq2):
    L = len(seq1)
    i, j = 0, 0
    for _ in range(L):
        if i < L and (j >= L or seq1[i] <= seq2[j]):
            median = seq1[i]
            i += 1
        else:
            median = seq2[j]
            j += 1
    return median


def process_sequences(sequences):
    n = len(sequences)
    L = len(sequences[0])
    results = []
    for i in range(n):
        for j in range(i + 1, n):
            left_median = find_left_median(sequences[i], sequences[j])
            results.append((i, j, left_median))
    return results


N, L = map(int, input().split())
sequences = [list(map(int, input().split())) for _ in range(N)]

results = process_sequences(sequences)

for i, j, median in results:
    print(median)
