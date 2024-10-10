def get_way(n, coords, c_ways, ways):
    forward_sum = [0]
    for i in range(n-1):
        if coords[i+1][1] > coords[i][1]:
            h = coords[i+1][1] - coords[i][1]
            forward_sum.append(forward_sum[i] + h)
        else:
            forward_sum.append(forward_sum[i])

    back_sum = [0]
    for i in range(n-1, 0, -1):
        if coords[i][1] < coords[i-1][1]:
            h = coords[i-1][1] - coords[i][1]
            back_sum.insert(0, back_sum[0] + h)
        else:
            back_sum.insert(0, back_sum[0])

    for way in ways:
        if way[0] <= way[1]:
            print(forward_sum[way[1]-1] - forward_sum[way[0]-1])
        else:
            left, right = way[0]-1, way[1]-1
            print(back_sum[right] - back_sum[left])


n = int(input())
coords = []
for i in range(n):
    coords.append(tuple(map(int, input().split())))

c_ways = int(input())
ways = []
for j in range(c_ways):
    ways.append(tuple(map(int, input().split())))

get_way(n, coords, c_ways, ways)
