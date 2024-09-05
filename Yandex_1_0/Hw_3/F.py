def calculate_degree_proximity(first, second):
    second_set = {second[ind] + second[ind + 1] for ind in range(len(second) - 1)}
    result = 0

    for ind in range(len(first) - 1):
        pair = first[ind] + first[ind + 1]
        if pair in second_set:
            result += 1

    return result


first_genome = input()
second_genome = input()
print(calculate_degree_proximity(first_genome, second_genome))