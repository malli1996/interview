import math
pos = [0,0]
while True:
    s = input('enter directions:')
    if not s:
        break
    number = s.split(' ')
    p = s[0]
    t = int(number[1])
    if p == 'up':
        pos[0]+=t
    elif p == 'down':
        pos[0]-=t
    elif p == 'left':
        pos[1]-=t

    elif p == 'right':
        pos[1]+=t
    else:
        pass
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
