#PROGRAM TO FIND FEASIBLE NAMES FOR AN IDENTIFIER

#By:-Srishti Singh

c=input("Enter any string: ")

import keyword

if(keyword.iskeyword(c)==False and c.isidentifier()==True ):

    print("It is an identifier")
	
else:

    print("It is not an identifier")