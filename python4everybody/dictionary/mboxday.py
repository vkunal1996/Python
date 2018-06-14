import string
filename=input('Enter the Filename ')
try:
    filehand=open(filename)
except:
    print('File Do not Exists ')
    exit()
mycount=dict()
for line in filehand:
    if line.startswith('From'):
        words=line.split()
        if len(words)>2:
            mycount[words[2]]=mycount.get(words[2],0)+1
mylist=list(mycount.keys())
mylist.sort()
for key in mylist:
    print(key,mycount[key])
            
