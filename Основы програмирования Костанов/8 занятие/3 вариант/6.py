def sorts(s):
    words = s.split()
    s_words = [''.join(sorted(word)) for word in words]
    return ' '.join(s_words)


a = input()
print(sorts(a))
