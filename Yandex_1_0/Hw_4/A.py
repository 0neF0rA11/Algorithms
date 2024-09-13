def get_symbol(word_list, word):
    word_syno = {word1: word2 for word1, word2 in word_list}
    syno_word = {word2: word1 for word1, word2 in word_list}

    if word in word_syno.keys():
        return word_syno[word]
    elif word in syno_word.keys():
        return syno_word[word]
    else:
        return "Not found"


N = int(input())
words = []
for i in range(N):
    words.append(input().split())
word = input()
print(get_symbol(words, word))