count=0
temp=0
sumofNumbers=0
while True:
    try:
        a=input()
        
        if a=='done':
            break
        temp=int(a)
        sumofNumbers=sumofNumbers+temp
        count=count+1
        
    except:
        print('Invalid Input')
        
print('Total is ',sumofNumbers,'\n')
print('Count is ',count,'\n')
print('Average is ',float(sumofNumbers/count),'\n')
