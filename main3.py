import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
    abs_path = os.path.abspath(os.path.dirname(__file__)) + '\\' + filename
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

def date_validator(date):
    
    if type(date) != str:
        return False
    
    elif len(date) != 10:
        return False
   
    elif date[2] != '-' and date[4] != '-':
        return False

    else:
        date_in_list_format = date.split('-')

        if int(date_in_list_format[1]) not in range(1,13):
            return False
         
        else:
            print(int(date_in_list_format[1]) not in range(1,13))
            if date_in_list_format[1] in ('01','03','05','07','08','10','12'):
                if int(date_in_list_format[0]) not in range(1,32):
                    return False
                else:
                    return True
            elif date_in_list_format[1] in ('04','06','09','11'):
                if int(date_in_list_format[0]) not in range(1,31):
                    return False
                else:
                    return True
            elif date_in_list_format[1] == '02':
                if int(date_in_list_format[2])%4 == 0:
                    if int(date_in_list_format[0]) not in range(1,30):
                        return False
                    else:
                        return True
                else:
                    if int(date_in_list_format[0]) not in range(1,29):
                        return False
                    else:
                        return True

def main(times_executed):


    if times_executed == 0:
        print(f'{Style.BRIGHT}TIME MANAGEMENT SYSTEM')

    print('Type in the required operation')
    print(f'{Fore.GREEN}[1]  {Style.RESET_ALL}View tasks')    
    print(f'{Fore.GREEN}[2]  {Style.RESET_ALL}Add tasks')
    print(f'{Fore.GREEN}[3]  {Style.RESET_ALL}Update task status ') 
    print(f'{Fore.GREEN}[4]  {Style.RESET_ALL}Delete tasks' )
    print(f'{Fore.GREEN}[5]  {Style.RESET_ALL}Graphs ')  
    print(f'{Fore.GREEN}[0]  {Style.RESET_ALL}Quit ')
    
    
    csv_file = pd.read_csv(absolute_path_maker('tasks.csv'))

    choice = input('> ')

    if choice_validator(choice) == False:
        main(times_executed=1)

    if choice == '0':
        clear_screen()
        print('GoodBye!')
        exit(0)

    elif choice == '2':
        clear_screen()
        taskname = input('Taskname: \n> ')
        description = input('\nDescription (optional) \n>')
        status = 'pending'
        sr_no = int(np.array(csv_file.tail(1)['Sr. No'])[0]) + 1
        
        def date_input():
            date = input(f'\nScheduled Date \n  {Fore.CYAN}Format : DD-MM-YYYY {Style.RESET_ALL}  \n>')
            return date
        
        date = date_input()

        while not date_validator(date):
            print(f"{Fore.RED}Please enter a valid date in prescribed format")
            date = date_input()


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
        
        print('Entry saved !')
        print()
        print(csv_file.tail(1))
        print()
        input('Press ENTER to continue. ')
        main(times_executed=1)

    elif choice == '3':
        clear_screen()
        print(csv_file.tail())
        print()
        sr_no_input = int(input("Enter serial number of task whose status is to be updated: \n"))

        #Turning oof the SettingWithCopyWarning  (Below line)
        pd.set_option('mode.chained_assignment', None)

        csv_file['Status(pending/done)'][sr_no_input-1] = 'done'
        csv_file.to_csv(absolute_path_maker('tasks.csv'), index=False)
        print()
        print(csv_file.loc[[sr_no_input-1]])
        csv_file.to_csv(absolute_path_maker('tasks.csv'), index=False)
        
        print()
        print('Task Updated! ')
        input('Press ENTER to continue. ')
        main(times_executed=1)

    elif choice == '1':
        clear_screen()

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
        
        while choice_for3 not in ('a','b','c','d','e'):
            print(f'{Fore.RED}Invalid options !')
            print('Valid options: a, b, c, d and e')
            print('Want to continue ?  (Y/n) ')
            confirmation = input('>')
            if confirmation.lower() == 'y':
                print(f" {Fore.GREEN}(a) {Style.RESET_ALL}Show today's schedule")
                print(f" {Fore.GREEN}(b) {Style.RESET_ALL}Show from serial number ...:")
                print(f" {Fore.GREEN}(c) {Style.RESET_ALL}Show all pending tasks .")
                print(f" {Fore.GREEN}(d) {Style.RESET_ALL}Show all completed tasks ")
                print(f" {Fore.GREEN}(e) {Style.RESET_ALL}Show all tasks ")
                choice_for3_func()
            elif confirmation.lower() == 'n':
                main(times_executed=1)
        
        if choice_for3.lower() == 'a':
            clear_screen()
            today = ""
            date_in_list_format = str(datetime.date.today()).split('-')

            for i in date_in_list_format[::-1]:
                today = today + i + '-'

            today = today[:len(today)-1]
            
            condition = csv_file['Scheduled Date'] == today
            print(csv_file[condition])
            
            input('Press ENTER to continue.  ')
            main(times_executed=1)
            
        elif choice_for3.lower() == 'b':
            clear_screen()
            sr_no_input = int(input("Enter serial number: \n"))
            condition = csv_file['Sr. No'] >= sr_no_input
            print(csv_file[condition])

            input('Press ENTER to continue.  ')
            main(times_executed=1)
            
        elif choice_for3.lower() == 'c':
            clear_screen()
            condition = csv_file['Status(pending/done)'] == 'pending'
            print(csv_file[condition])
            
            input('Press ENTER to continue.  ')
            main(times_executed=1)

        elif choice_for3.lower() == 'd':
            clear_screen()
            condition = csv_file['Status(pending/done)'] == 'done'
            print(csv_file[condition])
            
            input('Press ENTER to continue.  ')
            main(times_executed=1)

        elif choice_for3.lower() == 'e':
            clear_screen()
            print(csv_file)

            input('Press ENTER to continue.  ')
            main(times_executed=1)

    elif choice == '4':
        clear_screen()
        print(csv_file.tail(5))
        print()
        sr_no_input = int(input("Enter serial number of task which is to be deleted \n"))
        csv_file = csv_file.drop(sr_no_input-1)
        csv_file.to_csv(absolute_path_maker('tasks.csv'), index=False)
        
        print("Entry Deleted!")
        input('Press ENTER to continue.  ')
        main(times_executed=1)

    elif choice == '5':
        clear_screen()
        print("Enter required option:- ")
        print(f" {Fore.GREEN}(a) {Style.RESET_ALL}Productivity Analysis for last 7 registered days (Bar Graph)")
        print(f" {Fore.GREEN}(b) {Style.RESET_ALL}Productivity Score Analysis for last 7 registered days (line graph)")

        def choice_for5_func():
            choice_for5 = input(">")
            return choice_for5
        
        choice_for5 = choice_for5_func()
        
        while choice_for5 not in ('a','b'):
            print(f'{Fore.RED}Invalid options !')
            print('Valid options: a, b')
            print('Want to continue ?  (Y/n) ')
            confirmation = input('>')
            if confirmation.lower() == 'y':
                print(f" {Fore.GREEN}(a) {Style.RESET_ALL}Productivity Analysis for last 7 registered days (Bar Graph)")
                print(f" {Fore.GREEN}(b) {Style.RESET_ALL}Productivity Score Analysis for last 7 registered days (line graph)")
                choice_for5_func()
            elif confirmation.lower() == 'n':
                main(times_executed=1)

        """FUNCTIONS"""

        def graphs(data_dataframe,graph): # num_of_unique_enteries_reqd):
            
            def filter_unique(data):
                filtered_list = []
                for x in data:
                    if x not in filtered_list:
                        filtered_list.append(x)
                return filtered_list

            def sorting_function(data_dataframe):
                """Sorting out future dates"""
                dates = list(data_dataframe['Scheduled Date'])
                
                for date in range(len(dates)):
                    dates[date] = datetime.datetime.strptime(dates[date], "%d-%m-%Y")
                        
                today = ""
                date_in_list_format = str(datetime.date.today()).split('-')

                for i in date_in_list_format[::-1]:
                    today = today + i + '-'
    
                today = today[:len(today)-1]
                condition_list = []

                for date in dates:
                    if date > datetime.datetime.strptime(str(today), "%d-%m-%Y"):
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
                    dates.remove(min(dates))
                    unique_dates = filter_unique(dates)
                
                for date in list(data_dataframe['Scheduled Date']):
                    if date in dates:
                        condition_list.append(True)
                    else:
                        condition_list.append(False)

                data_dataframe = data_dataframe[condition_list]
                
                return data_dataframe, unique_dates

            sorted_df, dates = sorting_function(data_dataframe)
            df = pd.DataFrame()
            df2 = pd.DataFrame()
            df3 = pd.DataFrame()
            pending_tasks_count = []
            completed_tasks_count = []
            productivity_score_list = []

            for date in dates:
                df = sorted_df[sorted_df['Scheduled Date'] == date]
                df2 = df[df['Status(pending/done)'] == 'pending']
                df3 =  df[df['Status(pending/done)'] == 'done']
                
                pending_tasks_count.append(len(df2.index))
                completed_tasks_count.append(len(df3.index))
                productivity_score = ((len(df3.index) - len(df2.index))/(len(df3.index) + len(df2.index)))*100  
                productivity_score_list.append(productivity_score)

            if graph  == 'bar':
                x = np.arange(len(dates))
                plt.bar(x, completed_tasks_count, label="Completed", width=0.25, color="green")
                plt.bar(x+0.25, pending_tasks_count, label="Pending",width=0.25, color="red")
                plt.xticks(x, dates)
                plt.xlabel('Date')
                plt.ylabel('Number Of Tasks')
                plt.title('Productivity Analysis for last 7 registered days')
                plt.legend()
                plt.show()

            if graph == 'line':
                x = np.array(dates)
                y = np.array(productivity_score_list)
                plt.plot(x,y, marker='o')
                plt.xlabel('Dates')
                plt.ylabel('Productivity Score')
                plt.title('Productivity Score Analysis for last 7 registered days.')
                plt.show()
            
        if choice_for5.lower() == 'a':
            graphs(csv_file,'bar')
            input('Press ENTER to continue. ')
            main(times_executed=1)

        elif choice_for5 == 'b':
            graphs(csv_file,'line')
            input('Press ENTER to continue. ')
            main(times_executed=1)

if __name__ == '__main__': 
    main(times_executed=0)

