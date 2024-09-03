arr = list(map(int, input().split()))

if len(arr) == 3:
    print(" ".join(map(str, arr)))
else:
    h = max(arr[0], arr[1])
    l = min(arr[0], arr[1])
    h2s = arr[0:2]
    h2 = h2s[0] * h2s[1]
    l2s = h2s
    l2 = h2
    h3s = arr[0:3]
    h3 = h3s[0] * h3s[1] * h3s[2]

    for i in range(2, len(arr)):
        current = arr[i]
        ch2 = current * h2
        cl2 = current * l2
        if ch2 > h3 or cl2 > h3:
            if ch2 >= cl2:
                h3 = ch2
                h3s = h2s + [current]
            else:
                h3 = cl2
                h3s = l2s + [current]

        ch = current * h
        cl = current * l
        if ch > h2 or cl > h2:
            if ch >= cl:
                h2 = ch
                h2s = [h, current]
            else:
                h2 = cl
                h2s = [l, current]

        if ch < l2 or cl < l2:
            if ch < cl:
                l2 = ch
                l2s = [h, current]
            else:
                l2 = cl
                l2s = [l, current]

        if current > h:
            h = current
        if current < l:
            l = current

    print(" ".join(map(str, h3s)))
    