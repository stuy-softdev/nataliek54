#Natalie Keiger, Naomi Kurian, Joyce Lin
#Crinkled-water
#SoftDev
#K07 -- randodicto
#time taken: 2.0
#2025-09-17

'''
Criteria: we decided to sort the list alphabetically and ignore case (so not by ASCII)
Approach: we first removed the header and split the csv, then sorted it, then iterated through into three sections to setup username and duckiename key pairs
Sanitization: We removed the header, used "strip" to get rid of whitespace, and checked that the length was >2 to get rid of empty comment lines

'''
import random

def categorize(filename):
    file = open(filename, "r") #opens file to read

    file_content = file.read().strip() #removes empty spaces
    content = file_content.split("\n") #turn csv into array
    dict1 = {}
    dict2 = {}
    dict3 = {}
    
    content.remove("PD,U_GH,QUACK") #get rid of header
    
    i = 0
    while i < len(content):
        content[i] = content[i][2:] #takes away '4,'
        if (len(content[i]) < 3):
            content.remove(content[i]) #gets rid of empty values that are just ',,'
        else:
            i += 1
    content = sorted(content, key=str.casefold) #sorts alphabetically ignoring case

    for i in range(0, len(content)):
        content[i] = content[i].split(",", 1)  #if duckie name has commas, this adds the whole name
        if (len(content[i][0]) != 0):
            if (i < len(content)/3): #splits into three even categories by alphabetical order
                dict1[content[i][0]] = content[i][1]
            elif (i < 2 * len(content)/3):
                dict2[content[i][0]] = content[i][1]
            else:
                dict3[content[i][0]] = content[i][1]
               
    print("Criteria: splitting by alphabet value into thirds")
    print(dict1)
    print()
    print(dict2)
    print()
    print(dict3)
    print()
   
    random_selected = random.randrange(0, len(dict1))
    print("From dict 1: " + content[random_selected][0] + ", " + dict1[content[random_selected][0]])
    random_selected = random.randrange(len(dict1), len(dict2) + len(dict1))
    print("From dict 2: " + content[random_selected][0] + ", " + dict2[content[random_selected][0]])
    random_selected = random.randrange(len(dict2) + len(dict1), len(content))
    print("From dict 3: " + content[random_selected][0] + ", " + dict3[content[random_selected][0]])

categorize('handles-n-quacks.csv')

