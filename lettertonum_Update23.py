from optparse import Option
from pydoc import doc
import pandas as pd
import numpy as np
import re
#Read excel file into pandas dataframe
df = pd.read_excel("FRR.xlsx","Grid")

#numerical variables
cable_tray1 = 94
cable_tray2 = 74
cable_tray3 = 65
cable_tray4 = 40
cable_tray5 = 23
cable_tray6 = 11

harness_slack = 6

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
        option1 = (2*abs(int(someGridNum - cable_tray5)))+2
        option2 = (2*abs(int(someGridNum - cable_tray6)))+2
    elif alley == 2:
        option1 = (2*abs(int(someGridNum - cable_tray3)))+2
        option2 = (2*abs(int(someGridNum - cable_tray4)))+2
    elif alley == 3:
        option1 = (2*abs(int(someGridNum - cable_tray1)))+2
        option2 = (2*abs(int(someGridNum - cable_tray2)))+2
    return option1,option2

#Call function to find the two distance options from cabinet grid to left and right outer rail paths
cab_to_your_tray1 = find_horizonstal_harness_dist(int(userGridNum))[0]#This was userGridNum going to try your_frrPair_2_num
cab_to_your_tray2 = find_horizonstal_harness_dist(int(userGridNum))[1]
print(f'Rack location to cable tray distance: {cab_to_your_tray1}')
print(f'Rack location to cable tray distance: {cab_to_your_tray2}')

#Call the function to find the two distance options from the FRR pairs to the left and right outer rails
frr1_to_your_tray2 = find_horizonstal_harness_dist(int(your_FrrPair_1_num))[0]
frr1_to_your_tray1 = find_horizonstal_harness_dist(int(your_FrrPair_1_num))[1]
print(f'FRR1 location to cable tray distance: {frr1_to_your_tray1}')
print(f'FRR1 location to cable tray distance: {frr1_to_your_tray2}')

frr2_to_your_tray1 = find_horizonstal_harness_dist(int(your_FrrPair_2_num))[0]
frr2_to_your_tray2 = find_horizonstal_harness_dist(int(your_FrrPair_2_num))[1]
print(f'FRR2 location to cable tray distance: {frr2_to_your_tray1}')
print(f'FRR2 location to cable tray distance: {frr2_to_your_tray2}')



final_to_frr2_option1 = frr_vertical_dist2 + cab_to_your_tray1 + frr2_to_your_tray1 - 4
final_to_frr2_option2 = frr_vertical_dist2 + cab_to_your_tray2 + frr2_to_your_tray2 - 4

final_to_frr1_option1 = frr_vertical_dist1 + cab_to_your_tray1 + frr1_to_your_tray1 - 4
final_to_frr1_option2 = frr_vertical_dist1 + cab_to_your_tray2 + frr1_to_your_tray2 - 4

if alley == 3:
    tray_num1 = 97
    tray_num2 = 74
    print
elif alley == 2:
    tray_num1 = 65
    tray_num2 = 40
    print
elif alley == 1:
    tray_num1 = 23
    tray_num2 = 11

#rint(f'Total distance to FRR1 option 1: {final_to_frr1_option1} via cable tray {tray_num1}')
#print(f'Total distance to FRR1 option 2: {final_to_frr1_option2} via cable tray {tray_num2}')
print(f'frr_vertical_dist1 = {frr_vertical_dist1}')
print(f'cab_to_your_tray1 = {cab_to_your_tray1}')
print(f'frr1_to_your_tray1 = {frr1_to_your_tray1}')

print(f'Total distance to FRR2 option 1: {final_to_frr2_option1} via cable tray {tray_num1}')
print(f'Total distance to FRR2 option 2: {final_to_frr2_option2} via cable tray {tray_num2}')

print(f'frr1 option 1: {final_to_frr1_option1}')
print(f'frr1 option 2: {final_to_frr1_option2}')

print("Values:")
print(f'frr vertical dist {frr_vertical_dist2}') #Good
print(f'cab to your tray1:{cab_to_your_tray1}')
print(f'cab to your tray2:{cab_to_your_tray2}')
print(f'FRR2 to your tray1:{frr2_to_your_tray1}')
print(f'FRR2 to your tray2:{frr2_to_your_tray2}')

print(f'cab to tray 1 is {cab_to_your_tray1}')
print(f'cab to tray 2 is {cab_to_your_tray2}')

#cab to tray 2 should be 7*2 = 14
#cab to tray 1 should be 15*2 = 30


print(your_FrrPair_2_num)