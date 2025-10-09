#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def near_hundred(n):
  if abs(100 - n) <= 10:
    return True
  if abs(200 - n) <= 10:
    return True
  return False

#test cases
print("testing 93 (should be T) ==> " + str(near_hundred(93)))
print("testing 90 (should be T) ==> " + str(near_hundred(90)))
print("testing 89 (should be F) ==> " + str(near_hundred(89)))
