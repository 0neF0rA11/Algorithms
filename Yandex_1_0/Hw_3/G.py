def counting_truth_turtles(count_turtles, answers):
    result = 0
    turtle_set = set()

    for answer in answers:
        ahead, behind = map(int, answer.split())
        if abs(ahead) + 1 + abs(behind) == count_turtles and (ahead, behind) not in turtle_set:
            turtle_set.add((ahead, behind))
            result += 1
    return result


count_t = int(input())
answers = []
for i in range(count_t):
    answers.append(input())
print(counting_truth_turtles(count_t, answers))
