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
        apos=line.find('@')
        end=line.find(' ',apos)
        #print(line[apos+1:end])
        mycount[line[apos+1:end]]=mycount.get(line[apos+1:end],0)+1
#Histogram
print(mycount)


