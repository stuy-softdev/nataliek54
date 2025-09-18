#Natalie Keiger
#Salt Lamp Horse
#SoftDev
#K04 -- Reviewing python basics
#2025-09-12

def front_times(str, n):
    newstr = ""
    if (len(str) < 3):
        for i in range(n):
            newstr = newstr + str
    else:
        for i in range(n):
            newstr = newstr + str[0:3]
    return newstr

#test cases
print("testing 'Chocolate', 2 (should be 'ChoCho') ==> " + str(front_times('Chocolate', 2)))
print("testing 'Chocolate', 3 (should be 'ChoChoCho') ==> " + str(front_times('Chocolate', 3)))
print("testing 'Abc', 3 (should be 'AbcAbcAbc') ==> " + str(front_times('Abc', 3)))
