#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def string_times(str, n):
  newStr = ""
  for i in range(n):
    newStr = newStr + str
  return newStr

#test cases
print("testing 'Hi', 2 (should be 'HiHi') ==> " + str(string_times('Hi', 2)))
print("testing 'Hi', 3 (should be 'HiHiHi') ==> " + str(string_times('Hi', 3)))
print("testing 'Hi', 1 (should be 'Hi') ==> " + str(string_times('Hi', 1)))
