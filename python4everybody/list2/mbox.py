try:
    filename=input('Please Enter the Filename ')
    fileOpener=open(filename)
    newWordList=[]
    count=0
    for lines in fileOpener:
        if lines.startswith('From:'):
            words=lines.split()
            count=count+1
            print(words[1])
    print('There are',count,' lines in the file starting with From:')
except:
    print('FileName don'//'t Exists')
