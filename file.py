#!/usr/bin/env python
import os.path

# Define a filename.
filename = "hello_word.py"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
    content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
for line in content:
    print (line)

if os.path.isfile(filename):
    print('File exist.')

# Filename to write
filename = "newfile.txt"

# Open the file with writing permission
# novo myfile = open(filename, 'w')
myfile = open(filename, 'a')

# Write a line to the file
myfile.write('Written with Python\n')

# Close the file
myfile.close()


# A summary of parameters:
#
# Flag    Action
# r    open file for reading
# w   open file for writing (will truncate file)
# b   binary mode
# r+  open file reading and writing
# a+  open file for reading and writing (appends to end)
# w+  open file for reading and writing (truncates file)