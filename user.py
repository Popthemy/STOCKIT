'''
This module contain function to;
createuser = createuser()
Authenticate user = userauth()
'''

import sqlite3
from datetime import datetime as dt
import hashlib  # hasing password
from stocking import CreateProduct, DeleteDataFromDb


def createuser():
    '''
    Create new user. Users are been prompted to input username and
    if the username exist in the DB it has to be changed.
    The password is also hashed for security purpose.
    '''

    print('-----------------------------------------------------\nWelcome 😎 Enter your valid details and sign in\n-----------------------------------------------------\n')

    username = input('Enter username (length between 6 - 50): ')
    while not 6 <= len(username.strip()) <= 50:
        print('Enter a valid Username (length between 6 - 50)')
        username = input('Enter username of length between 6 - 50 : ')

    password = input('Enter password (length between 6 - 50): ')
    while not 6 <= len(password.strip()) <= 50:
        print('Enter a valid Password (length between 6 - 50)')
        password = input('Enter password of length between 6 - 50 : ')

    # creating date of creation
    time_obj = dt.now()
    created = time_obj.strftime('%Y-%m-%d %H:%M:%S')

    # connecting to stocker_db.sqlite3
    with sqlite3.connect('stocker_db.sqlite3') as user:
        cursor = user.cursor()

        # checking if user exists before storing into db
        COMMAND = 'SELECT * FROM Users WHERE Username=?'
        cursor.execute(COMMAND, (username,))
        existing = cursor.fetchone()

        if existing:
            print(
                '-----------------------------------------------------\nUser with the username: %s already existing.\nChange your username.\n-----------------------------------------------------\n' % username)
            return createuser()

        else:
            # hashing our password for security reason
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # storing details in our DB
            COMMAND = 'INSERT INTO Users(Username, Password, Created) VALUES (?,?,?)'
            cursor.execute(COMMAND, (username, hashed_password, created))
            user.commit()
            print('-----------------------------------------------------\nAccount Successfully\n-----------------------------------------------------\n')
            action()  # for decision making to log out or create product


# print(createuser())


def user_auth():
    '''
    Here user get authenticated, user input their details and it get checked with the details in the DB.
    '''

    print('-----------------------------------------------------\nWelcome back 😋 Enter your details and login.\n-----------------------------------------------------\n')

    username = input('Enter your username : ')
    while not (6 <= len(username.strip()) <= 50):
        print('Enter your valid Username (length between 6 - 50)')
        username = input('Enter your username of length between 6 - 50 : ')

    password = input('Enter your password : ')
    while not (6 <= len(password.strip()) <= 50):
        print('Enter your valid Password (length between 6 - 50)')
        password = input('Enter your password of length between 6 - 50 : ')

    # connecting to db
    with sqlite3.connect('stocker_db.sqlite3') as auth:
        cursor = auth.cursor()

        # checking if user exists before storing into db
        COMMAND = 'SELECT * FROM Users WHERE Username=? AND  Password=?'
        cursor.execute(COMMAND, (username, hashlib.sha256(
            password.encode()).hexdigest()))
        verified = cursor.fetchone()

        if verified:
            # calling a function that to specify if you log out or add product
            print('Checked✔✔✔ \nLogin Successful.')
            print('-----------------------------------------------------\nDo you want to perform an action (Create, Delete or Log out).\n-----------------------------------------------------\n')
            action()

        else:
            print("incorrect details.")
            login = input('Do you have an account? Yes/No: ')
            login_cap = login.capitalize()

            assert login_cap in ['Yes', 'No']  # catching error
            if login_cap == 'Yes':
                return user_auth()
            else:
                print('Create new account')
                return createuser()


# user_auth()


ACTIONS = ['Create', 'Log out', 'Delete']


def action():
    ''' This function allows us to decide either to create a product or delete data from a table or log out performing no action
    '''
    main_action = input(
        'Press either create , delete  or Log out to perform the function. required*: ').capitalize()
    print(main_action)

    while main_action not in ACTIONS:
        main_action = input(
            'Press either Create, Delete or Log out. required* : ').capitalize()

    if main_action == 'Create':
        # if add then we call the create product class that allows us to input the data for the product,
        # take the data updates it to Db and then print the input data to us.

        console_and_db = CreateProduct.create_product_input()
        console_and_db.product_to_console()

    elif main_action == 'Delete':
        print('-----------------------------------------------------\nChoose delete options.\n-----------------------------------------------------\n')
        del_input = int(
            input('Pick 1 to delete data from all DB or 2 to delete a particular table.'))
        if del_input == 1:

            DeleteDataFromDb().delete_all_tables()

        else:
            table_name = input('Enter the name of the table to be deleted: ')
            DeleteDataFromDb().delete_specific_table(table_name)

    elif main_action == 'Log out':
        print('-----------------------------------------------------\nLog out Successful. Bye for now👋.\n-----------------------------------------------------\n')
