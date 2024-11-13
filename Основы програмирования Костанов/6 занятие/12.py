s = input().split()

count_word = ""


for i in s:
    new_i = i.strip(",.!?")
    if new_i.endswith('я') or new_i.endswith('Я'):
        count_word += i + ' '

print(count_word.strip())



