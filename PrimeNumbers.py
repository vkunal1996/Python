i=2
j=2
flag=False
while i<=100:
    flag=False
    j=2
    while j<=i/2:
        if i%j==0:
            flag=True
            break
        j+=1
    if flag==False:
        print (i)
    i+=1
