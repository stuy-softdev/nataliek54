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
