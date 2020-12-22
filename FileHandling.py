#/usr/bin/env python
import os
FileName = 'filename.txt'

if os.path.exists('FileName'):
    os.remove(FileName)
else:
    f= open('filename.txt','r')
    #f.write("This is the first line")
    for line in f:
        print(line, end='')
    f.closed
