#QUES3
int1,int2=map(int,input("enter 2 numbers=").split())
quotient=int1//int2
remainder=int1%int2

#part(a)
print("a.checking if the quotient and remainder is a callable value or not.")
print(callable(quotient))
print(callable(remainder))

#part(b)
if(quotient==0):
    print("<b> the quotient is zero")
if(remainder==0):
    print("<b>the remainder is zero")
if(quotient!=0 and remainder!=0):
    print("<b>all the values are non zero")

#part(c)
partClist=[quotient+4,remainder+4,quotient+5,remainder+5,quotient+6,remainder+6]
result=[]
for i in range(len(partClist)):
    if partClist[i]>4:
        result.append(partClist[i])
print("<c>filtered out numbers that are greater than 4 are:{result}")

#part(d)
setresult=set(result)
print("<d>set=",setresult)

#part(e)
immutableset=frozenset(setresult) #frozen set is used to make the set immutable
print("<e>immutable set=",immutableset)

#part(f)
print("<f>hash value of the max value from the above set=",hash(max(immutableset)))

