# from stocking import *
from user import user_auth, createuser

print('-----------------------------------------------------\nWelcome to your favourite Stock taking app.\nCreate user or log in or delete .\n-----------------------------------------------------\n')

action = int(input('Enter 0 to Login or 1 to create account : '))

i = 0
while i < 1:
    if action in [0, 1]:
        if action == 1:
            createuser()
        else:
            user_auth()
    else:
        print(f'{action} not a valid input : ERROR 404')
    i +=1 # after a successful action user can now log out.