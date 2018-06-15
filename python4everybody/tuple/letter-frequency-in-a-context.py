import string
filename=input('Enter the File Name to Open ')
try:
    filehand=open(filename)
except:
    print('File do not exists ')
    exit()
count=0
makeDictionary=dict()
for line in filehand:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        for letter in word:
            if letter>=chr(97) and letter <=chr(122):
                makeDictionary[letter]=makeDictionary.get(letter,0)+1
                count+=1
frequencyList=list()
for letter,frequency in list(makeDictionary.items()):
    frequencyList.append((letter,frequency))
frequencyList.sort()
for letter ,frequency in frequencyList:
    print(letter,' ',round(float(frequency/count*100),2),'%')

            
