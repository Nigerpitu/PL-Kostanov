s = input().strip()
seredin = len(s)//2

s1 = s[:seredin]
s2 = s[seredin:]

print(s1)
print(s2)

s2_new = s2.replace("п",'').replace("П",'')

print("Изменная строка", s2_new)
