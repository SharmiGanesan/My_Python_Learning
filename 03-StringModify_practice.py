#Strings Modify operations
x=" hello, Ilan! "
print(x.upper())
print(x.lower())
print(x.strip().capitalize())
print(x.replace("I","Ni"))
print(x.capitalize())         #if all letters are in lowercase cant use capitalize
print(x[1].upper()+x[2:])    #capitalize
y="hELLO WORLD"
print(y.capitalize())
z="HELLO"
print(z.capitalize())
n="naveen sharmi ilan saravana ganesan pushpam poorni gnanam"
print(n.title())
print(x.split(","))
s="petty  bought some butter, butter was bitter, so she make some better butter, to make the bitter butter better."
print(s.split(","))
print(s.split("butter"))


#String Format
zip=78717
apt="ventana oaks"
location="We live in Austin,exactly at (zip)"
print(location)  #as zip is not a string it cant be concatenated,use f-string or save as str or use placeholder
location="We live in Austin,exactly at %s , %d." %(apt,zip)
print(location)
location="We live in Austin,exactly at %s." %(apt)
print(location)
print(f"We live in Austin,exactly at {zip}")
pin="78717"
print("We live in Austin,exactly at " + (pin))
time=6.30
#print("I want to wake up at %f in the morning. " %(time)



#Place holder
amount=59
8print(f"The cost of Instapot is {amount:.2f} dollars.")



#Escape charactersl
x="Python is a versatile, high-level programming language known for its simplicity and readability. Developed by Guido van Rossum and first released in 1991, Python has become one of the most popular languages in the world, powering everything from web applications and data analysis to artificial intelligence and scientific computing. Its syntax emphasizes code clarity, making it an excellent choice for beginners while remaining powerful enough for seasoned developers. Python supports multiple programming paradigms, including object-oriented, procedural, and functional programming, and comes with a rich standard library that simplifies complex tasks. With a thriving community and a vast ecosystem of third-party libraries, Python continues to be a go-to language for developers in diverse fields."
print(x.split(","))
print(x.replace(",","\n"))
print("python  \bcoder")
print("pyhton\tcoder")
print("I love 'Food'.")
print('I love "cooking"')
print("I love \"Ilan\"")
print('I love \'Naveen\'')
print("I love my mom\\dad")
print("America\rIndia")