# Variables and Data types

# Variable is the name of the memory location where we store the data. It is a container that holds data values. there are 5 different types of variables in python. They are: integer , boolean , string , float and NoneType.

#Variables

a = 10 # Integer
b = 20.5 # Float
c = "Ayan" # String
d = None # NoneType
e = True # Boolean

#Data types

#Data types are the classification of data items. It represents the kind of value that tells what operations can be performed on a particular data. There are 5 different types of data in python. They are: integer , boolean , string , float and NoneType.

#Data 

name = "Ayan" # String
age = 20 # Integer  
height = 5.9 # Float
Online_Status = None # NoneType
Living_Status = True # Boolean , [ _ is used to separate the words in a variable name. It is called snake case. ]


# How to find the data type of a variable in python?

print (type(name));
# output:
 # <class 'str'>
print (type(age));
# output
 # <class 'int'>
print (type(height));
# output
 # <class 'float'>

print("The data type of variable name is:", type(name));
print("The data type of variable age is:", type(age));
print("The data type of variable height is:", type(height));
print("The data type of variable Online_Status is:", type(Online_Status));
print("The data type of variable Living_Status is:", type(Living_Status));

# Numeric Data types in python
int = 1 , 4 , 9 , -5 , 0 , 100 # Integer
float = 1.5 , 4.0 , 9.8 , -5.5 , 0.0 , 100.0 # Float
complex = 1 + 2j , 3 + 4j , 5 + 6j , -7 + 8j , 0 + 0j # Complex

#Text Data type in python
string = "Hello" , 'World' , "Python" , 'Programming' , "Data Science" , 'Machine '
'' # String

# Boolean Data type in python
boolean = True , False # Boolean

# -------------------------------------------------------

#Sequence Data  types ( list , tuple ) in python
#Sequence data types ( list , tuple ) are the data types that are used to store a collection of data items.

#list is a collection of data items that are ordered and changeable. It is defined by square brackets [].
list = [1 , 2 , 3 , 4 , 5] # List

# tuple is a collection of data items that are ordered and unchangeable. It is defined by parentheses ().
tuple = (1 , 2 , 3 , 4 , 5) # Tuple