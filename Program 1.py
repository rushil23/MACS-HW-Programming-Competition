#Program1

#Min and Max
try:
    while True:
        n=input("Enter Number: ")
except :
    print 'Enter a numeric value'
max=min=n
status=0
if n==0:
    status=1
    print "The first number you entered itself is 0 and hence there is no highest or lowest number to display, since 0 is the termination point"
while n!=0:
    n=input("Enter Number: ")
    if n>max and n!=0:
        max=n
    elif n<min and n!=0:
        min=n

if status!=1:
    print "The Largest Number from the sequence of numbers entered: ",max
    print "The Smallest Number from the sequence of numbers entered: ",min
