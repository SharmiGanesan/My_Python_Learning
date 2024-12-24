#List Methods
list=["Ganesan","Gnanam","Saravanan","Sharmi"]
list.append("Ilan")
print("To append  element at the end:",list)
list.insert(3,"Naveen")
print("To insert element at specific index:", list)
list.extend(["Poorni","Yazhan"])
print("To add more than one element:", list)
list.extend(("Poorni","Yazhan"))
print(list)      #adds elements from tuple to list
list_1=[1,2,3]
list_1.extend(x*3 for x in range (3))
print("Added more no. of elements using for loop:", list_1)
print("Removed specific index:", list.pop(8))
print("Removed last:", list.pop())
list_2=["Ganesan","Gnanam","Saravanan","Sharmi"]
list_2.remove("Sharmi")
print("Removed specified element:", list_2)
list_3=[[1,2],[2,3],[3,4]]
list_3.remove([2,3])
print("Removed list of list:", list_3)
if "Ganesan" in list_2:
    list_2.remove("Ganesan")
    print("Check the item and remove using if:", list_2)
list_4=["Ganesan","Gnanam","Saravanan","Sharmi"]
del list_4[3]
print("Delete the indexing element:", list_4)
del list_4
#print(list_4)   # if indexing not specified deletes the whole list
list_5=[1,2,3,4,5,6]
print("Clear the entire list:", list_5.clear())
list_5.append(7)
print(list_5)
list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)


#for loop
list_6=["sasi","sathya","eswari"]
for x in list_6:
    print("To print listed elements using loop fn.:", x)
for x in range(len(list_6)-1):
    print("To print listed elements using loop fn. n range,len:",list_6[x])
for x in range(0,2,2):
    print("To print listed elements using loop fn. n range:", list_6[x])


#while loop
list_7=["sasi","sathya","eswari","Naveen"]
i=0
while i<len(list_7):
    print("To print listed elements in expected way:", list_7[i])
    i += 2 # can parse dynamic iterations


# #sort()
abc=[10.5, 8.5, 4.6, 9.54]
abc.sort(reverse=True)
print(abc)
def myfunc(n):
    return abs(n-50)
list_8=[65,76,87,96,34]
list_8.sort(key=myfunc)
print(list_8)

#copy()
list_9=list.copy()
list.append("Ilan")
print(list_9)
print(list)

#join()
list_11=[1, 2, 3]
list_12=[10, 20, 30]
list_13=list_12+list_11
print(list_13)
for x in list_12:
    list_11.append(x)
print(list_11)
list_11.extend(list_12)
print(list_11)