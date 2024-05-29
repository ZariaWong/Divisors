ListIntegers=[]
while len(ListIntegers)<2 or int(ListIntegers[0])>=int(ListIntegers[1]) or int(ListIntegers[0])<1 or int(ListIntegers[1])<1 :
    Integers=str(input('a b: '))
    ListIntegers=str(Integers).split(' ')

k=0
Divisors=[]
while k<=0:
    Divisors=str(input('Divisors: '))
    ListDivisors=str(Divisors).split(' ')
    k=len(ListDivisors)
    if k>0:
      for ii in range(0, len(ListDivisors)):
          ListDivisors[ii] = int(ListDivisors[ii])
      ListUniqSortedDivisors = sorted(set(ListDivisors))
      if (ListUniqSortedDivisors[-1] > int(ListIntegers[-1])) :
        k=0


print('M',end='')
for ii in range(0, len(ListUniqSortedDivisors)):
   print(' ' + str(ListUniqSortedDivisors[ii]),end='')
print()



for k in range(int(ListIntegers[0]),int(ListIntegers[1])):
    print(k,end='')
    for a in range(len(ListUniqSortedDivisors)):
        if k%ListUniqSortedDivisors[a]==0:
            print(' 1',end='')
        else:
            print(' 0',end='')
    print()
