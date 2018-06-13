filename=input('Enter the Filename: ')
try:
    fileopen=open(filename)
except:
    print('File with',filename,'do not exist')
count=0
spam=0
for line in fileopen:
    if line.startswith('X-DSPAM-Confidence:'):
        #line = line.rstrip()
        #print(line)
        count=count+1
        pos=line.find(':')
        end=len(line)-1
        spam=spam+ float(line[pos+1:end])
    else:
        continue
        
print('Average Spam Confidence :',spam/count)
        
