# Is-it-an-identifier
This program will help you check whether a string can be taken as an identifier or not, in any python program.

#PROGRAM TO FIND FEASIBLE NAMES FOR AN IDENTIFIER

#By:-Srishti Singh

c=input("Enter any string: ")

import keyword

if(keyword.iskeyword(c)==False and c.isidentifier()==True ):

    print("It is an identifier")
	
else:

    print("It is not an identifier")
	
