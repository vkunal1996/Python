readingfile=input('Enter the Filename from where you want to Read Content: ')
writingfile=input('Enter the Summary File where you want to write : ')
try:
    fileopen=open(readingfile)
    filewrite=open(writingfile,'w')
except:
    print('File with',readingfile,'do not exist')

countvowel=0
countconsonent=0
for  myline in fileopen:
    length=len(myline)
    line=myline.lower()
    i=0
    while i<=length-1:
        if line[i]=='a' or line[i]=='i' or line[i]=='e' or line[i]=='o' or line[i]=='u':
            countvowel=countvowel+1
        elif line[i]>=chr(97) and line[i]<=chr(122):
            countconsonent=countconsonent+1
            
        i=i+1

Stringvowel='The number of Vowels in %s are %d'%(readingfile,countvowel)
Stringconsonent='The number of Consonents in %s are %d'%(readingfile,countconsonent)
filewrite.write(Stringvowel)
filewrite.write(Stringconsonent)

fileopen.close()
filewrite.close()
