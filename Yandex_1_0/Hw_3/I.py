def find_languages(N, students_language):
    common_languages = set(students_language[0])
    all_languages = set(students_language[0])
    for i in range(1, N):
        common_languages &= set(students_language[i])
        all_languages |= set(students_language[i])

    return (len(common_languages), common_languages), (len(all_languages), all_languages)


N = int(input())
students = []
for i in range(N):
    count = int(input())
    students.append([input() for j in range(count)])

common, all_l = find_languages(N, students)
print(common[0])
print(*common[1], sep='\n', end='\n')
print(all_l[0])
print(*all_l[1], sep='\n', end='\n')
