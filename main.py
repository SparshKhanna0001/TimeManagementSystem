import os 
import pandas as pd
#import mathplotlib as pyplt
import datetime 


""" Functions """

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

#incomplete ↑
def choice_validator(input):

    if input not in ('0','1','2','3','4','5','6','7','8','9'):
        clear_screen()
        print('Invalid input provided !')
        print('\n')
        return False


def main(times_executed):


    if times_executed == 0:
        print('\033[1m TIME MANAGEMENT SYSTEM \033[0m')

    print('Type in the required operation')

    print('\033[92m [1] \033[0m Add tasks')
    print('\033[92m [2] \033[0m Edit task status ')
    print('\033[92m [3] \033[0m View tasks') 
    print('\033[92m [].\033[0m Delete tasks' )
    print('\033[92m [] \033[0m Graphs ')
    print('\033[92m [] \033[0m Help ')
    print('\033[92m [] \033[0m Quit ')
    
    #csv_file = pd.read_csv('tasks.csv')

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
        description = input('Description \033[1m (optional) \033[0m \n>')
        print()
        date = input('Scheduled Date \n  \033[1m Format : DDMMYYY \033[0m \n>')
        print()
        estimated_time= input('Enter estimated time required to do the task: \n>')
        
        status = True
        #sr_no = csv_file.tail(1)
        #csv_file.append[{'Sr. No':sr_no,'Tasks':taskname,'Description':description,'Scheduled Date':date,'Estimated Time':estimated_time,'Status(pending/done)':status}]
        #csv_file.to_csv('tasks.csv', index=False)

    elif choice == '2':
        sr_no_input = int(input("Enter serial number of task whose status is to be updated: \n"))
        print(
    elif choice == '3':
        print("\033[1mEnter required option:-\033[0m")
        print(" (a) Show today's schedule")
        print(" (b) Show from serial number ...:")
        print(" (c) Show all pending tasks .")
        print(" (d) Show all completed tasks ")
        print(" (e) Show all tasks ")

        def choice_for3():
            choice_for3 = input(">")

        if choice_for3 not in ('a','b','c','d','e'):
            print('Invalid options !')
            print('\033[1mValid options:\033[1m  a, b, c and d')
            print('Want to continue ?  (Y/n) ')
            confirmation = input('>')
            if confirmation.lower() == 'Y'
                choice_for3()
            else:
                main(times_executed=1)

        if choice_for3 == 'b':
            sr_no_input = int(input("Enter serial number: \n"))
            #print(csv_file('Sr. No') >= sr_no_input)

        elif choice_for3 == 'c':
            #print(csv_file('Status(pending/done)' == 'pending')

        elif choice_for3 == 'd':
            #print(csv_file('Status(pending/done)' == 'done')
        
        elif choice_for3 == 'e':                              #print(csv_file)
        




if __name__ == '__main__': 
    main(times_executed=0)
