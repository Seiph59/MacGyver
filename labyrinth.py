import os

x = 0
y = 0
myMap = []
ways = [3,18,31,32,33,34,35,36,37,52,67,68,69,70,78,83,84,93,97,98,99,108,114,123,
124,125,126,127,128,129,132,138,141,147,153,156,162,167,168,171,172,173,174,
175,176,177,190,192,193,202,203,204,205,217]

if (os.path.exists ('Labyrinth.txt')):
  os.remove('Labyrinth.txt')

while x <= 14:
    while y <= 14:
        myMap.append([x, y, "wall"])
        y += 1
    x += 1
    y = 0

for way in ways: 
    myMap[way][2] = "way"

myMap[3][2] = "start"
myMap[217][2] = "finish"

""" Send the Structure in a file
and manage the labyrinth from this file"""


for y in range(len(myMap)):
    fileManagement = open('Labyrinth.txt', 'a')
    for point in myMap[y][2]:
        fileManagement.write(str(point))
    fileManagement.write(" \n")
    fileManagement.close()
