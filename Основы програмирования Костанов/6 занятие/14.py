s = input()


words = s.split()


words_a = ""
words_ya = ""


for i in words:
    if i.startswith('а') or i.startswith('А'):
        words_a += i + " "

    if i.endswith('я') or i.endswith('Я'):
        words_ya += i + " "

print("Слова, начинающиеся на букву а", words_a.strip())
print("Слова, оканчивающиеся на букву я", words_ya.strip())
