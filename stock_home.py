# from stocking import *
from user import user_auth, createuser


# Good morning Task to handle today, make sure that when input is empty string it keeps on bringing the input button

print('-----------------------------------------------------\nWelcome to your favourite Stock taking app.\nCreate user or log in or delete .\n-----------------------------------------------------\n')

action = int(input('Enter 0 to Login or 1 to create account : '))
# assert action in [0, 1], 'Input can only be 1 or 0'
# command = createuser() if action == 1 else user_auth()
# print(command)

# Depending on the type of format used to call our function if we don't use
# print the last statement won.t be printed cause we are usinng the return statement.

while action in [0, 1]:
    if action == 1:
        createuser()

    else:
        user_auth()
