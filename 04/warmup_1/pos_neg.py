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
