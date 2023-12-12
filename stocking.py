''' This module contains function to CRUD;
Create
Retrieve
Update
Delete
'''

from datetime import datetime as dt
import sqlite3
import user # import our general action function for creating, deleting, logging out

# print('Welcome to your favourite Stock taking app.\nCreate,Delete or Retrieve')


# using multpile constructor (class method)
class CreateProduct:
    """
    This class contain differenent function for the purpose of populatin our DB.

    """

    def __init__(self, product):  # using positional arguments
        self.product = product
        self.item = product[0]  # for items
        self.category = product[1]  # for catergory
        self.unit = product[2]  # for unit
        self.price = product[3]  # for price
        self.status = product[4]  # for status
        self.date_added = product[5]  # to add a

    @classmethod
    def create_product_input(cls):
        '''
        A class method that takes input from user, this input is then used by the constructor.
        we must instantiate this method together with the class as it the method that take input needed by the constructor
        '''
        
        print('-----------------------------------------------------\nYou are about to start creating proudct watch out for error😁.\n-----------------------------------------------------\n')
        item = input('required \nWhat the product name: ').strip()
        while len(item) == 0:
            print('Enter a valid item:')
            item = input('required \nWhat the product name: ').strip()
        category = input(
            'What the category?: \n if you do want to add you can do it later.')
        unit = int(input('required  \nHow many unit is avalaible: '))
        price = float(input('required \nHow much per unit(15): '))

        # add date which product was created to DB
        date_added = dt.now().strftime("%Y-%m-%d %H:%M:%S")

        # controlling the input to 1 or zero alone with ternary operation
        status = int(input(
            'required \nIs the product available yet, Available/Out of stock : pick(1/0) '))  # available/out of stock

        while status not in [0,1]:
            print('Enter either 1(Available) or 0(Out of stock)')
            status = int(input(
            'required \nIs the product available yet, Available/Out of stock : pick(1/0) '))  # available/out of stock
        real_status = "Available" if status == 1 else "Out of stock" 
        
        product = item.capitalize(), category.capitalize(
        ), unit, price, real_status, date_added # tuple packing

        return cls(product)

    def product_to_db(self):
        """
        This function insert our list of product into the Db

        """
        
        with sqlite3.connect('stocker_db.sqlite3') as inserted:
            cursor = inserted.cursor()

            # insertion into atable we manually created name Product
            COMMAND = 'INSERT INTO Product(Item,Category,Unit,Price,Status,Created) VALUES (?,?,?,?,?,?)'
            cursor.execute(COMMAND, (self.item, self.category,
                           self.unit, self.price, self.status, self.date_added))

            inserted.commit()
            
            print('-----------------------------------------------------\nInserted into DB.\n-----------------------------------------------------\n')

    def product_to_console(self):
        ''' 
        A function making sure details inputted to DB is printed on terminal
        '''
        print('calling product to db function')
        self.product_to_db()
        print('success calling made to db function')
        # the end if all process is succceful
        # user.action() # after each creation make a new decision.
        print(f'-----------------------------------------------------\nEverything woring fine . \nThe input here = {self.product}\n-----------------------------------------------------\n')
        user.action() # after each creation make a new decision.

# console_and_DB = CreateProduct.create_product_input()
# console_and_DB.product_to_console()


def retrieve_record(table_name, column, record):
    """ Retrieving record from Database it can be any table
    The search is case-sensitive.
    param: table name = name of a table in our DB
            column = A column in our table
            record = A record will be returned if this matchs one of the stored data in any of the column in the table.
    """
    try:
        with sqlite3.connect("stocker_db.sqlite3") as retrieving:
            cursor = retrieving.cursor()

            COMMAND = f'SELECT * FROM {table_name} WHERE {column} =?'

            cursor.execute(COMMAND, (record,))
            found = cursor.fetchall()

            if len(found) >= 1:
                print(f'-----------------------------------------------------\n{found}\n-----------------------------------------------------\n')
                print(found)
            else:
                print(f'-----------------------------------------------------\nTable {table_name} doesn\'t have either a column named {column} or a record for {record}\n-----------------------------------------------------\n')

    except sqlite3.Error as e:
        print(e)

# retrieve_record('Product', 'Category', 'Drinks')


class DeleteDataFromDb:
    """
    This class contain the function for deleting data from either the whole tables in the DB or a specified table,
    """

    # def __init__(self, table_name):
    #     self.table = table_name
       

    def __delete_action(self):
        ''' 
        Implementation to know you really want to delete all files in the DB table. 
        if any inconsistency found in your input you will be logged out.
        The double underscore(__) is to make sure this class isn't accesible from the outside 
        '''
        # making sure you realy wants to delete all data
        print('\n-----------------------------------------------------\nif any inconsistency found in your input you will be logged out.\n-----------------------------------------------------\n')
        assurance = input('You are trying to delete the whole data🙄. Enter Yes or No: ').capitalize()
        # assured = 0

        if assurance == "Yes":
            assured = 0
            while assured < 3 and assurance =='Yes': # only No and assured gt 3 keeps end this loop
                print(f'\nAre you sure you really wants to delete all table.I am asking {assured+1} out of 3.\n', )
                assurance = input('You are trying to delete the whole data🙄. Enter Yes or No: ').capitalize()
                # iterator it increase assured value
                if assurance == 'Yes':
                    assured += 1
                else:
                    print('\nYou are guilty of indecision.You have been logged out.☹\n')
            return("Valid")
        else:
            print('\nYou are guilty of indecision.You are going to be logged out.🤐\n')
            return('Invalid')

    def delete_all_tables(self):
        ''' cAVEATS: All data from our Db can be deleted calling this function alone. 
        '''

        print('-----------------------------------------------------\nDELETEING ALL DATA FROM DB TABLES.\n-----------------------------------------------------\n')
        try:
            if self.__delete_action() == 'Valid':
                with sqlite3.Connection('stocker_db.sqlite3') as to_del:
                    cursor = to_del.cursor()

                    # to disable foreign key relationship between db table
                    COMMAND = 'PRAGMA foreign_key=OFF'
                    cursor.execute(COMMAND)

                    # to get list of all tables in our DB
                    COMMAND = "SELECT name FROM sqlite_master WHERE type='table';"
                    cursor.execute(COMMAND)
                    tables = cursor.fetchall()

                    for table in tables:
                        table_name = table[0]
                        print(table_name)
                        cursor.execute(f"DELETE FROM {table_name};")

                    # Enable foreign key constraints again
                    cursor.execute('PRAGMA foreign_keys=ON')

                    # Now deleting
                    to_del.commit()
                    print('Deleted succesfull.\n Database table data Empty')
            else:
                print('You have been logged out')

        except sqlite3.Error as e:
            print(f'There is an error {e}')

    def delete_specific_table(self,table_name):
        ''' Warning: A particular table will be deleted calling this function.
        The table to be deleted will be passed into the class object 
        '''
        print(f'-----------------------------------------------------\nDELETEING ALL DATA FROM {table_name}DB TABLES.\n-----------------------------------------------------\n')

        try:
            with sqlite3.Connection('stocker_db.sqlite3') as to_del:
                cursor = to_del.cursor()

                # to disable foreign key relationship between db table
                COMMAND = 'PRAGMA foreign_key=OFF'
                cursor.execute(COMMAND)

                # to get list of all tables in our DB

                COMMAND = "SELECT name FROM sqlite_master WHERE type='table';"
                cursor.execute(COMMAND)
                tables = cursor.fetchall()
                # print(list(tables)) # return name of all table in the Db

                for table in tables:
                    if table_name in table:
                        print(table_name)
                        cursor.execute(f"DELETE FROM {table_name};")
                        print(f"The table {table_name} is deleted")
                        break
                else:
                    print(f'Table {table_name} not found')

                # Enable foreign key constraints again
                cursor.execute('PRAGMA foreign_keys=ON')
                to_del.commit()

        except sqlite3.Error as e:
            print(f'There was an error {e}')

# delete = DeleteDataFromDb()
# delete.delete_specific_table()

# delete._DeleteDataFromDb__delete_action()  # through name mangling it can be accessed 
