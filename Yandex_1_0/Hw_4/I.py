def process_words(n, lines, words):
    dict_set = {}

    for t in lines:
        if t.lower() not in dict_set:
            dict_set[t.lower()] = []
        dict_set[t.lower()].append(t)

    result = 0

    for word in words:
        if word.lower() in dict_set:
            if word not in dict_set[word.lower()]:
                result += 1
        else:
            temp = sum(1 for char in word if char.isupper())
            result += (temp == 0 or temp > 1)

    return result


n = int(input())
lines = [input().rstrip() for _ in range(n)]
words = input().split()

print(process_words(n, lines, words))
