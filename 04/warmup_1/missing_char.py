#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def missing_char(str, n):
  return str[:n] + str[n+1:]

#test cases
print("testing 1 (should be 'ktten') ==> " + str(missing_char('kitten', 1)))
print("testing 0 (should be 'itten') ==> " + str(missing_char('kitten', 0)))
print("testing 4 (should be 'kittn') ==> " + str(missing_char('kitten', 4)))
