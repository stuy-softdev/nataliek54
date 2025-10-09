#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  if not (a_smile == True) and not (b_smile == True):
    return True
  if a_smile == True or b_smile == True:
    return False

#test cases
print("testing TT (should be T) ==> " + str(monkey_trouble(True, True)))
print("testing FF (should be T) ==> " + str(monkey_trouble(False, False)))
print("testing TF (should be F) ==> " + str(monkey_trouble(True, False)))
