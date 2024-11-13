s = input()

new_s = s.replace('а','').replace("А",'')
count = len(s) - len(new_s)

print("Изменный текст", new_s)
print("Количество удаленных символов",count)