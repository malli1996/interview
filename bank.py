netamount = 0
while True:
    s = input('enter some:')
    if not s:
        break
    values = s.split(' ')
    operation = values[0]
    amount =int(values[1])
    if operation == 'd':
        netamount+=amount
    elif amount == 'w':
        netamount-=amount
    else:
        pass
print(netamount)
    
