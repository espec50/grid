from optparse import Option
from pydoc import doc
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
    #print(f'Your alley number is: {alley}')
    return abstract_grid

#Function to determine alley(note: come back and replace the code above with less code by calling this function)
def determine_alley(someGrid):
    if int(userGridNum) >= 1 and int(userGridNum) <= 30:
        alley = 1
    elif int(userGridNum) >= 35 and int(userGridNum) <= 65:
        alley = 2
    elif int(userGridNum) >= 70 and int(userGridNum) <= 99:
        alley = 3
    return alley

#Call the function to get a stand alone allet valie of 1 to 3
alley = determine_alley(userGridNum)
print(f'Your alley number is: {alley}')

##Call function to determine FRR pair based off abstract numberical grid
your_abstract_grid = convert_to_abstract_grid(userGridNum)
your_FrrPair = choose_FRR(your_abstract_grid)
print(f'Your abstract grid is: {your_abstract_grid}')
print(f'Your FRR pair is: {your_FrrPair}')

#Assign and split FRR pair data into alpha/num and alpha abstract vales 
your_FrrPair_split = your_FrrPair.split('-')
your_FrrPair_1_alpha = your_FrrPair_split[0]
your_FrrPair_1_alpha_abs = alpha_to_num(your_FrrPair_1_alpha)
your_FrrPair_1_num = your_FrrPair_split[1]
your_FrrPair_2_alpha = your_FrrPair_split[2]
your_FrrPair_2_alpha_abs = alpha_to_num(your_FrrPair_2_alpha)
your_FrrPair_2_num = your_FrrPair_split[3]

#Function to determine the vertical distance on the birds eye between the user provided rack and FRR pair in feet
def find_vertical_harness_dist(someFRR):
    vertical_harness_dist = (1 + abs(rackLocAlpha - someFRR))*2
    return vertical_harness_dist
#Call the function to determine the distance of the two verticale runs(1/3 of the full distance formula)
frr_vertical_dist1 = find_vertical_harness_dist(your_FrrPair_1_alpha_abs)
frr_vertical_dist2 = find_vertical_harness_dist(your_FrrPair_2_alpha_abs)
print(f'The distance verticle distance to FRR {your_FrrPair_1_alpha}-{your_FrrPair_1_num} is {frr_vertical_dist1} feet')
print(f'The distance verticle distance to FRR {your_FrrPair_2_alpha}-{your_FrrPair_2_num} is {frr_vertical_dist2} feet')


#Function to find distance to both rails
def find_horizonstal_harness_dist(someGridNum):
    if alley == 1:
        option1 = abs(int(someGridNum - cable_tray6))*2+1
    elif alley == 2:
        option1 = abs(int(someGridNum - cable_tray4))*2+1
    elif alley == 3:
        option1 = abs(int(someGridNum - cable_tray2))*2+1
    return option1

#Call function to find lowest horizontal dist
cab_to_tray = find_horizonstal_harness_dist(int(userGridNum))
print(f'Rack location to cablt tray distance: {cab_to_tray}')



def find_horizontal(someUserGrid,someFrrGridNum):
    if someUserGrid in range(cable_tray2,cable_tray1):
        rack_to_tray_option1 = abs(someUserGrid - cable_tray1)
        rack_to_tray_option2 = abs(someUserGrid - cable_tray2)
        #frr_to_tray_option1 = abs(someFrrGridNum - cable_tray1)
        #frr_to_tray_option2 = abs(someFrrGridNum - cable_tray2)
    elif someUserGrid in range(cable_tray4,cable_tray3):
        rack_to_tray_option1 = abs(someUserGrid - cable_tray1)
        rack_to_tray_option2 = abs(someUserGrid - cable_tray2)
    elif someUserGrid in range(cable_tray6,cable_tray5):
        rack_to_tray_option1 = abs(someUserGrid - cable_tray1)
        rack_to_tray_option2 = abs(someUserGrid - cable_tray2)

    if someFrrGridNum in range(cable_tray2,cable_tray1):
        frr_to_tray_option1 = abs(someFrrGridNum - cable_tray1)
        frr_to_tray_option2 = abs(someFrrGridNum - cable_tray2)
    elif someFrrGridNum in range(cable_tray4,cable_tray3):
        frr_to_tray_option1 = abs(someFrrGridNum - cable_tray1)
        frr_to_tray_option2 = abs(someFrrGridNum - cable_tray2)
    elif someFrrGridNum in range(cable_tray6,cable_tray5):
        frr_to_tray_option1 = abs(someFrrGridNum - cable_tray1)
        frr_to_tray_option2 = abs(someFrrGridNum - cable_tray2)

    finalOption1 = rack_to_tray_option1 + frr_to_tray_option1 + frr_vertical_dist1
    finaloption2 = rack_to_tray_option2 + frr_to_tray_option2 + frr_vertical_dist1

    if finalOption1 > finaloption2:
        final = finaloption2
    else:
        final = finalOption1
    return final

horizontal_to_relay1 = find_horizontal(userGridNum,your_FrrPair_1_num)
print(horizontal_to_relay1)



    




