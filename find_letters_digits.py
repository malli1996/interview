x = input('enter a string and number:')
d = {'letters':0,'digit':0}
for s in x:
    if s.isdigit():
        d['digit']+=1
    elif s.isalpha():
        d['letters']+=1
    else:
        pass
print('letters:',d['letters'])
print('digits:',d['digit'])
