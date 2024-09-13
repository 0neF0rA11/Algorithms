def word_occurrences(text):
    word_dict = {}
    result = []

    for word in text:
        if word not in word_dict:
            word_dict[word] = 0
        result.append(str(word_dict[word]))
        word_dict[word] += 1

    return ' '.join(result)


with open('input.txt', 'rt', encoding='utf-8') as file:
    text = file.read().split()

output_string = word_occurrences(text)
print(output_string)
