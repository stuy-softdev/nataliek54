#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def pos_neg(a, b, negative):
  if (negative and a<0 and b<0):
    return True
  if (negative):
    return False
  if (a>0 and b<0) or (a<0 and b>0):
    return True
  return False

#test cases
print("testing 1, -1, F (should be T) ==> " + str(pos_neg(1, -1, False)))
print("testing -1, 1, F (should be T) ==> " + str(pos_neg(-1, 1, False)))
print("testing -4, -5, T (should be T) ==> " + str(pos_neg(-4, -5, True)))
