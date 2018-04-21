#Simplest Impossible Maths
def collatz(number):
    if number % 2 == 0:
        return int(number//2)
    elif number % 2 ==1:
        return int(3*number+1)
print('Enter the Number')
myNumber=int(input())
while True:
    myNumber=collatz(myNumber)
    print(myNumber)
    if(myNumber==1):
        break
