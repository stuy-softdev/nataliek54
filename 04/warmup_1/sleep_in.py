#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def sleep_in(weekday, vacation):
  if weekday == False:
    return True
  if vacation == True:
    return True
  if vacation == False and weekday == True:
    return False

#test cases
print("testing F, F (should be T) ==> " + str(sleep_in(False, False)))
print("testing T, F (should be F) ==> " + str(sleep_in(True, False)))
print("testing F, T (should be T) ==> " + str(sleep_in(False, True)))
