import random
print('I am thinking of Number 1 and 20')
number=random.randint(1,20)
guessNumber=0
counter=0
while counter<=6:
    print('Take a guess')
    guessNumber=int(input())
    counter+=1
    if(guessNumber==number):
        print('You Guess the Number Correct in '+str(counter)+' turns')
        break
    elif(guessNumber<number):
        print('Your Guess is too low')
    elif(guessNumber>number):
        print('Your Guess is too high')

    if counter==6:
        print('You Failed to Guess the Number in 6 turns')
        print('Number was '+str(number))
        break
