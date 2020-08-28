#!/usr/bin/python
def pigl(word):
    vowels='aeiou'
    if (vowels.find(word[0]) == -1):
        print('Starts with constanent')
        return word[1:] + word[0] + 'ay'
    else:
        print('Starts with a vowel')
        return word + 'way'


if __name__ == "__main__":

    convword = pigl('pig')
    print(convword)
