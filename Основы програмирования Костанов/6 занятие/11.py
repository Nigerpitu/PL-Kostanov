s = input()

max_c = 0
cur_c = 0

for i in s:
    if i == 'н' or i == 'Н':
        cur_c += 1
        max_c = max(max_c,cur_c)
    else:
        cur_c = 0


new_s = s.replace("!",".")

print(max_c, new_s)