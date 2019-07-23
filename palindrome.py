def palindrome(word):
    ct1 = 0
    ct2 = -1
    while ct1 < (len(word)/2):
        if len(word) < 2:
            return True
        elif word[ct1] == word[ct2]:
            ct1 += 1
            ct2 -= 1
            return True
        else:
            return False
