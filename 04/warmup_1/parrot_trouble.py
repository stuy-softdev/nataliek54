#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  if talking == True and (hour >= 7 and hour <= 20):
    return False
  if talking == False:
    return False
