#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def string_bits(str):
  newstr = ""
  for i in range(len(str)):
    if (i % 2 == 0):
      newstr = newstr + str[i]
  return newstr

#test cases
print("testing 'Hello' (should be 'Hlo') ==> " + str(string_bits('Hello')))
print("testing 'Hi' (should be 'H') ==> " + str(string_bits('Hi')))
print("testing 'Heeololeo' (should be 'Hello') ==> " + str(string_bits('Heeololeo')))
