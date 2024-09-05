def count_shots(count_birds, bird_coords):
    bird_coords = [tuple(coord.split()) for coord in bird_coords]
    return len({x for x, y in bird_coords})


count_birds = int(input())
coords = []
for i in range(count_birds):
    coords.append(input())
print(count_shots(count_birds, coords))
