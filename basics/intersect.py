#!/usr/bin/python
list1=[2,4,6,7,8,10]
list2=[1,2,3,7]

def inboth(lis1,lis2):
    output=[]
    for i in lis1:
        if i in lis2:
            output.append(i)
    return output

finallist=inboth(list1,list2)
print(finallist)

