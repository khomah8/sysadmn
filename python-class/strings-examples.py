# from  https://www.w3schools.com/python/ 

print("Hello")
print('Hello')

a = "Hello, World"
print(a)

abb = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(abb)

# try on  https://www.w3schools.com/python/trypython.asp?filename=demo_string_slice_start
print(abb[:4])
print(abb[5:])

bb = "H e l l o,d e a r W o r l d !"
print(bb[::2])

# try on  https://www.w3schools.com/python/trypython.asp?filename=demo_string_replace
aw = "333Hello, World333"
print(aw.strip('3'))  # returns "Hello, World!" -- removes any '3' from the beginning or the end 

print(a, '/', a.replace("H", "Jo"))

print(a.split(" "))  # returns ['Hello,', ' World!']

# takes the passed arguments, formats them, and places them in the string where the placeholders {} are 
age = 36
name = 'John'
txt = "My name is {1}, and I am {0}"
print(txt.format(name, age))
