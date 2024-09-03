def get_type():
    IS_CONSTANT = True
    IS_ASCENDING = True
    IS_WEAKLY_ASCENDING = True
    IS_DESCENDING = True
    IS_WEAKLY_DESCENDING = True
    number = int(input())
    while True:

        time_number = int(input())
        if time_number == -2e9:
            break

        if time_number == number:
            IS_DESCENDING = False
            IS_ASCENDING = False

        if time_number > number:
            IS_CONSTANT = False
            IS_DESCENDING = False
            IS_WEAKLY_DESCENDING = False

        if time_number < number:
            IS_CONSTANT = False
            IS_ASCENDING = False
            IS_WEAKLY_ASCENDING = False

        number = time_number

    if IS_CONSTANT:
        return "CONSTANT"
    elif IS_ASCENDING:
        return "ASCENDING"
    elif IS_WEAKLY_ASCENDING:
        return "WEAKLY ASCENDING"
    elif IS_DESCENDING:
        return "DESCENDING"
    elif IS_WEAKLY_DESCENDING:
        return "WEAKLY DESCENDING"
    return "RANDOM"


print(get_type())