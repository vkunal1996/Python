filename=input('Enter the File Name to Open ')
try:
    filehand=open(filename)
except:
    print('File do not exists ')
    exit()
mailDictionary=dict()
for line in filehand:
    if line.startswith('From'):
       # print(line)
        words=line.split()
        #mailDictionary[words[1]]=mailDictionary.get(words[1],0)+1
        if len(words)>2:
            if words[1] not in mailDictionary:
                mailDictionary[words[1]]=1
            else:
                mailDictionary[words[1]]+=1
mynewlist=list()
for key,val in list(mailDictionary.items()):
    mynewlist.append((val,key))
mynewlist.sort(reverse=True)
print(mynewlist[0])

#print(mailDictionary)
