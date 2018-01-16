import string
sentence=raw_input('Enter Sentence:')
newsentence=''
for ch in sentence:
    if ch.isalpha():
        newsentence=newsentence+ch
    

palindrome=newsentence[::-1]

if palindrome.lower()==newsentence.lower():
    print 'Palindrome'
else:
    print 'Not Palindrome'
    
