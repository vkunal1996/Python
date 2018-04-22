animal={'dog':'black',
        'cat':'black',
        'horse':'black'
        }
while True:
    print('Enter the Animal Name ')
    name=input()
    if name=='':
        break
    if name in animal:
        print('We have '+name+' in '+animal[name]+' color')
    else:
        print('We do not have requested animal')
        print('please Enter the Color you Need')
        color=input()
        animal[name]=color
