#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def last2(str):
  count = 0
  last_str = str[len(str) - 2:]
  for i in range(len(str) - 2):
    if (str[i:i + 2] == last_str):
      count += 1
  return count
