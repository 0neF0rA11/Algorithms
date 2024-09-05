def number_colors(N, M, colors):
    colors_A = set(colors[:N])
    colors_B = set(colors[N:])

    common_colors = colors_A & colors_B
    unique_A = colors_A - colors_B
    unique_B = colors_B - colors_A

    print(len(common_colors))
    print(*sorted(common_colors))
    print(len(unique_A))
    print(*sorted(unique_A))
    print(len(unique_B))
    print(*sorted(unique_B))


N, M = map(int, input().split())

colors = []
for i in range(N + M):
    colors.append(int(input()))

number_colors(N, M, colors)
