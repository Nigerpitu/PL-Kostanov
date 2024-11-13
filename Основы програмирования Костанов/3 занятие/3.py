a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))
ans = []
if 1 <= a <= 3:
    ans.append(a)
if 1 <= b <= 3:
    ans.append(b)
if 1 <= c <= 3:
    ans.append(c)

print(*ans)
