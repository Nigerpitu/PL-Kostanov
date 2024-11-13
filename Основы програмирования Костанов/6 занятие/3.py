s = input()
count = 0

text = ""

for i in s:
    if i == ".":
        count += 1
    else:
        text += i

print(text,"Изменнеая строка")
print(count,"Количество удаленных точек")