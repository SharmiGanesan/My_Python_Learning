#List
list_x = [ "masha", "bear", "ilan" ]
print(list_x)
list_y = [143,4.5,"Ilan"]
print(list_y)
#Indexing
list_y[2]="Naveen"
print(list_y)
#Append
list_y.append("Govindaraj")
print(list_y)
#Insert
list_y.insert(2,"Ilan")
print(list_y)
#Insert
list_y.extend(["pushpam","sasi"])
print(list_y)
#addlist
list_z = list_x +list_y
print(list_z)
#remove
list_y.remove(4.5)
print(list_y)
#pop
list_y.pop(2)
print(list_y)




#tuple
tuple_1 = (0,1,2,3,4)
print(tuple_1)
tuple_2 = (5,6,7,8,9,)
print(tuple_1 + tuple_2)
# tuple_1[1] = 44
# print(tuple_1)


#dict
a={"father": 'Naveen' , 'son' : 'Ilan'}
print(a['son'])