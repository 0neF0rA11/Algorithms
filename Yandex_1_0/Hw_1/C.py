import re

def get_clear_number(number):
    number = number.replace("+7", "8")
    number = re.sub(r'|\-|\(|\)', '', number)
    if len(number) == 11:
        return number
    return "8495" + number


new_number = get_clear_number(input())
for i in range(3):
    number = get_clear_number(input())
    print("YES") if new_number == number else print("NO")
