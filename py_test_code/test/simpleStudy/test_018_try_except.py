'''
Created on 2016年8月19日

@author: shengxiz
'''
import sys
try:
    s = input('Enter something --> ')
except EOFError:
    print ('\nWhy did you do an EOF on me?')
    sys.exit() # exit the program
except:
    print ('\nSome error/exception occurred.')
# here, we are not exiting the program
print ('Done')