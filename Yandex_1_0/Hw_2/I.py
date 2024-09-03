def create_game_field(N, M, points):
    field = [[0 for i in range(M)] for i in range(N)]

    for x, y in points:
        x -= 1
        y -= 1
        field[x][y] = '*'
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and field[nx][ny] != '*':
                    field[nx][ny] += 1

    str_field = '\n'.join(' '.join(map(str, line)) for line in field)

    return str_field


N, M, K = map(int, input().split())

points = []
for _ in range(K):
    points.append(tuple(map(int, input().split())))

print(create_game_field(N, M, points))
