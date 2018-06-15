filename=input('Enter the File Name to Open ')
try:
    filehand=open(filename)
except:
    print('File do not exists ')
    exit()
mailDictionary=dict()
for line in filehand:
    if line.startswith('From'):
        words=line.split()
        if len(words)>=6:
            time=words[5].split(':')
            mailDictionary[time[0]]=mailDictionary.get(time[0],0)+1
mynewlist=list()
for hours,value in list(mailDictionary.items()):
    mynewlist.append((hours,value))
mynewlist.sort()
for hours,value in mynewlist:
    print(hours,' ',value)
