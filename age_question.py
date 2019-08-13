# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:22:58 2019

@author: jim
ask the user name :
 Ask the user’s age+input the name of user in the box of asking there age
. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trickor-Treating”
"""
name=input('what your name : ')
age=int(input('what your age {} : '.format(name)))
if age>=18:
    print('You can vote')
elif age==17:
    print('You can learn to drive')
elif age==16:
    print('you can buy a lottery ticket')
else:
    print('you can go Trickor-Treating')

