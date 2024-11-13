text = input()

words = text.split()

count = 0

for word in words:
    if word.lower().startswith("е"):
        count += 1

print(count)