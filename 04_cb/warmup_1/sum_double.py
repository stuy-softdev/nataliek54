#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def sum_double(a, b):
  if a == b:
    return 2 *(a + b)
  return a + b

#test cases
print("testing 1, 2 (should be 3) ==> " + str(sum_double(1, 2)))
print("testing 3, 2 (should be 5) ==> " + str(sum_double(3, 2)))
print("testing 2, 2 (should be 8) ==> " + str(sum_double(2, 2)))
