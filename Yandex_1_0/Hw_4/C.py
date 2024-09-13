def find_frequent_word(text):
    word_count = {}
    max_frequent_word = ''
    max_frequent = 0
    for word in text.split():
        frequent = word_count.get(word, 0) + 1
        word_count[word] = frequent
        if frequent >= max_frequent:
            max_frequent_word = word if frequent > max_frequent else min(word, max_frequent_word)
            max_frequent = frequent
    return max_frequent_word


text = input()
print(find_frequent_word(text))
