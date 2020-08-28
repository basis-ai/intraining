#!/usr/bin/python
def conv(roman):
    numerals={'m': 1000, 'l': 100, 'c': 50, 'x': 10, 'v': 5, 'i':1}
    total=0
    a=numerals.get(roman[0])
    for c in (roman[1:]):
        if numerals.get(c) <= a:
            total += a
        else:
            total -= a
        a=numerals.get(c)
    total += numerals.get(roman[-1])
    return(total)
        


retv=conv('mmmxlviii')
print(retv)
