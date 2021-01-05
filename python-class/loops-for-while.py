# as https://www.w3schools.com/python/python_for_loops.asp

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
# https://www.w3schools.com/python/python_while_loops.asp

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# get out of loop 

i = 0
while i < 6:
  i += 1
  if i == 3 or i== 5:
    continue
  print(i)
# conditional skip some loop 
