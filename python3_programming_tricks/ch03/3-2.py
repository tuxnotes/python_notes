fn = 'aaa.py'

fn.endswith('.py') # return True or False

fn.endswith(('.py', '.sh')) # end with .py or .sh

import os

d = os.listdir('.') # return a list

s = os.stat('b.py')
s.st_mode | 0o100
oct(s.st_mode)

os.chmod('b.py', s.st_mode | 0o100)

import stat

stat.S_IXUSR

for fn in os.listdir('.'):
    if fn.endswith(('.py','.sh')):
        fs = os.stat(fn)
        os.chmod(fn, fs.st_mode | stat.S_IXUSR)
