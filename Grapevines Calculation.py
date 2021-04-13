print('This program will calculate: \n\n\
How many grapevines will fit in a row based on length of row, space used by an end-post assembly, and space between vines.')
print()

import numbers

def grapeVine():
    rowLength = ''

    while isinstance(rowLength, float) == False:

        try:
            rowLength = float(input('Please enter the heigh of your row. (in feet) \n'))

            if isinstance(rowLength, float) == True:
                print()
                print('You have entered a row Length of ' + str(rowLength) + ' ft.')
                postSpaceUsed = ''
                print()
        except ValueError:
            print('\nPlease enter your row in numerical format.')

    while isinstance(postSpaceUsed, float) == False:
        
        try:
            postSpaceUsed = float(input('Please enter the amount of space used by an end-post assembly. (in feet)\n'))

            if isinstance(postSpaceUsed, float) == True:
                print()
                print('You have entered ' + str(postSpaceUsed) + ' ' + 'ft as the space used by your end-post assembly.')
                spaceBetweenVines = ''
                print()
                
        except ValueError:
            print('\nPlease enter your space used by end-post in numerical format.')

    while isinstance(spaceBetweenVines, float) == False:

        try:
            spaceBetweenVines = float(input('Please enter the amount of space between vines. (in feet)\n'))

            if isinstance(spaceBetweenVines, float) == True:
                print()
                print('You have entered ' + str(spaceBetweenVines) + ' ft. as the space between your vines.')

        except ValueError:
                print()
                print('Please enter a numerical value for the space between your vines.')
                print()
                
    #Formula to calculate how many grapevines will fit in row:   
    grapevinesFitInRow = (rowLength - ((2.0 * postSpaceUsed) / spaceBetweenVines))
    print()
    print('The total number of grapevines that will fit in your row are: ' + str(grapevinesFitInRow) + ' grapevines.')

grapeVine()
print()

#Asks user if they want to make another calculation:
anotherCalculation = '?'

while anotherCalculation != 'yes' or anotherCalculation != 'no':
    anotherCalculation = input('Would you like to make another calculation? type: yes/no \n').lower()
    if anotherCalculation == 'yes':
        print()
        print()
        print()
        grapeVine()
    if anotherCalculation =='no':
        print()
        print('Thank you. Goodbye')
        break