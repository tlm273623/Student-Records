
# Description:  This program provides a menu for the user.  The menu asks the user whether they want to
#create, show, delete, show all records, or exit the program.  Once a number is entered by the user, the user is met
#with a display that outlines what they have chosen.  Then, user is asked to type in a last name.
# Input: Input a number on the selection menu to decide what you would like to choose from the selection list
#and then enter in the last name of a student that you would like to act on.

# Output:
'''
The output is based on what the user types in.  If the user enters in a one then the program states that the user 
wants to create a new record, 2 states that the user wants to show a record, 3 illustrates that the user wants to
delete a record, 4 anounces that the user wants to show all records, and, finally, 5 anounce that the program
is being exited.  If any other input is put in by the user and error will occur and the user will be asked to try again.
'''
# Additional Comments:
'''
Only enter in character and only enter in integers wherever necessary.  if not, then an error will be introduced
to the user.  
'''
try:
    import time
    import os
    myList = []
    myDict = {}
    lastList = []

    def option1():
        print('You chose to create a new record!\n')
        try:
                studentID = int(input("Enter student ID: "))
                firstName = input("Enter first name: ")
                lastName = input("Enter last name: ")
                age = int(input("Enter age: "))
                address = input("Enter address: ")
                phone = int(input("Enter phone number: "))
                u = 1
        except:
                print('\nInvalid selection, please type in integers or characters only when necessary!\n')
                main()


        print()
        print('Student has been put into the system!')
        print()
        decision = int(input('Press \'1\' to exit to main page or \'2\' to create another record: '))
        print()
        o = 0
        while o == 0:
            if decision == 1:
                o += 1
                print('Exiting to main page...')
            elif decision == 2:
                o += 1
                option1()
            else:
                o = 0
                print('Please enter a \'1\' or \'2\'!')
                print()
                decision = int(input('Press \'1\' to exit to main page or \'2\' to show another record: '))
                print()


        with open('file_records.txt', 'a') as infile:
            global myList
            global  myDict
            # myDict = {'Student ID:':studentID,'First name:':firstName,'Last name:':lastName,'Age:':age,'Address:':address, 'Phone':phone}

            myList = [
               str(studentID),
               firstName,
               lastName,
               str(age),
               address,
               str(phone)]
            infile.write(str(myList)+'\n')
            # infile.write('\n')
            # infile.write(str(studentID) + '\n')
            # infile.write(firstName + '\n')
            # infile.write(lastName + '\n')
            # infile.write(str(age) + '\n')
            # infile.write(address + '\n')
            # infile.write(str(phone) + '\n')

        with open('LastNameRecords.txt','a') as lastRecords:
            global lastList
            lastList = [
                lastName
            ]
            lastRecords.write(str(lastList) + '\n')




    def option2():
        count = 0
        x = 0
        print('You chose to show a record!\n')
        while count == 0:
            user = input('Enter last name of student: ')
            print()
            with open('LastNameRecords.txt','r') as lastname:
                contents = lastname.read()
                #------------------------------------------------
                with open('LastNameRecords.txt', 'r') as thelast:
                    enter = thelast.readlines()
                    p = 0
                    for i in enter:
                            if user == (i.replace("'", "").replace("[", "").replace("]", "").strip()):
                                x = 1
                                break
                            else:
                                x = 0
                                continue

                if x == 1:
                    print('Record found!')
                    print()
                    with open('file_records.txt', 'r') as infile:
                        access = infile.readlines()
                        for line in access:
                            if line.find(user) != -1:
                                theList = []
                                theList.append(line.strip().split())
                                print("Student ID: " + theList[0][0].strip().replace("[", "").replace("\'", "").replace(",", ""))
                                print("First name: " + theList[0][1].strip().replace("[", "").replace("\'", "").replace(",", ""))
                                print("Last Name: " + theList[0][2].strip().replace("[", "").replace("\'", "").replace(",", ""))
                                print("Age: " + theList[0][3].strip().replace("[", "").replace("\'", "").replace(",", ""))
                                print("Address: " + theList[0][4].strip().replace("[", "").replace("\'", "").replace(",", ""))
                                print("Phone: " + theList[0][5].strip().replace("]", "").replace("\'", "").replace(",", ""))
                                print()
                                decision = int(input('Press \'1\' to exit to main page or \'2\' to show another record: '))
                                print()
                                o = 0
                                while o == 0:
                                    if decision == 1:
                                        count += 1
                                        o += 1
                                        print('Exiting to main page...')
                                        print()
                                    elif decision == 2:
                                        count = 0
                                        o += 1
                                    else:
                                        o = 0
                                        print('Please enter a \'1\' or \'2\': ')
                                        print()
                                        decision = int(input('Press \'1\' to exit to main page or \'2\' to show another record: '))
                                        print()




                else:
                    print("Record not found!")
                    print()
                    prompt = int(input('Press \'1\' to exit to main page or \'2\' to try again: '))
                    print()
                    z = 0
                    while z == 0:
                        if prompt == 1:
                            count += 1
                            z += 1
                            print('Exiting to main page...')
                            print()
                        elif prompt == 2:
                            count = 0
                            z+=1
                        else:
                            z = 0
                            print('Please enter a \'1\' or \'2\': ')
                            print()
                            prompt = int(input('Press \'1\' to exit to main page or \'2\' to try again: '))
                            print()

    def remove_file(retries=3, sleep=0.1):
        for i in range(retries):
            try:
                os.remove('file_records.txt')
            except WindowsError:
                time.sleep(sleep)
                break

    def remove_file_lasts(retries=3, sleep=0.1):
        for i in range(retries):
            try:
                os.remove('LastNameRecords.txt')
            except WindowsError:
                time.sleep(sleep)
                break

    def option3():
        count = 0
        x = 0
        while count == 0:
            print("You chose to delete a record!\n")
            user = input('Enter last name of student: ')
            with open('LastNameRecords.txt', 'r') as lastname:
                contents = lastname.read()
                with open('LastNameRecords.txt', 'r') as thelast:
                    enter = thelast.readlines()
                    for i in enter:
                        (i.replace("'", "").replace("[", "").replace("]", "").strip())
                        if user == (i.replace("'", "").replace("[", "").replace("]", "").strip()):
                            x = 1
                if x == 1:
                    print()
                    print('Record found and deleted!\n')
                    with open('file_records.txt', 'r') as infile:
                        access = infile.readlines()
                        for line in access:
                            if line.find(user) != -1:
                                with open('file_records.txt', 'r') as infile, open('next.txt','a') as nextfile:
                                    for newline in infile:
                                        if newline != line:
                                            nextfile.write(newline)
                                with open('LastNameRecords.txt', 'r') as lastname, open('newlasts.txt', 'a') as newlasts:
                                            enter = lastname.readlines()
                                            for i in enter:
                                                if (i.replace("'","").replace("[","").replace("]","").strip())  != user:
                                                    newlasts.write(i)
                    k = 0
                    while k == 0:
                        try:
                            decision = int(input('Press \'1\' to exit to main page or \'2\' to show another record: '))
                            print()
                            o = 0
                            while o == 0:
                                if decision == 1:
                                    count += 1
                                    o += 1
                                    k=1
                                    print('Exiting to main page...')
                                    print()
                                elif decision == 2:
                                    count = 0
                                    o += 1
                                    k=1
                                else:
                                    o = 0
                                    print('Please enter a \'1\' or \'2\': ')
                                    print()
                                    decision = int(input('Press \'1\' to exit to main page or \'2\' to show another record: '))
                                    print()
                        except:
                            print('Only enter in integers!\n')
                            k=0

                else:
                    print()
                    print("Record not found!")
                    newCount = 0
                    while newCount == 0:
                        try:
                            print()
                            prompt = int(input('Press \'1\' to exit to main page or \'2\' to try again: '))
                            print()
                            z = 0
                            while z == 0:
                                if prompt == 1:
                                    count += 1
                                    z += 1
                                    newCount = 1
                                    print('Exiting to main page...')
                                    print()
                                elif prompt == 2:
                                    count = 0
                                    z += 1
                                    newCount = 1
                                else:
                                    z = 0
                                    print('Please enter a \'1\' or \'2\': ')
                                    print()
                                    prompt = int(input('Press \'1\' to exit to main page or \'2\' to try again: '))
                                    print()
                        except:
                            newCount = 0
                            print('\nOnly enter in integers!')

            if x == 1:
                remove_file_lasts()
                os.rename("newlasts.txt", "LastNameRecords.txt")
                open('newlasts.txt', 'x')
                remove_file()
                os.rename("next.txt", "file_records.txt")
                open('next.txt', 'x')



                
    def option4():
        print("You chose to show all records!")

        with open('LastNameRecords.txt', 'r') as lastname:
            contents = lastname.readlines()
            contents.sort()
            newList = []
            for i in (contents):
                newList.append(i.strip().replace("[", "").replace("\'", "").replace(",", "").replace(']',''))
            for i in newList:
                with open('file_records.txt', 'r') as infile:
                    access = infile.readlines()
                    for p in access:
                        theList = []
                        theList.append(p.strip().split())
                        if (theList[0][2].strip().replace("[", "").replace("\'", "").replace(",", "")) == i:
                            print("Student ID: " + theList[0][0].strip().replace("[", "").replace("\'", "").replace(",", ""))
                            print("First name: " + theList[0][1].strip().replace("[", "").replace("\'", "").replace(",", ""))
                            print("Last Name: " + theList[0][2].strip().replace("[", "").replace("\'", "").replace(",", ""))
                            print("Age: " + theList[0][3].strip().replace("[", "").replace("\'", "").replace(",", ""))
                            print("Address: " + theList[0][4].strip().replace("[", "").replace("\'", "").replace(",", ""))
                            print("Phone: " + theList[0][5].strip().replace("]", "").replace("\'", "").replace(",", ""))
                            print()



    def main():
        count = 0
        while count == 0:
            try:
                choice1 = 0
                while choice1 != 5:

                    display_menu()
                    if os.stat("file_records.txt").st_size == 0:
                        choice1 = int(input('Enter your choice: '))
                        print()
                        if choice1 == 1:
                            option1()
                            count = 1
                        elif choice1 == 2:
                            print('There are no records in the system, please create one first (option 1).')
                            print()
                            count = 1
                        elif choice1 == 3:
                            print('There are no records in the system, please create one first (option 1).')
                            print()

                        elif choice1 == 4:
                            print('There are no records in the system, please create one first (option 1).')
                            print()
                        elif choice1 == 5:
                            print('Exiting the program. . .')
                            print()
                            count = 1
                        else:
                            print('Error: invalid selection, please try again.')
                            print()
                    else:
                        choice1 = int(input('Enter your choice: '))
                        print()
                        if choice1 == 1:
                            option1()
                            count = 1
                        elif choice1 == 2:
                            option2()
                            count = 1
                        elif choice1 == 3:
                            option3()
                            count = 1
                        elif choice1 == 4:
                            option4()
                            count = 1
                        elif choice1 == 5:
                            print('Exiting the program. . .')
                            print()
                            count = 1
                        else:
                            print('Error: invalid selection, please try again.')
                            print()
            except:
                c = 0
                print()
                print('Invalid, please only type in integers.\n')
                prompt = int(input("Press '1' to reboot program or '2' to leave: "))
                print()
                while c == 0:
                    if prompt == 1:
                        count = 0
                        c = 1
                    elif prompt == 2:
                        c = 1
                        count = 1
                        print()
                        print("Exiting program...\n")
                    else:
                        print("Invalid selection, please only select a '1' or a '2': ")
                        c = 0


    def display_menu():
        print('**********************************************\n')
        print('RECORDS MANAGER\n')
        print('**********************************************\n')
        print('1. Create a new record.')
        print('2. Show a record.')
        print('3. Delete a record.')
        print('4. Display All Records')
        print('5. Exit')

    main()

except:
    print()
    print('Something went wrong, exiting program...')