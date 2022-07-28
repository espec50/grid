import pandas as pd
import numpy as np
import re
#Read excel file into pandas dataframe
df = pd.read_excel("FRR.xlsx","Grid")

#numerical variables
cable_tray1 = 94
cable_tray2 = 75
cable_tray3 = 65
cable_tray4 = 40
cable_tray5 = 23
cable_tray6 = 11

#Obtain rack location from user
userGrid = input('Please enter a grid, Ex. AD-45: ')
print(f'You entered: {userGrid}')
#Split user location into alphs/numerical parts
userGridSplit = userGrid.split('-')
gridAlpha = userGridSplit[0]
userGridNum = userGridSplit[1]


#Function to convert alpha port of grid location to a numberical value Ex. AA = 27, AB = 28
def alpha_to_num(s):
    n = ord(s[-1]) - 64
    if s[:-1]:
        return 26 * (alpha_to_num(s[:-1])) + n
    else:
        return n
#Call the function to convert alpha portion of rack location into a numerical value
rackLocAlpha = (alpha_to_num(gridAlpha))
frr1LocAlpha = (alpha_to_num("AF"))

vertical_harness_dist = (1 + abs(rackLocAlpha - frr1LocAlpha))*2
print(vertical_harness_dist)

relayLocNum = 85

if relayLocNum in range(cable_tray2,cable_tray1):
    if cable_tray1 - relayLocNum < relayLocNum - cable_tray2:
        relay_to_tray = cable_tray1 - relayLocNum + 1
    else:
        relay_to_tray = relayLocNum - cable_tray2 + 1
print(relay_to_tray)
#elif relayLocNum in range(cable_tray3,cable_tray4):


#Function to convert user provide grid to abtract numerical grid
def convert_to_abstract_grid(someGrid):
    if int(userGridNum) >= 1 and int(userGridNum) <= 30:
        alley = 1
    elif int(userGridNum) >= 35 and int(userGridNum) <= 65:
        alley = 2
    elif int(userGridNum) >= 70 and int(userGridNum) <= 99:
        alley = 3
    abstract_grid = str(alley) + str(rackLocAlpha) + str(userGridNum)
    abstract_grid = int(abstract_grid)
    your_alley = alley
    print(f'Your alley number is: {alley}')
    return abstract_grid
#call the function to conver the user provided location into an abstract number to look up the relay rack
your_abstract_grid = convert_to_abstract_grid(userGridNum)


#Function to determine which relay rack pair to use
def choose_FRR(someAbstractGridNum):
    if your_abstract_grid in range(13007,15230):
        FrrPair = 'AL-21/AN-13'
    elif  your_abstract_grid in range(15307,18030):
        FrrPair = 'BK-22/BC-22'
    elif your_abstract_grid in range(23039,25167):
        FrrPair = 'AM-62-AL-41'
    elif your_abstract_grid in range (25239,27067):
        FrrPair = 'BA-54-BP-54'
    elif your_abstract_grid in range(27139,29767):
        FrrPair = 'CB-59-CM-52'
    elif your_abstract_grid in range(36274,38399):
        FrrPair = 'CD-94-BO-78'
    elif your_abstract_grid in range(19007,112630):
        FrrPair = 'DL-21-CU-22'
    elif your_abstract_grid in range(113107,116730):
        FrrPair = 'FB-21-EQ-12'
    elif your_abstract_grid in range(212839,214367):
        FrrPair = 'DZ-59-EG-48'
    elif your_abstract_grid in range(314974,316899):
        FrrPair = 'FG-78-EV-98'
    return FrrPair
#Call function to determine FRR pair based off abstract numberical grid
your_FrrPair = choose_FRR(your_abstract_grid)
print(f'Your abstract grid is: {your_abstract_grid}')
print(f'Your FRR pair is: {your_FrrPair}')


your_FrrPair_split = your_FrrPair.split('-')
your_FrrPair_1_alpha = your_FrrPair_split[0]
your_FrrPair_1_num = your_FrrPair_split[1]
your_FrrPair_2_alpha = your_FrrPair_split[2]
your_FrrPair_2_num = your_FrrPair_split[3]

print(your_FrrPair_1_alpha)
print(your_FrrPair_1_num)
print(your_FrrPair_2_alpha)
print(your_FrrPair_2_num)
