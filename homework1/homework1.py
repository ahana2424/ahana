# File: homework1.py

# Variables and Data Types
a = 10 
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a collection of items

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection of key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an ordered collection of items

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a collection of items

i = True
print(i)
print(type(i)) # i is a boolean, a value that can be either True or False   

j = None
print(j)
print(type(j)) # j is NoneType, a special type that represents the absence of a value or a null value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a collection of items

l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a number with decimals

"""Questions:
1. How many different data types did you find?
    9
2. List all the data types you found.
    int
    float
    complex
    string
    list
    dictionary
    tuple
    boolean
    NoneType
3. What variables have the same data types?
    b and m are both floats
    d and l are both strings
    e, h, and k are both lists
4. What is the data types of l? Why is it not an integer? What does str() do?
    The data type of l is a string. It is not an integer because the str() converts the integer 14 into a string
5. Look up one more data type not given above. Repeat the same procedure
    range
    """
n = range(5)
print(n)
print(type(n)) # n is a range, a sequence of numbers generated within a specified range

#Booleans
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10<= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, non-empty string is considered True
print(bool(123)) # True, non-zero number is considered True
print(bool(["apple", "cherry", "banana"])) # True, non-empty list is considered True
print(bool(True)) # True, boolean value True is considered True
print(bool(False)) # False, boolean value False is considered False
print(bool(0)) # False, zero is considered False
print(bool("")) # False, empty string is considered False
print(bool(" ")) # True, non-empty string with a space is considered True
print(bool(())) # False, empty tuple is considered False
print(bool([])) # False, empty list is considered False
print(bool({})) # False, empty dictionary is considered False
print(a)
print(bool(True and False)) # False, True and False is considered False
print(bool(True and True)) # True, True and True is considered True
print(bool(False and False)) # False, False and False is considered False
print(bool(True or False)) # True, True or False is considered True
print(bool(True or True)) # True, True or True is considered True
print(bool(False or False)) # False, False or False is considered False
print(bool(not(False))) # True, not False is considered True
print(bool(not(True))) # False, not True is considered False

"""Questions:
What pattern do you notice about eperssions returing True or False?
    If there's both true and false, then for and it defaults to false, but for or it defaults to true. If there's only one value, then it will return that value.
Which expression surprised you about its result?
    bool(True or False)
Create an expression, not given above, that returns True. Why is it True.
    bool(5 > 3) # This expression returns True because 5 is indeed greater than 3.
Create an expression, not given above, that returns False. Why is it False.
    bool(2 == 3) # This expression returns False because 2 is not equal to 3.
    """

# Operators
#Arithmetic Operators
print(10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction
print(2*4) # 8, * performs multiplication
print(6/3) # 2, / performs division
print(5%2) # 1, % performs modulus, returns the remainder of the division
print(3**2) # 9, ** performs exponentiation, raises 3 to the power of 2
print(15//2) # 7, // performs floor division, returns the largest integer less than or equal to the division result

#Comparison Operators
print(5==2) # False, == checks if two values are equal
print(10 != 10) # False, != checks if two values are not equal
print(2<5) # True, < checks if the left value is less than the right value
print(12>5) # True, > checks if the left value is greater than the right value
print(5 <= 6) # True, <= checks if the left value is less than or equal to the right value
print(1>= 10) # False, >= checks if the left value is greater than or equal to the right value

#Assignments Operators
x = 5
x += 5  #adds and assigns the value to the variable
print(x)
x -= 4  #subtracts and assigns the value to the variable
print(x)
x *= 3  #multiplies and assigns the value to the variable
print(x)

#Logical Operators

#1. What does the operator and do? Write an expression that results in True. Write an expression that results in False.
    #The operator and returns True if both operands are True, otherwise it returns False.
bool(True and True)
bool(True and False)
#2. What does the operator or do? Write an expression that results in True. Write an expression that results in False.
    #The operator or returns False if both operands are False, otherwise it returns True.
bool(False or True)
bool(False or False)
#3. What does the operator not do? Write an expression that results in True. Write an expression that results in False.
    #The operator not returns True if the operand is False, and returns False if the operand is True.
bool(not(False))
bool(not(True))

#More Questions
#1. What is the difference between / and //?
    #The operator / performs standard division and can return a float result, while the operator // performs floor division and returns the largest integer less than or equal to the division result
#2. What is the difference between % and //?
    #The operator % returns the remainder of a division operation, while the operator // returns the largest integer less than or equal to the division result.
#3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
    #The operator % is used to calculate the remainder when dividing two numbers. For example, 15 % 4 returns 3.
#4. How do assignment operators work?
    #Assignment operators are used to assign values to variables. They can also perform an operation on the variable and assign the result back to the variable.

my_string = "hello"
print(my_string) # prints: hello
print(my_string[0]) # prints: h, prints the first character of the string
print(my_string[1]) # prints: e, prints the second character of the string
print(my_string[2]) # prints: l, prints the third character of the string
print(my_string[3]) # prints: l, prints the fourth character of the string
print(my_string[4]) # prints: o, prints the fifth character of the string
print(my_string[-1]) # prints: o, prints the last character of the string
print(my_string[1:3]) # prints: el
print(my_string[0:5:2]) # prints: hlo, prints every second character from index 0 to 4
print(len(my_string)) # prints: 5, prints the length of the string
print(my_string + "goodbye") # prints: hellogoodbye
print(my_string * 7) # prints: hellohellohellohellohellohellohello, repeats the string 7 times

"""Questions:
1. Define the term slicing. For which of the manipulations did you slice your string?

    Slicing is used to extract a portion of a sequence by specifying a start index, an end index, and an optional step value. Slicing was used in the following lines:
    - print(my_string[1:3])
    - print(my_string[0:5:2])
    """
#2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)
# The result is: Hello, my name is Oski.

#3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
# The result is: Hello, my name is Oski. This is an example of an f-string.
#4. What is the difference between the two last print statements?
    #The first print statement uses string concatenation to combine the string "Hello, my name is" with the variable `name`, while the second print statement uses an f-string to embed the value of the variable `name` directly within the string.

#Terminal Commands

"""
cd
changes directories. use it to move from one folder to another
eg: cd desktop

ls
lists the contents of the current directory. use it to see what files and folders are in the current directory
eg: ls

ls -a
lists all files and folders, including hidden ones. use it to see all files and folders in the current directory
eg: ls -a

mkdir
creates a new directory. use it to create a new folder
eg: mkdir new_folder

cat
displays the contents of a file. use it to view the contents of a file
eg: cat file.txt

pwd
prints the current working directory. use it to see the full path of the current directory
eg: pwd

cd ..
moves up one directory level. use it to go back to the parent directory
eg: cd ..

cd .
keeps you in the current directory. use it to stay in the current directory
eg: cd .

cd ~
moves to the home directory. use it to go to your home directory
eg: cd ~

cp 
copies a file or directory. use it to make a copy of a file or folder
eg: cp file.txt new_file.txt

mv
moves a file or directory. use it to move a file or folder to a new location
eg: mv file.txt new_folder/

rm
removes a file or directory. use it to delete a file or folder
eg: rm file.txt

clear
clears the terminal screen. use it to remove all previous commands and output from the terminal
eg: clear

grep
searches for a specific pattern in a file or output. use it to find specific text in a file or output
eg: grep "hello" file.txt
"""
"""Questions:
1. Look up 3 other commands not present. Define and explain how to use them on the command line.
    touch: creates a new empty file. use it to create a new file in the current directory
    nano: opens a text editor in the terminal. use it to create or edit text files directly in the terminal
    head: displays the first 10 lines of a file. use it to quickly view the beginning of a file without opening the entire file
2. What is the difference between ls and ls -a?
    The command ls lists the contents of the current directory, while ls -a lists all files and folders, including hidden ones.
3. What is a hidden file?
    A hidden file is a file that is not normally visible when listing the contents of a directory. Hidden files have names that start with a dot (.) and are used for configuration or system purposes.
4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
    -r: reverses the order of the output. use it with commands like ls to display the contents in reverse order
    -l: displays detailed information about files and directories. use it with commands like ls to see file permissions, ownership, size, and modification date
    -h: displays file sizes in a human-readable format. use it with commands like ls -l to see file sizes in KB, MB, or GB instead of bytes
"""
