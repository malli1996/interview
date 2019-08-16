l = []
while True:
    s = input('enter the sentence:')
    if s:
        l.append(s.upper())
    else:
        break
for sentence in l:
    print(sentence)
