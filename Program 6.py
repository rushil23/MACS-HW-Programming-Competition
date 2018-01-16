def anagram(n,q):
    str_n=str(n)
    L=list()
    for i in range(2,10):
        s=n*i
        str_s=str(s)
        status=0
        if len(str_n)==len(str_s):
            for ch in str_n:
                if ch not in str_s:
                    status=1
                    break
            if status==0:
                L.append(i)
    if q==1:
        if L==[]:
            print 'NO'
        else:
            for ch in L:
                print ch,
    elif q==2:
        if L!=[]:
            return True


        
def range_ana():
    for i in range(1000,10000):
        s=str(i)
        L=[]
        for ch in s:
            if ch not in L:
                L.append(ch)
        if len(L)==len(s):
            if anagram(i,2):
                print i
while True:

    check=True
    while check:
        try:
            n=input('Enter number(between 1 and 123456789)-')
            if n>123456789:
                raise ValueError
            check=False
        except:
            print 'Enter numeric value in the given range'
    anagram(n,1)

    print '\nThe anagrams in range 1000 to 9999'
    range_ana()
