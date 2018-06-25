
try:
    num=input('Enter the Integer greater than 2')
    temp=num
    if num<2:
        raise ValueError('Number is less then 2')
except ValueError(message):
    print(message)
    exit()
count=0
while True:
    if num==0:
       print('0 can be divided by 2 0 times')
    else:
        num//=2
        #print(num)
        if num>=2:
            count+=1
        else:
            break
print(temp,'can be dividied by 2 before getting number<2 is ',count)
        
        
        
        
