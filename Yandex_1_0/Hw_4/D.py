def keyboard_work(durability_str, sequence_push):
    durability_list = list(map(int, durability_str.split()))
    sequence_push_list = list(map(int, sequence_push.split()))
    for key in sequence_push_list:
        durability_list[key-1] -= 1

    for durability in durability_list:
        if durability >= 0:
            print("NO")
        else:
            print("YES")


n = int(input())
ds = input()
k = int(input())
sp = input()
keyboard_work(ds, sp)
