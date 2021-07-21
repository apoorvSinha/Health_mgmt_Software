def edit_data(patient, Health_chart):
    if Health_chart == 1:
        '''Go to diet'''
        if patient == 1:
            '''open diet for patient 1'''

        elif patient == 2:
            '''open diet for patient 2'''

        elif patient == 3:
            '''open diet for patient 3'''

    elif Health_chart == 2:
        '''Go to Exercise'''
        if patient == 1:
            '''open exercise for patient 1'''
        elif patient == 2:
            '''open exercise for patient 2'''
        elif patient == 3:
            '''open exercise for patient 3'''

    else:
        edit_data(patient, Health_chart)
    return 0


def view_data(patient, Health_chart):
    if Health_chart == 1:
        '''Go to diet'''
        if patient == 1:
            '''open diet for patient 1'''
            with open('Diet_P_HT001.txt') as file:
                content = file.readlines()
                print('Diet chart for saturday is: \n')
                for i in range(10):
                    print(content[i])
                print('Diet chart for saturday is: \n')
                for j in range(10, 20):
                    print(content[j])
        elif patient == 2:
            '''open diet for patient 2'''
            with open('Diet_P_HT002.txt') as file:
                content = file.readlines()
                print('Diet chart for saturday is: \n')
                for i in range(10):
                    print(content[i])
                print('Diet chart for saturday is: \n')
                for j in range(10, 20):
                    print(content[j])
        elif patient == 3:
            '''open diet for patient 3'''
            with open('Diet_P_HT003.txt') as file:
                content = file.readlines()
                print('Diet chart for saturday is: \n')
                for i in range(10):
                    print(content[i])
                print('Diet chart for saturday is: \n')
                for j in range(10, 20):
                    print(content[j])

    elif Health_chart == 2:
        '''Go to Exercise'''
        if patient == 1:
            '''open exercise for patient 1'''
            with open('Exercise_P_HT001.txt') as file:
                content = file.readlines()
                print('Diet chart for saturday is: \n')
                for i in range(6):
                    print(content[i])
                print('Diet chart for saturday is: \n')
                for j in range(6, 12):
                    print(content[j])
        elif patient == 2:
            '''open exercise for patient 2'''
            with open('Exercise_P_HT002.txt') as file:
                content = file.readlines()
                print('Diet chart for saturday is: \n')
                for i in range(6):
                    print(content[i])
                print('Diet chart for saturday is: \n')
                for j in range(6, 12):
                    print(content[j])
        elif patient == 3:
            '''open exercise for patient 3'''
            with open('Exercise_P_HT003.txt') as file:
                content = file.readlines()
                print('Diet chart for saturday is: \n')
                for i in range(6):
                    print(content[i])
                print('Diet chart for saturday is: \n')
                for j in range(6, 12):
                    print(content[j])
    else:
        view_data(patient, Health_chart)
    return 0


print('Welcome to harry_tut weight Loss services\n\n')
print('Customer names are:\n1. Rajesh\n2. Rohan\n3. Raj\n')

inp1 = int(input('Enter the number in front of name of the patient to lock data: '))
inp2 = int(input('Press 1 to go into Diet or 2 to goto Exercise: '))
inp3 = int(input('Press 1 to view or 2 to edit Patient\'s data: \n'))

if inp3 == 2:
    edit_data(inp1, inp2)
elif inp3 == 1:
    view_data(inp1, inp2)
else:
    inp3 = int(input('Press 1 to view or 2 to edit Patient\'s data: \n'))
