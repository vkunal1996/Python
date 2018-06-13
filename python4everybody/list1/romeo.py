try:
    filename=input('Please Enter the Filename ')
    fileOpener=open(filename)
    newWordList=[]
    for lines in fileOpener:
        words=lines.split()
        for i in range(len(words)):
            if words[i] in newWordList:
                continue
            else:
                newWordList.append(words[i])
    newWordList.sort()
    print(newWordList)
except:
    print('FileName don'//'t Exists')
