
word = input().upper()
word_list = []

for i in set(word):
    count = word.count(i)
    word_list.append(count)

if word_list.count(max(word_list)) > 1:
    print('?')
else:
    print(list(set(word))[word_list.index(max(word_list))])
