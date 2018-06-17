import re
import string
expression=input('Enter the Command : grep expression filename ')
expressionlist=expression.split(' ')
if expressionlist[0] != 'grep':
    print('Invalid Command')
if not expressionlist[1].startswith('\'') and not expressionlist[1].endswith('\''):
    print('Invalid Expression')
try:
    f=open(expressionlist[2])
except:
    print('Filename do not exists ')
count=0
myexpression=expressionlist[1]
for line in f:
    if re.search(myexpression[1:len(myexpression)-1],line):
        count=count+1
print('There are ',count,' that matched ',expressionlist[1],' in file ',expressionlist[2])
        


            
