#Project 4 Pin Decode
#Jacob Garrison
#This project takes a users memorized coded word and converts it back to their pin

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z']


def alphapinDecode(tone):
    '''(str) -> int

    alphapinDecode takes a users memorable
    string and converts it back into the integer
    they started with.

    >>>alphapinDecode('lohi'):
    4327
    >>>alphapinDecode('dizo'):
    1298
    >>>alphapinDecode(''):
    The tone is not in the correct format
    '''
    if tone == '':
        print('The tone is not in the correct format')
    pin = ''
    while len(tone) > 0:
        chs = tone[:2]
        for ch in chs:
            if ch in vowels:
                remainder = vowels.index(ch)
            elif ch in consonants:
                integer = consonants.index(ch)
            
        pin += str((integer * 5) + remainder)
        tone = tone[2:]
    print(int(pin))
