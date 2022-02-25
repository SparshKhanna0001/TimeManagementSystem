import os 
import numpy as np
import pandas as pd
import matplotlib as pyplt
import datetime 

#importing colorama: module for producing colored terminal test and styling
import colorama
from colorama import Fore, Style, init

#initialising colorama for windows systems
init(autoreset=True)


""" Functions """

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def choice_validator(input):

    if input not in ('0','1','2','3','4','5','6','7','8','9'):
        clear_screen()
        print('{Fore.RED}{Style.BRIGHT}Invalid input provided !')
        print('\n')
        return False

def absolute_path_maker(filename):
    abs_path = os.getcwd() + '\\' + filename
    return abs_path 

def time_slot_validator(start_time, end_time):
    start_time_list_format = start_time.split(':')
    end_time_list_format = end_time.split(':')
    
    if int(start_time_list_format[0]) > int(end_time_list_format[0]):
        return False
    elif int(start_time_list_format[0]) == int(end_time_list_format[0]):
        if int(start_time_list_format[1]) >= int(end_time_list_format[1]):
            return False
        else:
            return True
    else:
        return True

def main(times_executed):


    if times_executed == 0:
        print(f'{Style.BRIGHT}TIME MANAGEMENT SYSTEM')

    print('Type in the required operation')

    print(f'{Fore.GREEN}[1]  {Style.RESET_ALL}Add tasks')
    print(f'{Fore.GREEN}[2]  {Style.RESET_ALL}Update task status ')
    print(f'{Fore.GREEN}[3]  {Style.RESET_ALL}View tasks') 
    print(f'{Fore.GREEN}[4]  {Style.RESET_ALL}Delete tasks' )
    print(f'{Fore.GREEN}[5]  {Style.RESET_ALL}Graphs ')
    print(f'{Fore.GREEN}[6]  {Style.RESET_ALL}Help ')
    print(f'{Fore.GREEN}[7]  {Style.RESET_ALL}Quit ')
    
    
    csv_file = pd.read_csv(absolute_path_maker('tasks.csv'))

    #choice = input('> ')
    choice = '5'
    if choice_validator(choice) == False:
        main(times_executed=1)

    if choice == '0':
        clear_screen()
        print('Good Bye!')
        exit(0)

    elif choice == '1':
        clear_screen()
        taskname = input('Taskname: \n> ')
        description = input('\nDescription (optional) \n>')
        date = input(f'\nScheduled Date \n  {Fore.CYAN}Format : DD-MM-YYYY {Style.RESET_ALL}  \n>')
        status = 'pending'
        sr_no = int(np.array(csv_file.tail(1)['Sr. No'])[0]) + 1
            
        def start_time_input():
            start_time = input(f'\nEnter start time \n  {Fore.CYAN}Format : HH:MM (24 hour format){Style.RESET_ALL} \n   >')
            return start_time

        def end_time_input():
            end_time =  input(f'\nEnter end time \n  {Fore.CYAN}Format  : HH:MM (24 hour format) {Style.RESET_ALL} \n    >')
            return end_time
        
        start_time = start_time_input()
        end_time = end_time_input()

        while not time_slot_validator(start_time, end_time):
            print(f'{Fore.RED}Please enter a valid time slot !\n')
            start_time = start_time_input()
            end_time = end_time_input()
            
        data = {'Sr. No':sr_no,'Tasks':taskname,'Description':description,'Scheduled Date':date,'Start Time':start_time,'End Time':end_time,'Status(pending/done)':status}
        data_df = pd.DataFrame(data, index=[sr_no]) 
        csv_file = pd.concat([csv_file,data_df], ignore_index=True)
        csv_file.to_csv(absolute_path_maker('tasks.csv'), index=False)
        
        input('Press ENTER to continue.\n>')
        main(times_executed=1)

    elif choice == '2':
        sr_no_input = int(input("Enter serial number of task whose status is to be updated: \n"))

        #Turning oof the SettingWithCopyWarning  (Below line)
        pd.set_option('mode.chained_assignment', None)

        csv_file['Status(pending/done)'][sr_no_input-1] = 'done'
        csv_file.to_csv(absolute_path_maker('tasks.csv'), index=False)
        print(csv_file)
	
        input('Press ENTER to continue.\n>')
        main(times_executed=1)

    elif choice == '3':
        print("Enter required option:- ")
        print(f" {Fore.GREEN}(a) {Style.RESET_ALL}Show today's schedule")
        print(f" {Fore.GREEN}(b) {Style.RESET_ALL}Show from serial number ...:")
        print(f" {Fore.GREEN}(c) {Style.RESET_ALL}Show all pending tasks .")
        print(f" {Fore.GREEN}(d) {Style.RESET_ALL}Show all completed tasks ")
        print(f" {Fore.GREEN}(e) {Style.RESET_ALL}Show all tasks ")

        def choice_for3_func():
            choice_for3 = input(">")
            return choice_for3
        
        choice_for3 = choice_for3_func()
        
        if choice_for3 not in ('a','b','c','d','e'):
            print('{Fore.RED}IInvalid options !')
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
                today = today + i + '-'

            today = today[:len(today)-1]
            
            condition = csv_file['Scheduled Date'] == today
            print(csv_file[condition])
            
            input('Press ENTER to continue.\n>')
            main(times_executed=1)
            
        elif choice_for3.lower() == 'b':
            sr_no_input = int(input("Enter serial number: \n"))
            condition = csv_file['Sr. No'] >= sr_no_input
            print(csv_file[condition])

            input('Press ENTER to continue.\n>')
            main(times_executed=1)
            
        elif choice_for3.lower() == 'c':
            condition = csv_file['Status(pending/done)'] == 'pending'
            print(csv_file[condition])
            
            input('Press ENTER to continue.\n>')
            main(times_executed=1)

        elif choice_for3.lower() == 'd':
            condition = csv_file['Status(pending/done)'] == 'done'
            print(csv_file[condition])
            
            input('Press ENTER to continue.\n>')
            main(times_executed=1)

        elif choice_for3.lower() == 'e':
            print(csv_file)

            input('Press ENTER to continue.\n>')
            main(times_executed=1)
    
    elif choice == '4':
        sr_no_input = int(input("Enter serial number of task whose status is to be updated: \n"))
        csv_file = csv_file.drop(csv_file[sr_no_input]-1)

        input('Press ENTER to continue.\n>')
        main(times_executed=1)
    

    elif choice == '5':
        print("Enter required option:- ")
        
        """FUNCTIONS"""

        def order_by_dates(data_dataframe): # num_of_unique_enteries_reqd):
            
            def filter_unique(data):
                filtered_list = []
                for x in data:
                    if x not in filtered_list:
                        filtered_list.append(x)
                return filtered_list

            def sorting_function(data_dataframe):
                """Sorting out future dates"""
                dates = list(data_dataframe['Scheduled Date'])
                dates = lambda date: datetime.datetime.strptime(date, '%d-%m%-%Y')
                
                today = datetime.date.today()
                condition_list = []

                for date in dates:
                    if date > today:
                        condition_list.append(False)
                    else:
                        condition_list.append(True)

                data_dataframe = data_dataframe[condition_list]
                
                """Selecting the recent seven date entries"""
                dates = list(data_dataframe['Scheduled Date'])
                dates.sort(key = lambda date: datetime.datetime.strptime(date, '%d-%m-%Y')) 
                dates.reverse()
                condition_list = []
                
                unique_dates = filter_unique(dates)

                while len(unique_dates) > 7:
                    del min(dates)
                    unique_dates = filter_unique(dates)
                
                for date in list(data_dataframe['Scheduled Date']):
                    if date in dates:
                        condition_list.append[True]
                    else:
                        condition_list.append[False]

                data_dataframe = data_dataframe[condition_list]





            #dates = list(data_dataframe['Scheduled Date'])
            #dates = filter_unique(dates)
            #print(dates)
            #dates.reverse()
            #print(dates)
            #print(type(dates[0]))
            #dates.sort(key = lambda date: datetime.strptime(date, '%
        order_by_dates(csv_file)


    #elif choice == '6':

if __name__ == '__main__': 
    main(times_executed=0)

