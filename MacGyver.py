import os

x = 0
y = 0
myMap = []
ways = [3,18,31,32,33,34,35,36,37,52,67,68,69,70,78,93,97,98,99,108,114,123,
124,125,126,127,128,129,132,138,141,147,153,156,162,167,168,171,172,173,174,
175,176,177,190,192,193,202,203,204,205,217]

while x <= 14:
    while y <= 14:
        myMap.append([x, y, "Wall"])
        y += 1
    x += 1
    y = 0
#print(len(myMap))
#print(myMap)
for way in ways: 
    #print(passage)
    for i in range(len(myMap)):
        #print(i)
        if i is way:
            #print(myMap[i][2])
            myMap[i][2] = "Way"
myMap[3][2] = "Start"
myMap[217][2] = "Finish"

""" Send the Structure in a file
and manage the labyrinth from this file"""

fileManagement = open('Labyrinth.txt', 'a')
for point in myMap:
    #print(point)
    fileManagement.write(str(point) +"\n")
fileManagement.close()
#print(myMap)

""" Read the file and all the structure """

openFile = open('Labyrinth.txt', 'r')
lignes = openFile.readlines()
openFile.close()

for ligne in lignes: 
    print(ligne)

        

