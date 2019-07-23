import argparse

SPACE = ' '

"""
    Author = Jacob Garrison
    Passphrase = Jefferson

    shoutLetters - prints all characters within words of a phrase
    separated by a character (we'll start with a space, but later allow
    the option to specify the character used as a separator from the command line.
    Whitespace and punctuation are not printed with a hypen separator.
"""

def shoutLetters(phrase,sep):

    phrase = phrase.upper() # really shout out loud
    x = 1
    skipSep = False       # state variable
    print(phrase[0],end="")
    phrase = phrase[x] # finished with first character
    if phrase == ' ':
        print(phrase, end="")
    elif phrase.isalnum == True:
        print(phrase, sep, end="")
    else:
        print(phrase, sep, end="")
        x += 1
    
    #FIXME (define a loop structure to interleave the separator (sep) between letters
    # in a word.

    print()


if __name__ == "__main__":

    sep = SPACE
    parser = argparse.ArgumentParser(description="Shout Letters")
    parser.add_argument("phrase", type=str, help="Enter a phrase to shout")

    """
        Add an optional command line argument to specify which character to use as
        a separator.
    """


    args = parser.parse_args()

    shoutLetters(args.phrase, sep)
