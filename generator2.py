def Givenumber(n):
    i = 0
    while i<n:
        j = i
        i = i+1
        if j%7 == 0:
            yield j
for i in Givenumber(100):
    print(i)
