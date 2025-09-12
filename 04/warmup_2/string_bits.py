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
