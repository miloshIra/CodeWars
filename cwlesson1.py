def getCountwrong(asd): #!WRONG
    num=0
    for i in asd:
        if i ==('a,e,o,u,i'):
            num=(num+1)
    return num
    print(num)

  # This is wrong, use "in" instead of "==" with no brackets and no ,.

def getCount(asd): # !RIGHT
    num=0

    for i in asd:
        if i in 'aeoiu':
            num=(num+1)
    print(num) # or return(num)

getCount('asdasdasdasdadsa')
