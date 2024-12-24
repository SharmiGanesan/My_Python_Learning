#String Methods
a="hello world"
print("To change the first letter to upper case:", a.capitalize())
b="HELLO WORLD"
print("To change into lowercase:", b.casefold())
c="Hello Ilan"
print("To get a CENTERed a string:", c.center(20))
d="I scream, you scream, we all scream for ice cream!"
print("To get the COUNT of specific word:", d.count("scream"))
print("To check if the string ENDSWITH the specific value:", d.endswith("!"))
print(d.endswith("cream"))
e="Hello Ilan"
print(e.expandtabs(10))
print("To FIND the specific character or word in the string:", d.find("!"))
print("To FIND the specific character or word in the string:", d.find("z"))
f="Hello {}"
print("To FORMAT specific value in the string:", f.format("Ilan"))
g="{} is {}"
print(g.format("love","god"))
h="Will meet you on {day} at {time}."
print(h.format(day="Monday",time="5pm"))
i="{0} is teaching {course}."
print("Mixed indexing and named arguments:", i.format("Naveen",course="Python"))
j="I need the value as {:.2f}."
print(j.format(1.23375634765546098))
print("{:>20}".format("Right"))
print( "My name is {name} and I am {age} years old.".format_map({"name": "Sharmi", "age": 30}))
d="I scream, you scream, we all scream for ice cream!"
print("To get the position of specific substring in a string:", d.index("w"))
print(d.index("scream",15))
print("To check only alphanumeric is present:","Python123".isalnum())
print("python 123".isalnum())
print("123".isalnum())
Password= "Naveen9739"
if Password.isalnum():
    print("valid Password")
else:
    print("invalid Password")
Password= "Naveen*9739"
if Password.isalnum():
    print("valid Password")
else:
    print("invalid Password")
print("To check string contains only alphabets:", Password.isalpha())
Fact="100k job openings will be there in 2024."
Truth=Fact.split()
Alnum_Truths=[Truth for Truth in Truth if Truth.isalnum()]
print(Alnum_Truths)
Alnum_Truth2=[Truth for Truth in Truth if not Truth.isalnum()]
print(Alnum_Truth2)
Alpha_Truths=[Truth for Truth in Truth if Truth.isalpha()]
print(Alpha_Truths)
j="12345"
print("To check only the decimals r present:", j.isdecimal())
values = ["123", "123.45", "ABC", "6789"]
decimal_values = [value for value in values if value.isdecimal()]
print(decimal_values)
print("To check digits i.e included superscripts n fractions r present:", j.isdigit())
k=""
print(k.isdigit())  #empty str is not treated as digit
l = "2nd_variable"
print("To check string has valid identifiers:", l.isidentifier())
m="my_var"
print(m.isidentifier())
a="hello world"
b="HELLO WORLD"
print("To check str has only lower cases:", a.islower())
print(b.islower())
print("To check str has only upper cases:",a.isupper())
print(b.isupper())
print("To check str has space or empty:", "   ".isspace())
print("\t\n".isspace())
j="12345"
print("To check str has only numerics:",j.isnumeric())
n="XX"
print("To check str has only numerics:",n.isnumeric())   #isnumeric accepts roman numbers but getting false
print("To check str has only printable characters:",a.isprintable())
print("\t\n".isprintable())
print("To check str has first upper case in each word:",b.istitle())
print("Hello World".istitle())
o=["python ", "is ", "good"]
print("To join the number of strings:", ''.join(o))
p=("python ", "is ", "good")
print("To join the number of strings w specific character:", '.'.join(p))
q={"python ", "is ", "good"}
print(','.join(q))
r = "\n\t  Hello, Naveen!  \n\t"
print("To trim the string:", r.strip())
s = "      Hello, Naveen! "
print(s.lstrip())
t = "Hello, Naveen!      "
print(t.rstrip())
trans = str.maketrans("hai", "bye")
u = "haiabc"
print("To translate specific characters:", u.translate(trans))
v = "haidog"
print(v.translate(trans))
trans = str.maketrans("", "" ,"bye")
w = "byeilan"
print(w.translate(trans))
y= "Naveen,Ilan,Sharmi"
print("To part the string to and from the specific character: ", y.partition("Ilan"))
print("To split the string by specific character:", y.rsplit(","))       # it should be used to String not List
z = "apple|banana|cherry|dates"
print("To split the string in specified position:", z.rsplit("|", 2))
print(z.rsplit("|", 1))
ab = "Hello World Python"
print("To split word by word:", ab.split())
bc="Hello\nWorld\nPython"
print("To split the strings line by line:", bc.splitlines())
print("To check string starts with gn letter:", ab.startswith("H"))
print("To  swap upper and lower case: ", y.swapcase())
print("To  change the first letter of each word to uppercase:", z.title())
cd="12345"
print("To fill the specified no. of zeros to make the digit mentioned:", cd.zfill(7))
