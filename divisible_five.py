l = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p,2)
    if not intp%5:
        l.append(p)
print(','.join(l))
