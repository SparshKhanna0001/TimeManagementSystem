import os 
import numpy as np
import pandas as pd
import matplotlib as pyplt
import datetime 


""" Functions """

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def choice_validator(input):

    if input not in ('0','1','2','3','4','5','6','7','8','9'):
        clear_screen()
        print('Invalid input provided !')
        print('\n')
        return False

#def absolute_path_maker(filename):
 #   abs_path = os.getcwd() + '\\' + filename
  #  return abs_path 

def main(times_executed):


    if times_executed == 0:
        print(f'TIME MANAGEMENT SYSTEM')

    print('Type in the required operation')

    print('[1]  Add tasks')
    print('[2]  Edit task status ')
    print('[3]  View tasks') 
    print('[4]  Delete tasks' )
    print('[5]  Graphs ')
    print('[6]  Help ')
    print('[7]  Quit ')
    
    csv_file = pd.read_csv(r'C:\Users\pooja\school_project\tasks.csv')

    choice = input('> ')
    if choice_validator(choice) == False:
        main(times_executed=1)

    if choice == '0':
        clear_screen()
        print('Good Bye!')
        exit(0)

    elif choice == '1':
        clear_screen()
        taskname = input('Taskname: \n> ')
        print()
        description = input('Description (optional) \n>')
        print()
        date = input('Scheduled Date \n  Format : DDMMYYY  \n>')
        print()
        estimated_time= input('Enter estimated time required to do the task(in mins): \n>')
        
        status = 'pending'
        sr_no = int(np.array(csv_file.tail(1)['Sr. No'])[0]) + 1
        data = {'Sr. No':sr_no,'Tasks':taskname,'Description':description,'Scheduled Date':date,'Estimated Time':estimated_time,'Status(pending/done)':status}
        data_df = pd.DataFrame(data, index=[sr_no]) 
        print(data_df)
        csv_file = pd.concat([csv_file,data_df], ignore_index=True)
        print(csv_file)
        csv_file.to_csv(r'C:\Users\pooja\school_project\tasks.csv', index=False)

    elif choice == '2':
        sr_no_input = int(input("Enter serial number of task whose status is to be updated: \n"))
        print()

    elif choice == '3':
        print("Enter required option:- ")
        print(" (a) Show today's schedule")
        print(" (b) Show from serial number ...:")
        print(" (c) Show all pending tasks .")
        print(" (d) Show all completed tasks ")
        print(" (e) Show all tasks ")

        def choice_for3_func():
            choice_for3 = input(">")
        
        choice_for3_func()

        if choice_for3 not in ('a','b','c','d','e'):
            print('Invalid options !')
            print('Valid options: a, b, c and d')
            print('Want to continue ?  (Y/n) ')
            confirmation = input('>')
            if confirmation.lower() == 'Y':
                choice_for3_func()
            else:
                main(times_executed=1)

        if choice_for3 == 'b':
            sr_no_input = int(input("Enter serial number: \n"))
            print(csv_file('Sr. No') >= sr_no_input)

        elif choice_for3 == 'c':
            print(csv_file('Status(pending/done)' == 'pending'))

        elif choice_for3 == 'd':
            print(csv_file('Status(pending/done)' == 'done'))

        elif choice_for3 == 'e':
            print(csv_file)
        




if __name__ == '__main__': 
    main(times_executed=0)

