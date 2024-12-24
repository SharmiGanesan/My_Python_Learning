#dict methods
phone = { "brand" : "Apple" , "model" : "15 pro", "year" : 2023 }
print(len(phone))
print(type(phone))
phone = dict(brand = "Apple" , model = "15 pro", year = 2023)
print(phone)
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict1=dict(zip(keys, values))
print(dict1)
print(phone.get("model"))
print(phone.keys())
print(phone.values())
print(phone.items())
#check if key exists:
if "year" in phone:
    print("yes key exists")
phone.update({"year" : 2024 , "Color": "Black"})
print(phone)
print(phone.pop("year"))
print(phone.popitem())
del phone["model"]
print(phone)
#del phone
phone.clear()
print(phone)

#Looping dict
phone = { "brand" : "Apple" , "model" : "15 pro", "year" : 2023 }
for x in phone:
    print(x)
for x in phone.keys():
    print(x)
for x in phone:
    print(phone[x])
for x in phone.values():
    print(x)
for x,y in phone.items():
    print(x,y)

#Copy  DICT
dict_1=phone.copy()
phone["color"]="Black"
print(dict_1)
print(phone)

#vowels_finding_practice

a="endeavour"
for x in a:
    if x in "aeiou":
        print("Vowels present in endeavour:", x)


b="maldives"
for x in b:
    if x in "aeiou":
        print("Vowels present in maldives:", x)


