#Project 3.2 Pin
#Jacob Garrison
#alphapinEncode takes a pin of whatever length and converts it into a
#string of letters.

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z']



def alphapinEncode_stub(pin):
    '''
    (num) -> (str)

    alphapinEncode takes a pin and converts it into a memorable string

    >>>alphapinEncode(4327)
    'lohi'
    >>>alphapinEncode(1298)
    'dizo'
    >>>alphapinEncode(3463470)
    'bomejusa'
    '''
    letters = ''
    origpin = pin
    while pin > 0:
        num = pin%100

        v1 = vowels[num%5]
        c1 = consonants[num//5]
        letters += (v1+c1)
        a = list(letters)
        a.reverse()
        b = ''.join(a)

        
        pin = pin//100
    pass 
    print('Encoding of',origpin,'is',b)

def alphapinEncode(pin):
    '''
    (num) -> (str)

    alphapinEncode takes a pin and converts it into a memorable string

    >>>alphapinEncode(4327)
    'lohi'
    >>>alphapinEncode(1298)
    'dizo'
    >>>alphapinEncode(3463470)
    'bomejusa'
    '''
    letters = ''
    origpin = pin
    while pin > 0:
        num = pin%100

        v1 = vowels[num%5]
        c1 = consonants[num//5]
        letters += (v1+c1)
        a = list(letters)
        a.reverse()
        b = ''.join(a)

        
        pin = pin//100 
    print('Encoding of',origpin,'is',b)
