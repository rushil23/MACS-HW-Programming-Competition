line=raw_input('Enter Line of input: ')
line=line.lower()
l=[]
for ch in line:
    if ch not in l:
        l.append(ch)
status=0
for ch in l:
    if ch.isalpha():
        count=0
        for ch1 in line:
            if ch==ch1:
                count+=1
        print ch.upper(),':',count,',',
        status=1
    
if status==0:
    print 'NO ENGLISH CHARACTERS FOUND'
    
        
        
           
            
            
        
            

        
