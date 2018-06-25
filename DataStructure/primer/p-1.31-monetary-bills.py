try:
    message=''
    monetary_charged=round(float(input('Enter the Charged Amount ')),0)
    print(monetary_charged)
    monetary_given=round(float(input('Enter the Given Amount')),0)
    if monetary_charged>monetary_given:
        raise ValueError('Insufficient amount Deposited')
except ValueError as e:
    print(e)
    exit()
denomonitions=list()
denominitions=[2000,500,200,100,50,20,10,5,2,1]

monetary_to_return=monetary_given-monetary_charged
currency_dictionary=dict()
for currency in denominitions:
    remainder=int(monetary_to_return / currency)
    if remainder == 0:
        continue
    currency_dictionary[currency]=remainder
    monetary_to_return-=remainder*currency
returnlist=list()
for key,value in list(currency_dictionary.items()):
    returnlist.append((key,value))
    
returnlist.sort(reverse=True)
for denom,value in returnlist:
    print('Returning : ',value,' currency not of ',denom)
    
