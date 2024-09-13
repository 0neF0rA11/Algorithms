def build_pyramid(count, size_list):
    max_height_dict = {}

    for size in size_list:
        x, y = map(int, size.split())
        max_height_dict[x] = max(max_height_dict.get(x, y), y)

    return sum(max_height_dict.values())


n = int(input())
size_list = []
for i in range(n):
    size_list.append(input())
print(build_pyramid(n, size_list))
