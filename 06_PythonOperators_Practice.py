#Arithmetic_Operators
a=11
b=5
print("add:", a+b)
print("Subtract:", a-b)
print("Multiply:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Exponent:", a**b)
print("Floor Division:", a//b)

#Assignment_Operators
a+= 3
print("addassign:", a)
b=11
b-=3
print("subtractassign:", b)
c=11
c*=3
print("Multiplyassign:", c)
d=11
d/=3
print("Divisionassign:", d)
e=11
e**=3
print("exponentassign:", e)
f=11
f%=3
print("modulusassign:", f)
g=11
g//=3
print("Floordivisionassign:", g)
h=11
h&=3
print("BitwiseAndAssign:", h)
i=11
i|=3
print("BitwiseORAssign:", i)
j=11
j^=3
print("BitwiseXORAssign:", j)
k=11
k<<=3
print("LeftshiftAssign:", k)
l=11
l>>=3
print("RightshiftAssign:", l)
print("can assign in the print syntax:", a:=5 +3)



#Comparison_Operators
a=6
b=3
print("Compare whether equal:", a==b)
print("Compare whether not equal:", a!=b)
print("Compare whether smaller:", a<b)
print("Compare whether greater:", a>b)
print("Compare whether lesserthan or equal:", a<=b)
print("Compare whether greaterthan or equal:", a>=b)


#Logical_Operators
print("Check both are true:", a!=b and a>b)
print(a==b and a>b)
print("Check anyone is true:", a==b or a>b)
print("Check anyone is true:", a!=b or a>b)
print("Inverts the truth:", not b>a)



#Identity_Operators
a=[1,2,4,8]
b=[1,2,4,8]
c=a
print("Check both are assigned as equal:", a is c)
print(b is c)
print("Inverts the truth:", a is not c)
print("Inverts the truth:", b is not c)



#Membership_Operators
x=1,2,3
y=3
print("check y is member of sequence:", y in x)
print("check y is not member of sequence:",y not in x)

