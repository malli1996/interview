s = input()
words = [x for x in s.split(' ')]
print(' '.join(sorted(list(set(words)))))
