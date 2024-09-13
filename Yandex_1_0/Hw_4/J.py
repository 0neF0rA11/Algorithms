def process_file(n, c, d, key_set, text):
    symbols = set('0123456789qazwsxedcrfvtgbyhnujmikoplQAZWSXEDCRFVTGBYHNUJMIKOLP_')

    ident = {}
    temp = []
    for sym in text:
        if sym in symbols:
            temp.append(sym)
        else:
            if temp:
                if d == 'no' and temp[0].isdigit():
                    temp.clear()
                    continue

                idr = ''.join(temp)

                if c == 'no':
                    idr = idr.lower()
                if idr in key_set:
                    temp.clear()
                    continue
                if idr.isdigit():
                    temp.clear()
                    continue
                
                ident[idr] = ident.get(idr, 0) + 1
                temp.clear()

    max_value = max(ident.values())

    for k, v in ident.items():
        if v == max_value:
            return k


with open('input.txt', 'rt', encoding='utf-8') as file:
    n, c, d = file.readline().rstrip().split()

    if c == 'no':
        key_set = {file.readline().rstrip().lower() for _ in range(int(n))}
    else:
        key_set = {file.readline().rstrip() for _ in range(int(n))}

    text = file.read()

result = process_file(n, c, d, key_set, text)
print(result)
