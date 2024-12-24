#string slicing

slice=("My Son is ILAN!")
print(slice[:2])
print(slice[3:6])
print(slice[7:9])
print(slice[-5:-1])
print(len(slice))
print(slice[14:])


#list slicing
list=[1,22,333,4444]
print(list[:1])
print(list[1:2])
print(list[2:3])
print(list[-4:])


#mixed slicing not possible

x=("My mobile number is 8344857514 at 2018")
y=["Naveen","number",9739]
print(y[0])
#print(x[:2]+y[0])   Different data types cannot be concatenated


#Conversion/Casting
a=1
b=2.2
c=12e34
d=1+2j
print(float(a))
print(complex(a))
print(str(a))
print(int(b))
print(complex(b))
print(type(c))
print(float(c))
print(int(c))
print(str(c))      #complex cant be converted to integer

#frozenset

a=({"Naveen","Sharmi","Ilan"})
print(a)
b=({4444,333,22,1})
print(b)

#range
for x in range(0,10):
    print(x)
for y in range(0,10,3):
    print(y)



