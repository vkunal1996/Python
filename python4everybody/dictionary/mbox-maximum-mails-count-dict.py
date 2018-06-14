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
            mycount[words[1]]=mycount.get(words[1],0)+1
#Histogram
print(mycount)
mylist=list(mycount.keys())
mylist.sort()
#sorted List
for key in mylist:
    print(key,mycount[key])
            
#maximum of all the messages
maximum=0
maximumkey=' '
for key,value in mycount.items():
    if value>maximum:
        maximum=value
        maximumkey=key
print(maximumkey,maximum)
