def easy_way(str1, str2):
    numbers1 = set(map(int, str1.split()))
    numbers2 = set(map(int, str2.split()))
    return ' '.join(map(str, numbers1 & numbers2))


str1 = input()
str2 = input()
print(easy_way(str1, str2))

