#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return "not " + str

#test cases
print("testing 'candy' (should be 'not candy') ==> " + str(not_string('candy')))
print("testing 'x' (should be 'not x') ==> " + str(not_string('x')))
print("testing 'not bad' (should be 'not bad') ==> " + str(not_string('not bad')))
