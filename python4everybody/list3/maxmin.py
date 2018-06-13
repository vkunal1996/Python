myNumberList=[]
while True:
    try:
        number=input('Input Value ')
        if number=='done':
            break
        temp=int(number)
        myNumberList.append(temp)
    except:
        print('Invalid Input ')
print('Maximum of ',myNumberList,' is ',max(myNumberList))
print('Minimum of ',myNumberList,' is ',min(myNumberList))
