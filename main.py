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

def absolute_path_maker(filename):
    abs_path = os.getcwd() + '\\' + filename
    return abs_path 

def main(times_executed):


    if times_executed == 0:
        print(f'TIME MANAGEMENT SYSTEM')

    print('Type in the required operation')

    print('[1]  Add tasks')
    print('[2]  Update task status ')
    print('[3]  View tasks') 
    print('[4]  Delete tasks' )
    print('[5]  Graphs ')
    print('[6]  Help ')
    print('[7]  Quit ')
    
    csv_file = pd.read_csv(absolute_path_maker('tasks.csv'))

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
        csv_file = pd.concat([csv_file,data_df], ignore_index=True)
        csv_file.to_csv(absolute_path_maker('tasks.csv'), index=False)
        

    elif choice == '2':
        sr_no_input = int(input("Enter serial number of task whose status is to be updated: \n"))

        #Turning oof the SettingWithCopyWarning  (Below line)
        pd.set_option('mode.chained_assignment', None)

        csv_file['Status(pending/done)'][sr_no_input-1] = 'done'
        csv_file.to_csv(absolute_path_maker('tasks.csv'), index=False)
        print(csv_file)

    elif choice == '3':
        print("Enter required option:- ")
        print(" (a) Show today's schedule")
        print(" (b) Show from serial number ...:")
        print(" (c) Show all pending tasks .")
        print(" (d) Show all completed tasks ")
        print(" (e) Show all tasks ")

        def choice_for3_func():
            choice_for3 = input(">")
            return choice_for3
        
        choice_for3 = choice_for3_func()

        if choice_for3 not in ('a','b','c','d','e'):
            print('Invalid options !')
            print('Valid options: a, b, c, d and e')
            print('Want to continue ?  (Y/n) ')
            confirmation = input('>')
            if confirmation.lower() == 'y':
                choice_for3_func()
            else:
                main(times_executed=1)
        
        if choice_for3.lower() == 'a':
            today = ""
            date_in_list_format = str(datetime.date.today()).split('-')
            for i in date_in_list_format[::-1]:
                today += i

            condition = csv_file['Scheduled Date'] == np.dtype('int64').type(today)
            print(csv_file[condition])
            
        elif choice_for3.lower() == 'b':
            sr_no_input = int(input("Enter serial number: \n"))
            condition = csv_file['Sr. No'] >= sr_no_input
            print(csv_file[condition])
            
        elif choice_for3.lower() == 'c':
            condition = csv_file['Status(pending/done)'] == 'pending'
            print(csv_file[condition])

        elif choice_for3.lower() == 'd':
            condition = csv_file['Status(pending/done)'] == 'done'
            print(csv_file[condition])

        elif choice_for3.lower() == 'e':
            print(csv_file)
    
    elif choice == '4':
        sr_no_input = int(input("Enter serial number of task which you want to get deleted: \n"))
        
        
if __name__ == '__main__': 
    main(times_executed=0)
