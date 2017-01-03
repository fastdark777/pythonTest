'''
Created on 2017. 1. 3.

@author: lsh
'''



#===============================================================================
# Pass by reference vs value
#===============================================================================


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
print ("Values outside the function: ", mylist)
changeme( mylist );


#===============================================================================
# Default arguments
#===============================================================================

# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )


#===============================================================================
# Variable-length arguments
#===============================================================================
#===============================================================================
# You may need to process a function for more arguments than you specified while 
# defining the function. These arguments are called variable-length arguments and are not named 
# in the function definition, unlike required and default arguments.
#===============================================================================
 
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )



#===============================================================================
# The Anonymous Functions
#===============================================================================

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

 

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
