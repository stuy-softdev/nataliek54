#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def string_splosion(str):
  newstr = ""
  for i in range(len(str)):
    newstr = newstr + str[:i + 1]

  return newstr
