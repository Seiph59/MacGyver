""" File who generate the labyrinth"""
import os

X = 0
Y = 0
MY_MAP = []
WAYS = [3, 18, 31, 32, 33, 34, 35, 36, 37, 52, 67, 68, 69,
        70, 78, 83, 84, 93, 97, 98, 99, 108, 114, 123,
        124, 125, 126, 127, 128, 129, 132, 138, 141, 147,
        153, 156, 162, 167, 168, 171, 172, 173, 174,
        175, 176, 177, 190, 192, 193, 202, 203, 204, 205, 217]

if os.path.exists('Labyrinth.txt'):
    os.remove('Labyrinth.txt')

while X <= 14:
    while Y <= 14:
        MY_MAP.append([X, Y, "wall"])
        Y += 1
    X += 1
    Y = 0

for way in WAYS:
    MY_MAP[way][2] = "way"

MY_MAP[3][2] = "start"
MY_MAP[217][2] = "finish"

""" Send the Structure in a file
and manage the labyrinth from this file"""


for y, value in enumerate(MY_MAP):
    fileManagement = open('Labyrinth.txt', 'a')
    # for point in MY_MAP:
    fileManagement.write(str(value[2]))
    fileManagement.write(" \n")
    fileManagement.close()
