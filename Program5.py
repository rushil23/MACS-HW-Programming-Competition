def maximum(a):
    max=a[0]
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]

        

    return [max,i]
def average(L):
    n=len(L)
    sum=0
    for i in range(n):
        sum+=L[i]
    avg=sum/float(n)
    yield avg

        
def main():
    f=open('stats.txt','r')
    line=f.readline()
    word=line.split()
    m=int(word[0])
    n=int(word[1])
    R=[[0 for j in range(n)]for i in range(m)]
    lines=f.readlines()
    for i in range(m):
        for j in range(n):
            for line in lines:
                words=line.split()
                for word in words:
                    for k in range(len(word)):
                        R[i][j]=int(word[k])

    
    for i in range(m):
        for j in range(n):
            print R[i][j],
        print

    avgTrial=avgSub=[]
    #Trial Average
    for i in range(m):
        avgTrial.append(average(R[i]))
    #Sub Average
    for j in range(n):
        trial=[]
        for i in range(m):
            trial.append(R[i][j])
        avgSub.append(average(trial[j]))
    maxa=max1()
    print avgSub, maxa
    print avgTrial, maxb
        
main()
    
        

        

    
        
        
                        
    
        
