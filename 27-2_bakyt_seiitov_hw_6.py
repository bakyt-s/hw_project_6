import re


def program():
    while True:
        print(f'Program menu')
        program_options = ['1 - Read names and last names',
                           '2 - Read emails',
                           '3 - Read files',
                           '4 - Read colors',
                           '5 - Exit']
        for option in program_options:
            print(option)
        try:
            with open('MOCK_DATA.txt', 'r') as data:
                content = data.read()
            select_option = int(input('\nEnter a number from the list: '))

            if select_option == 1:
                with open('colors.txt', 'w') as colors:
                    colors_lst = re.findall(r'\b[A-Z][a-zA-Z\'\- ]+[\s]+[a-zA-Z\'\- ]+\b', content)
                    for color in colors_lst:
                        colors.write(color)
                print('List of Names and Last Names has been created in names.txt\n')
            if select_option == 2:
                with open('colors.txt', 'w') as colors:
                    colors_lst = re.findall(r'[\w\.-]+@[\w\.-]+', content)
                    for color in colors_lst:
                        colors.write(color)
                print('List of Emails has been created in emails.txt\n')
            if select_option == 3:
                with open('files.txt', 'w') as files:
                    files_lst = re.findall(r'\t\w+\.[a-z]{1,}', content)
                    files_lst = [i.rstrip() for i in files_lst]
                    for file in files_lst:
                        files.write(file)
                print('List of Files has been created in files.txt\n')
            if select_option == 4:
                with open('colors.txt', 'w') as colors:
                    colors_lst = re.findall(r'#[\da-f]{6}', content)
                    for color in colors_lst:
                        colors.write(color + '\n')
                print('List of RGB Color Code has been created in colors.txt\n')
            if select_option == 5:
                print('The program has ended')
                break
        except ValueError:
            print('Enter only numbers from 1 to 5\n'.upper())


program()
