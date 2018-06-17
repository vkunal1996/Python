import re
import string
filename=input('Enter the Filename ')
try:
    f=open(filename)
except:
    print('Filename do not exists ')
    exit()
count=0
SUM=0.0
for line  in f:
    x=re.findall('^N.*: ([0-9.]+)',line)
    if len(x)>0:
        SUM=SUM+float(x[0])
        count=count+1
print('Average is ',round(SUM/count,7))
            
