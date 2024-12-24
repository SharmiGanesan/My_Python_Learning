def my_tuple_func():
    family=("Naveen", "Sharmi", "Ilan")
    print("To get he length of the tuple:", len(family))
    list_1=["Naveen", "Sharmi", "Ilan"]
    set_1={"Naveen", "Sharmi", "Ilan"}
    print("To get the list as tuple:", tuple(list_1))
    print("To get the set as tuple:",tuple(set_1))
    if "Ilan" in family:
        print("Yes")
    if "e" in family[0]:
        print("Yes")
    #update tuple
    list_2= ["Ashvika",]
    list_1 += list_2
    print(tuple(list_1))
    list_1.remove("Sharmi")
    print(tuple(list_1))
    list_1.append("Sharmi")
    print(tuple(list_1))
    del list_1

    #Unpack_tuples
    colors=("Red", "Green", "Blue")
    (x,y,z)=colors
    print("Tuple unpack:", x)
    print(y)
    print(z)
    colors_2=("Red", "Green", "Blue", "Yellow", "Orange")
    (a,*b,c)=colors_2
    print("Unpack using asterisk method:",a)
    print(b)
    print(c)

    #Loop_tuples
    sisters=("sasi","sathya","eswari")
    for x in sisters:
        print("To print tupled elements using loop fn.:", x)
    for x in range(len(sisters)-1):
        print("To print tupled elements using loop fn. n range,len:",sisters[x])
    for x in range(0,2,2):
        print("To print tupled elements using loop fn. n range:", sisters[x])

    #while loop
    siblings=("sasi","sathya","eswari","Naveen")
    i=0
    while i<len(siblings):
        print("To print tupled elements in expected way:", siblings[i])
        i += 2

    #tuple_methods
    tuple_1=(1, 3, 4, 3, 5, 6, 3, 5, 3)
    result = tuple_1.count(3)
    print("To get the count of character or string:", result)
    print("To find the index of specified character:", tuple_1[5])

my_tuple_func()
