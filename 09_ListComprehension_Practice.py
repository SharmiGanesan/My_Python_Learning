#List_Comprehension
names=["Ganesan","Gnanam","saravanan","sharmi"]
newnames=[]
for x in names:
    if "r" in x:
        newnames.append(x)
print(newnames)
newnames=[x for x in names if "s" in x ]
print("Fetch names w character s:", newnames)
#using else
newnames=[x if "an" in x else "Ilan" for x in names]
print("Fetch names w character an else replace Ilan:",newnames)

#Practice_1 Comprehensive method
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = [x for x in list if x % 2 != 0]
print("Fetch odd no.s thru comprehensive method:", odd_list)
even_list = [x for x in list if x % 2 == 0]
print("Fetch even no.s thru comprehensive method:", even_list)
#Practice_1 Classic method
odd_list=[]
even_list=[]
for x in list:
    if x%2 != 0:
        odd_list.append(x)
    else:
        even_list.append(x)
print("Fetch odd no.s thru classic method:", odd_list)
print("Fetch even no.s thru classic method:", even_list)



#practice_2 Classic method
list_1=[9739, 1.43, 333, 3.14, "Naveen", 514, "Sharmi", 5.57, "Ilan", True]
integer_list=[]
float_list=[]
string_list=[]
boolean_list=[]
for x in list_1:
    if type(x) == int:
        integer_list.append(x)
    elif type(x) == float:
        float_list.append(x)
    elif type(x) == str:
        string_list.append(x)
    else:
        boolean_list.append(x)
print("Fetch integers from mixed list using classic method:", integer_list)
print("Fetch float numbers from mixed list using classic method:", float_list)
print("Fetch strings from mixed list using classic method:", string_list)
print("Fetch boolean from mixed list using classic method:", boolean_list)
#Practice_2 Comprehensive method
type_list=[type(x) for x in list_1]
integer_list=[x for x in list_1 if type(x) == int]
float_list=[x for x in list_1 if type(x) == float]
string_list=[x.upper() for x in list_1 if type(x) == str]
boolean_list=[not x for x in list_1 if type(x) == bool]
print(type_list)
print("Fetch integers from mixed list using Comprehensive method:", integer_list)
print("Fetch float numbers from mixed list using Comprehensivec method:", float_list)
print("Fetch strings from mixed list using Comprehensive method:", string_list)
print("Fetch boolean from mixed list using Comprehensive method:", boolean_list)
