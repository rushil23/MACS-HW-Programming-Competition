#Program 3

s1=raw_input('Enter file name 1 - ')
s2=raw_input('Enter file name 2 - ')

def createfile1():
    f=open((s1+'.txt'),'w')
    while True:
        try:
            n=input('Enter number of lines - ')
            break
        except:
            print "Error, you must enter a numeric value only. Please Try Again."
    Lines = range(n)
    for i in range(n):
        Lines[i]=raw_input('Enter line - ')+'\n'
    f.writelines(Lines)
    f.close()

def displayfile1():
    f=open(s1+'.txt','r')
    print '\nFile #1 Content:'
    print f.read()
    Content = f.read()
    f.close()

def copy():
    print "Copying file contents character by character \n"
    f2=open(s2+'.txt','w')
    f1=open(s1+'.txt','r')
    L=f1.read()
    for ch in L:
        f2.write(ch)
    f1.close()
    f2.close()

createfile1()
displayfile1()
copy()

print "The contents of file 2 are:"

f2=open((s2+'.txt'),'r')
print f2.read()
f2.close()
