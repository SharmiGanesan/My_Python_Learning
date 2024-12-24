#Set_Functions
def my_set_func():
    flowers={"rose","lilly","lotus","daisy"}
    print("To get the length of set:", len(flowers))
    print("To get the type:", type(flowers))
    for x in flowers:
        print(x)
    if "rose" in flowers:
        print("yes")
    flowers.add("jasmine")
    print("Added an element to set:", flowers)
    colors={"red", "green", "blue", "pink"}
    colors.update(flowers)
    print("Added an set to set:", colors)
    colors.remove("pink")
    print("Removed an element from set:", colors)
    colors.discard("black")
    print("Removed notfound element from set:", colors)
    colors.pop()
    print("Removed a random element from set:", colors)
    colors.clear()
    print("Cleared and retrieved empty set:", colors)
    del colors
    #print(colors)
my_set_func()

#Loop_Sets
def set_loop_func():
    flowers={"rose","lilly","lotus","daisy"}
    for x in flowers:
        print("Assigning elements from set:", x)
    numbers={2, 4, 6, 8, 10, 13}
    for x in numbers:
        if x%2 == 0 :
            print("Assigning elements from set and using if condition:", "x is even number")
set_loop_func()

#Set_operations
def set_operations_func():
    #union()
    flowers = {"rose", "lilly", "lotus", "daisy"}
    colors = {"red", "green", "blue", "rose"}
    numbers = (2, 4, 6, 8, 10, 13)
    new_set = flowers | colors | set(numbers)
    print("Joined sets using union function:", new_set)
    new_set2 = flowers.union(colors)
    print(new_set2)
    new_set3 = flowers.union(numbers)
    print(new_set3)
    #Interseection()
    new_set4 = flowers & colors
    print("Found common element b/w sets using Intersection fn.:", new_set4)
    new_set5 = flowers.intersection(new_set3)
    print(new_set5)
    flowers.intersection_update(colors)
    print(flowers)
    #Difference()
    flowers = {"rose", "lilly", "lotus", "daisy"}
    new_set6 = flowers - colors
    print("Removed the duplicates from sets using difference fn.:", new_set6)
    new_set7 = flowers.difference(colors)
    print(new_set7)
    flowers.difference_update(colors)
    print(flowers)
    #Symmetric_difference()
    flowers = {"rose", "lilly", "lotus", "daisy"}
    new_set8 = flowers ^ colors
    print("Found the uncommon elements from sets using symmetric difference fn.:", new_set8)
    new_set9 = flowers.symmetric_difference(colors)
    print(new_set9)
    flowers.symmetric_difference_update(colors)
    print(flowers)
set_operations_func()