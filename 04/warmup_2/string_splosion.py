#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def string_splosion(str):
  newstr = ""
  for i in range(len(str)):
    newstr = newstr + str[:i + 1]

  return newstr

#test cases
print("testing 'Code' (should be 'CCoCodCode') ==> " + str(string_splosion('Code')))
print("testing 'abc' (should be 'aababc') ==> " + str(string_splosion('abc')))
print("testing 'ab' (should be 'aab') ==> " + str(string_splosion('ab')))

