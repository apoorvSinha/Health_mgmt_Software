def edit_data(patient, Health_chart):
    if Health_chart == 1:
        '''Go to diet'''
        if patient == 1:
            '''open diet for patient 1'''
            file = open('Diet_P_HT001.txt','a')
        elif patient == 2:
            '''open diet for patient 2'''
            file = open('Diet_P_HT002.txt','a')
        elif patient == 3:
            '''open diet for patient 3'''
            file = open('Diet_P_HT003.txt','a')

        inp4 = input('Type \'enter\' to input deit plan and \'exit\' to exit to stop writing: ')
        while True:
            inp5 = input('Enter the details of Diet you want to enter as above format: ')
            if inp5 == 'exit':
                break
            file.write('\n')
            file.write(inp5)

    elif Health_chart == 2:
        '''Go to Exercise'''
        if patient == 1:
            '''open exercise for patient 1'''
            file = open('Exercise_P_HT001.txt','a')
        elif patient == 2:
            '''open exercise for patient 2'''
            file = open('Exercise_P_HT002.txt','a')
        elif patient == 3:
            '''open exercise for patient 3'''
            file = open('Exercise_P_HT003.txt','a')
        inp6 = input('Type \'enter\' to input deit plan and \'exit\' to exit to stop writing: ')
        while True:
            inp7 = input('Enter the details of Diet you want to enter as above format: ')
            file.write('\n\n',inp7)
            if inp7 == 'exit':
                break


def view_data(patient, Health_chart):
        if Health_chart == 1:
            #Goto Diet
            if patient == 1:
                '''open diet for patient 1'''
                file = open('Diet_P_HT001.txt')
            elif patient == 2:
                '''open diet for patient 2'''
                file = open('Diet_P_HT002.txt')
            elif patient == 3:
                '''open diet for patient 3'''
                file = open('Diet_P_HT003.txt')

            content = file.readlines()
            print('Diet chart for saturday is: \n')
            for i in range(10):
                print(content[i])
            print('Diet chart for saturday is: \n')
            for j in range(10, 20):
                print(content[j])

        elif Health_chart == 2:
            #Goto Exercise
            if patient == 1:
                '''open exercise for patient 1'''
                file = open('Exercise_P_HT001.txt')
            elif patient == 2:
                '''open exercise for patient 2'''
                file = open('Exercise_P_HT002.txt')
            elif patient == 3:
                '''open exercise for patient 3'''
                file = open('Exercise_P_HT003.txt')

            content = file.readlines()
            print('Diet chart for saturday is: \n')
            for i in range(6):
                print(content[i])
            print('Diet chart for saturday is: \n')
            for j in range(6, 12):
                print(content[j])



#To prevent invalid input
while True:
    try:
        print('Welcome to harry_tut weight Loss services\n\n')
        print('Customer names are:\n1. Rajesh\n2. Rohan\n3. Raj\n')
        inp1 = int(input('Enter the number in front of name of the patient to lock data: '))
        inp2 = int(input('Press 1 to go into Diet or 2 to goto Exercise: '))
        inp3 = int(input('Press 1 to view or 2 to edit Patient\'s data: \n'))
        if inp3 == 2:
            edit_data(inp1, inp2)
        elif inp3 == 1:
            view_data(inp1, inp2)
    except:
        print('Not a valid option')

