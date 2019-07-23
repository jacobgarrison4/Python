"""
Substitution Cipher
CIS 210 F17 Project 4

Authors: Jacob Garrison

Credits: Python Programming in Context

Encrypts and decrypts a plain text message.
"""

def main():
    message = input("Message: ")
    password = input("Password: ")
    encryption = substitutionEncrypt(message, password)
    print(encryption)
    decryption = substitutionDecrypt(encryption, password)
    print(decryption)

def removeDupes(myString):
    """(str) -> str

    Removes duplicate characters.

    >>> removeDupes('topsecret')
    'topsecr'
    >>> removeDupes('hello world')
    'helo wrd'
    """
    newStr = ''
    for ch in myString:
        if ch not in newStr:
            newStr += ch
    return newStr

def removeMatches(myString, removeString):
    """(str, str) -> str

    Removes all matching characters that
    are in removeString from myString.

    >>> removeMatches('abcdefghijklmnopqrstuvwxyz', 'topsecr')
    'abdfghijklmnquvwxyz'
    """
    newStr = ''
    for ch in myString:
        if ch not in removeString:
            newStr += ch
    return newStr

def genKeyFromPass(password):
    """(str) -> str

    Generates a key from a password.

    >>> genKeyFromPass('ajax')
    'ajxyzbcdefghiklmnopqrstuvw'
    """
    key = 'abcdefghijklmnopqrstuvwxyz'
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], password)
    beforeString = removeMatches(key[:lastIdx], password)
    key = password + afterString + beforeString
    return key

def substitutionEncrypt(plainText, psw):
    """(str, str) -> str

    Encrypts a message and returns the cipherText.

    >>> substitutionEncrypt('the quick brown fox', 'ajax')
    'qdznrexgjoltkblu'
    """
    key = genKeyFromPass(psw)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plainText = plainText.replace(' ', '')
    cipherText = ''
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText += key[idx]
    return cipherText


def substitutionDecrypt(cipherText, psw):
    """(str, str) -> str

    Decrypts a cipherText and returns original message.

    >>> substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'
    """
    key = genKeyFromPass(psw)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plainText = ''
    for ch in cipherText:
        idx = key.find(ch)
        plainText += alphabet[idx]
    return plainText

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    
main()
