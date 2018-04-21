def collatz(number):
    if number % 2 == 0:
        return int(number//2)
    elif number % 2 ==1:
        return int(3*number+1)
print('Enter the Number')
flag=False
while True:
    try:
        myNumber=int(input())
        while True:
            myNumber=collatz(myNumber)
            print(myNumber)
            if(myNumber==1):
                flag=True
                break
        if flag==True:
            break
    except ValueError:
        print('Please Enter the Integral Value')
