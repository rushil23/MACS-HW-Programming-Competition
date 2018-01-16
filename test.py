def oddNumbers(l,r):
    L=list()
    for i in range(l,(r+1),1):
        if i%2!=0:
            L.append(i)
    return L

print oddNumbers(3,9)
