'''
# Open a file
fo = open("foo.txt", "w")
fo.write("test strig\n")
fo.write("test strig1111\n")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()
'''


fo = open("foo.txt", "r+")
str = fo.read(50)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)
# Close opened file
fo.close()
