text = input()

count = 0

text_s = ""

for i in text:
    if i == "а":
        text_s += "о"
        count += 1
    else:
        text_s += i


count2 = len(text_s)


print('Изменнеая строка', text_s)
print('Количесвто замен', count)
print('Количество символов в строке',count2)