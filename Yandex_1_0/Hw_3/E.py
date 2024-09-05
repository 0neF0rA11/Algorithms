def count_min_but(buttons, number):
    buttons_set = set(buttons.split())
    number_set = set(list(number))

    return len(number_set - buttons_set)


buttons = input()
number = input()
print(count_min_but(buttons, number))
