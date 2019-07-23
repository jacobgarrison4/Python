vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z']


def Pin(pin):
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
