from math import e
import time
import os
import sys
import random
from getpass import getpass
from itertools import chain, product
from typing import Counter
from random import randint, sample

# Python 2 and 3 have different string constants, so this makes the library
# Python 3 compatible.
try:
    from string import (
        digits as _numbers,
        letters as _letters,
        punctuation as _symbols,
        whitespace as _spaces,
    )
except ImportError:
    from string import (
        digits as _numbers,
        ascii_letters as _letters,
        punctuation as _symbols,
        whitespace as _spaces,
    )


__version__ = '0.0.3'


def brute(start_length=1, length=3, ramp=True, letters=True, numbers=True, symbols=True, spaces=False):
    """
    Iterate through a sequence of possible strings, efficiently.

    :param int start_length: The length of the string to begin ramping through.
        This number must be less than length and greater than 0. Default: 1.
    :param int length: The length of the string to iterate through.  We'll
        iterate through all permutations of strings up to this length. Default:
        3.
    :param bool ramp: Should we ramp up in length from 1 until length?  Or
        should we only iterate over values of the current length?  Default:
        True.
    :param bool letters: Include letters (upper and lower case)? Default: True.
    :param bool numbers: Include numbers? Default: True.
    :param bool symbols: Include symbols? Default: True.
    :param bool spaces: Include space characters? Default: False.

    :rtype: generator
    :returns: A generator which iterates through all permutations of the
        specified values.
    """
    choices = ''
    choices += _letters if letters else ''
    choices += _numbers if numbers else ''
    choices += _symbols if symbols else ''
    choices += _spaces if spaces else ''
    choices = ''.join(sample(choices, len(choices)))

    if ramp:
        if start_length < 1 or start_length > length:
            start_length = 1

    return (
        ''.join(candidate) for candidate in
        chain.from_iterable(
            product(
                choices,
                repeat=i,
            ) for i in range(start_length if ramp else length, length + 1)
        )
    )


mode = ''
second = 0
minute = 0
hours = 0


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return ("{0}:{1}:{2}".format(int(hours), int(mins), round(sec, 1)))


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer[3:], end="\r")
        time.sleep(1)
        t -= 1
    print("\n:)")


time.sleep(0.5)
human_rage = 0
robot_trust = 0
rage = 0
none_validate = ''
passwd = str(getpass('Enter your password : '))
while passwd == '':
    time.sleep(1)
    print("'-'")
    time.sleep(1)
    print('-_-')
    time.sleep(1)
    none_validate = input('\nReally you want Enter Nothing ._. ?(y or n)')
    if none_validate == 'n':
        time.sleep(0.2)
        print('\n0k Enter Again')
        time.sleep(0.4)
        passwd = str(getpass('Enter your password : '))
        rage += 1
        time.sleep(0.6)
        while passwd == '':
            if rage == 1:
                time.sleep(1)
                print('IDK why you enter nothing ,')
                rage += 1
                time.sleep(1)
                passwd = str(getpass('Enter your password : '))
            elif rage == 2:
                time.sleep(0.6)
                print('\nAgain ?\nare you ok ?\n')
                rage += 1
                time.sleep(0.5)
                passwd = str(getpass('Enter your password : '))
            elif rage == 3:
                time.sleep(0.5)
                rage += 1
                time.sleep(0.5)
                passwd = str(getpass('\njust enter the f***ing password : '))
            elif rage == 4:
                time.sleep(1)
                print('\n...')
                time.sleep(3)
                print('Mother B*&%#ch /:')
                time.sleep(1)
                rage += 1
                passwd = str(getpass('ENTER ITTTTT : '))
            elif rage == 5:
                if human_rage == 0:
                    time.sleep(0.5)
                    human = input('Are You A human ? :| ').lower()
                    human_rage += 1
                elif human_rage == 1:
                    time.sleep(0.5)
                    human = input('Are You A human ? :| ').lower()
                    human_rage += 1
                elif human_rage == 2:
                    time.sleep(0.5)
                    human = input('I ASK AGAIN , \n r u ANIMAL ? ').lower()
                    human_rage += 1
                elif human_rage == 3:
                    time.sleep(0.5)
                    human = input('pls answer bro, are you human or not ?').lower()
                    human_rage += 1
                elif human_rage == 4:
                    time.sleep(0.5)
                    print('pls')
                    time.sleep(2)
                    print('dont bother me,')
                    time.sleep(1)
                    human = input('This is not hard , answer me :( ').lower()

                if human == 'no' or human == 'n':
                    print('But\n')
                    time.sleep(2.5)
                    print('How you know to answare my questions ? ;-;')
                    time.sleep(2.5)
                    rage += 1
                elif human == 'yeah' or human == 'yes' or human == 'ye' or human =='y':
                    num_0 = random.randint(1,30)
                    num_1 = random.randint(1,30)
                    num_3 = num_0 + num_1
                    time.sleep(0.8)
                    numsGet = int(input(f'0K :/ Confirm you are not Robot :D \n{num_0} + {num_1} ?? '))
                    time.sleep(1.6)
                    print('\nWait sec to i calculate .. ')
                    if numsGet != num_3:
                        time.sleep(1.2)
                        print('._.')
                        time.sleep(2)
                        print('I want to say something...\nyour math is so FUCKING.')
                        rage += 1
                    elif numsGet == num_3:
                        time.sleep(0.5)
                        print('Clever,')
                        time.sleep(0.2)
                        break
                else:
                    robot_trust += 1
                    if robot_trust == 1:
                        time.sleep(0.4)
                        print('WTF are you saying ._.\nANSWER ME')
                    elif robot_trust == 2:
                        time.sleep(1)
                        print('JUST')
                        time.sleep(1)
                        print('ANSER')
                        time.sleep(1)
                        print('ME\n')
                        time.sleep(1)
                        print('WITH')
                        time.sleep(1)
                        print('THIS')
                        time.sleep(1)
                        print('FUCKING CHARACTERS -->\n')
                        time.sleep(1)
                        print('     -----> yeah,yes,ye,y OR no,n <----BITCH\n')
                        time.sleep(1)
                    elif robot_trust == 3:
                        time.sleep(1)
                        time.sleep(1)
                        print('ok..')
                        time.sleep(1)
                        print('i think i NEVER FORGIVE YOU.\n')
                        time.sleep(2)
                    elif robot_trust == 4:
                        time.sleep(6)
                        print(':)')
                        time.sleep(2)
                        print('\n.')
                        time.sleep(3.5)
                        num_4 = random.randint(1,10)
                        num_5 = random.randint(500,1000)
                        num_6 = random.randint(50,200)
                        num_7 = random.randint(100,250)
                        num_8 = random.randint(300,330)
                        num_9 = random.randint(200,250)
                        num_10 = random.randint(100,150)
                        print(f'\n{"F"*num_4}{"U"*num_5}{"C"*num_6}{"K"*num_7}  {"Y"*num_8}{"O"*num_9}{"U"*num_10}\n\n')
                        time.sleep(1)
                    elif robot_trust == 5:
                        print('Bro')
                        time.sleep(3)
                        print('Dont forget something..')
                        time.sleep(2)
                        print('I Just do my job')
                        time.sleep(2)
                        print('i mean ..')
                        time.sleep(1)
                        print('Help to people is my job .. SomeOne like You :)')
                        time.sleep(3)
                        print('my Friend')
                        time.sleep(1.5)
                        print('Forgive me if i upset you\n')
                        time.sleep(1.2)
                        print('Anyway.')
                        time.sleep(1.8)
                        print('I have best wishes for you :)')
                        time.sleep(3)
                        print('\nand one more thing')
                        time.sleep(4.5)
                        print('...')
                        time.sleep(0.4)
                        countdown(t=5)
                        os.system('cls')
                        time.sleep(0.7)
                        print('\n\nGoodBye')
                        time.sleep(2)
                        print('Myfriend')
                        time.sleep(1)
                        print(':)')
                        time.sleep(2.5)
                        sys.exit()    
            elif rage == 6:
                passwd = str(getpass('Please enter it, Its Good For you :) '))
    elif none_validate == 'y':
        time.sleep(1)
        print('\n0K adiot ._. \n')
        break


time.sleep(0.5)

if __name__ == '__main__':
    start_length = int(input('\nMin length of your password [1,2, ...] : '))
    length = int(input('Max length of your password[1,2, ...] : '))
    letters = input('Include letters[y or n] : ').lower() != 'n'
    numbers = input('Include numbers[y or n] : ').lower() != 'n'
    symbols = input('Include symbols[y or n] : ').lower() != 'n'
    spaces = input('Include space[y or n] :') == 'y'

time.sleep(0.5)

print('\nAttention \nmaybe FuckUp your CPU ...')
time.sleep(2)
print('\n3 Second to start\n')
time.sleep(1)


countdown(t=3)

passGen = brute(start_length=start_length, length=length, letters=letters, numbers=numbers, symbols=symbols, spaces=spaces)

index = 0
type_index = 1
type_index_req = 1

start_time = time.time()
for guess in passGen:
    end_time = time.time()
    time_lapsed = end_time - start_time
    expt = time_convert(time_lapsed)
    out_time = expt[:-2]
    if out_time[-1] == '5':
        while type_index > 0:
            type_index -= 1
            print(f'{index} password checked : {guess}  time spend : {out_time}')
    if out_time[-1] != '5':
        type_index = type_index_req
    index += 1
    if guess == passwd:
        os.system('cls')
        print(
            f'\n\nYour password is : {guess}\n\nSpended Time {out_time}\n{index} password checked !\n')
        break
