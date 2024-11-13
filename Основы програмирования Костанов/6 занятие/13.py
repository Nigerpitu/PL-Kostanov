s = input()

flag = False

res = ''

for i in s:
    if i == '(':
        flag = True
    elif i == ')':
        flag = False
        break
    elif flag:
        res += i

print(res)