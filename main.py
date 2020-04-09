import random
import re
from random import randint

# probl4// A password is considered strong if below conditions are all met: 1.  It has at least 6 characters and at
# most 20 characters. 2.  It must contain at least one lowercase letter, at least one uppercase letter, and at least
# one digit. 3.  It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is
# strong, assuming other conditions are met).  Write an algorithm that takes a string s as input, and return the
# MINIMUM change required to make s a strong password. If s is already strong, return 0.  Insertion, deletion or
# replace of any one character are all considered as one change.


# project by Nadia Gherman

def randchar(label):
    # get a random letter
    # if label == 'a', return a random lower case letter
    # if label == 'A', return a random upper case letter

    if label == 'a':
        return chr(random.randrange(97, 97 + 26))
    if label == 'A':
        return chr(random.randrange(65, 65 + 26))


def make_changes(conditions, password, start, changes):
    # conditions : Dict[key: string, value: int]
    # dictionary of the conditions for password strength

    # password : String
    # a password string we need to make changes to

    # start : int
    # if password contains 3 ore more repeating characters in a row: start = 0
    # else: start = index where the sequence starts

    # changes : int
    # number of changes made to password

    # make an array out of password string to perform operations like insert, append etc
    password_array = [x for x in password]

    # check the strongest conditions, where number of changes can be minimised
    # if (password length is < 6) and (password contains 3 repeating characters in a row)
    # and (password does not contain at least one lower case letter/upper case letter/digit) then
    # add the missing type of character somewhere in the sequence of repeating characters

    if conditions['length is >=6 letters'] == 0 \
            and conditions['does not contain 3 repeating characters in a row'] == 0:
        if conditions['it contains at least one digit'] == 0:
            password_array.insert(start + 2, randint(0, 9))
            changes += 1
            conditions['it contains at least one digit'] = 1

        if conditions['it contains at least one lower case letter'] == 0:
            password_array.insert(start + 2, randchar('a'))
            changes += 1
            conditions['it contains at least one lower case letter'] = 1

        if conditions['it contains at least one upper case letter'] == 0:
            password_array.insert(start + 2, randchar('A'))
            changes += 1
            conditions['it contains at least one upper case letter'] = 1

    # check if length and sequence conditions were fixed
    # update conditions dictionary accordingly

    password = ""
    for let in password_array:
        password += str(let)

    if len(password_array) == 6:
        conditions['length is >=6 letters'] = 1

    if re.search('([a-zA-Z0-9])\\1{2,}', password) is None:
        conditions['does not contain 3 repeating characters in a row'] = 1

    # check next strong conditions and minimise the number of changes
    # if (password contains 3 repeating characters in a row) and (password does not contain at least one
    # lower case letter/upper case letter/digit) then replace one/more of the characters in the sequence
    # with the missing type of character (random generated)

    if conditions['does not contain 3 repeating characters in a row'] == 0:
        if conditions['it contains at least one lower case letter'] == 0:
            changes += 1
            password_array[start + 2] = randchar('a')
            conditions['it contains at least one lower case letter'] = 1
        else:
            if conditions['it contains at least one upper case letter'] == 0:
                changes += 1
                password_array[start + 2] = randchar('A')
                conditions['it contains at least one upper case letter'] = 1
            else:
                if conditions['it contains at least one digit'] == 0:
                    changes += 1
                    password_array[start + 2] = randint(0, 9)
                    conditions['it contains at least one digit'] = 1
                else:
                    del password_array[start + 2]
                    changes += 1

    # if (password length < 6) and (password does not contain at least one lower case letter/upper case letter/
    # digit) then append the missing type of character
    # if (password length < 6) append random character
    if conditions['length is >=6 letters'] == 0:
        if conditions['it contains at least one upper case letter'] == 0:
            changes += 1
            password_array.append(randchar("A"))
            conditions['it contains at least one upper case letter'] = 1

        else:
            if conditions['it contains at least one digit'] == 0:
                changes += 1
                password_array.append(randint(0, 9))
                conditions['it contains at least one digit'] = 1
            else:
                if conditions['it contains at least one lower case letter'] == 0:
                    changes += 1
                    password_array.append(randchar('a'))
                    conditions['it contains at least one lower case letter'] = 1
                else:
                    password_array.append(randchar('a'))
                    changes += 1

    # check remaining conditions and make changes

    # if (password length >20 letters) delete random character
    if conditions['length is <=20 letters'] == 0:
        del password_array[randint(0, len(password_array) - 1)]
        changes += 1

    # if (password does not contain at least one lower case letter/upper case letter/digit) then
    # append the missing type of character
    if conditions['it contains at least one digit'] == 0:
        password_array.append(randint(0, 9))
        changes += 1

    if conditions['it contains at least one lower case letter'] == 0:
        password_array.append(randchar('a'))
        changes += 1

    if conditions['it contains at least one upper case letter'] == 0:
        password_array.append(randchar('A'))
        changes += 1

    # return the password as a string and the number of changes made to the main method
    password = ""
    for let in password_array:
        password += str(let)

    return password, changes


def check_password(password):
    # dictionary for the conditions of a strong password, values = {0,1}
    # conditions[key] == 0 -> password does not meet condition
    # conditions[key] == 1 -> password meets condition
    # initialize all conditions to 0

    conditions = {'length is >=6 letters': 0,
                  'length is <=20 letters': 0,
                  'it contains at least one digit': 0,
                  'it contains at least one lower case letter': 0,
                  'it contains at least one upper case letter': 0,
                  'does not contain 3 repeating characters in a row': 0}

    # number of changes made to the password string,
    # initially 0
    changes = 0
    # remember a copy of our initial password
    password_copy = password

    # a while loop to keep re-evaluating and changing the password until it becomes a strong password

    while [v for v in conditions.values()] != [1, 1, 1, 1, 1, 1]:
        # evaluate if password string respects all constraints

        # checks if length is between 6-20 characters
        if len(password) in range(6, 21):
            conditions['length is >=6 letters'] = 1
            conditions['length is <=20 letters'] = 1
        if len(password) < 6:
            conditions['length is <=20 letters'] = 1
        if len(password) > 20:
            conditions['length is >=6 letters'] = 1
        # checks if it contains at least one lower case letter
        if re.search('[a-z]', password):
            conditions['it contains at least one lower case letter'] = 1
        # checks if it contains at least one upper case letter
        if re.search('[A-Z]', password):
            conditions['it contains at least one upper case letter'] = 1
        # checks if it contains at least one digit
        if re.search('[0-9]', password):
            conditions['it contains at least one digit'] = 1

        # checks if it contains a sequence of 3 ore more repeating characters
        s = re.search('([a-zA-Z0-9])\\1{2,}', password)
        if s is not None:
            # if password string contains a sequence of 3 or more repeating characters, start <- the index where the
            # sequence starts
            start = s.span()[0]
        if s is None:
            conditions['does not contain 3 repeating characters in a row'] = 1

        # call make_changes() method
        if conditions['does not contain 3 repeating characters in a row'] == 0:
            password, changes = make_changes(conditions, password, start, changes)
        else:
            password, changes = make_changes(conditions, password, 0, changes)

    # after while loop
    if changes == 0:
        # no changes were made, so password is strong already
        return 0
    else:
        # we return the old password string, new password string and number of changes that were made
        return str(password_copy) + " into " + str(password) + " with number of changes made: " + str(changes)


# some tests
print(check_password("aBBBBBCDEF5678"))
print(check_password("abcdefij1"))
print(check_password("123abcDEFaaa"))
print(check_password("555AbcDef"))
print(check_password("!#$"))
print(check_password("abcdef4123456789bdefhjdj"))
print(check_password("ABCDEF4567890123456123456"))
print(check_password("parolaMea123"))
print(check_password("1"))
print(check_password("ABCDE12345ABCDE12345a"))
