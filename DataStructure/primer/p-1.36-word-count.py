import string
try:
    filename=input('Enter the File Name to Open')
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
        makeDictionary[word]=makeDictionary.get(word,0)+1
frequencyList=list()
for word,frequency in list(makeDictionary.items()):
    frequencyList.append((word,frequency))
frequencyList.sort()
for word ,frequency in frequencyList:
    print(word,' appeared ',frequency)

            
