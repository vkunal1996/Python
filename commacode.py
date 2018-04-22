def stringtoReturn(myList):
    mystr=''
    for i in range(0,len(myList)):
        if(i<len(myList)-1):
            mystr+=myList[i]+', '
        elif(i==len(myList)-1):
            mystr+='and '+myList[i]

    return mystr +' are brothers for Life'


myList=['Kunal','Bharpur','Rashiv','Nishant']
print(stringtoReturn(myList))
