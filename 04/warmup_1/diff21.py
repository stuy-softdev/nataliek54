#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def diff21(n):
  if n > 21:
    return 2 * abs(21 - n)
  return 21 - n

#test cases
print("testing 19 (should be 2) ==> " + str(diff21(19)))
print("testing 10 (should be 11) ==> " + str(diff21(10)))
print("testing 21 (should be 0) ==> " + str(diff21(21)))