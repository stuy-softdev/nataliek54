#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def makes10(a, b):
  if a == 10 or b == 10:
    return True
  if a + b == 10:
    return True
  return False

#test cases
print("testing 9, 10 (should be True) ==> " + str(makes10(9, 10)))
print("testing 9, 9 (should be False) ==> " + str(makes10(9, 9)))
print("testing 1, 9 (should be True) ==> " + str(makes10(1, 9)))
