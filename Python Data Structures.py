# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:48:48 2019

@author: D17911
"""
## Python Data Structures

## String Data Type
## A string is a dequence of characters
## A string literal uses quotes 'Hello' or "Hello"
## For strings, + means 'concatenate'
## When a strong contains numbers, it is still a string
## We can convert numbers in a string into a number using int()

str1 = 'Hello'
str2 = "there"
bob = str1 + str2
print(bob)
str3 = '123'
str3 = str3 + 1
x = int(str3) + 1
print(x)

## Reading and Converting
## We prefer to read data in using strings and then parse and convert the data as we needed
## This gives us more control over error situations and /or bad user input
## Input numbers must be converted from strings, the input() only has character outcomes.
name = input('Enter: ')
print(name)
apple = input('Enter: ')
x = apple - 10  ## this will give error message
x = int(apple) - 10
print(x)
       
## Looking Inside Strings
## We can get at any single character in a string using an index specified in square brackets
## The index value must be an integer and starts at zero
## The index value can be an expression that is computed
## Example:
## b a n a n a
## 0 1 2 3 4 5
fruit = 'banana'
letter = fruit[1]
print(letter)
## output is 'a'
x = 3
w = fruit[x - 1]
print(w)
## Output is 'n'
## python position index starts from 0

## A character Too Far, beyong the length of the string
## You will get a Python error if you attempt to index beyond the end of a string
## So be careful when constructing index values and slices
zot = 'abc'
print(zot[5])
## trackback error bc string index 5 is greater than largest string index 2

## Strings Have Length
## The built-in function len() gives us the length of a string
fruit = 'banana'
print(len(fruit))  ## output is 6 which means largest string index is 6 - 1 = 5
## len() is a function which is some stored code that we use. A function takes some input and produces an output.

## Looping Through Strings
## Using a while statement(indefinite loop) and an iteration variable, and the len() function, we can construct a loop to look at each of the letters in a string individually
fruit = 'banana'
index = 0
while index < len(fruit) :
    letter_f = fruit[index]
    print(index, letter_f)
    index = index + 1
print(index)
#0 b
#1 a
#2 n
#3 a
#4 n
#5 a
#6

## Using definite loop: A definite loop using a for statement is much elegant
## The iteration variable is completely taken care of by the for loop
fruit = 'banana'
for letters in fruit:  ## iteration variable letter taking on all the successive values of the characters of fruit
    print(letters)
## use for loop always when it is simpler

## Looping and Counting: how many 'a' in a word
## This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters the 'a' character
word = 'banana'
count = 0
for letter in word:
    if letter == 'a' :
        count = count + 1
print(count)

## Looking Deeper into 'in'
## The iteration variable 'iterates' through the sequence (ordered set)
## The block(body) of code is executed once for each value in the sequence
## The iteration variable moves through all of the values in the sequence
for letter in 'banana' :
    print(letter) ## letter is iteration variable and 'banana' is Six-character string
## The iteration variable 'iterates' through the string and the block(body) of code is executed once for each value in the sequence
   
## Slicing Strings: do not need to loop, just grab something from a string
## We can also look at any continuous section of a string using a colon operator :
## The second number is one beyond the end of the slice - 'up to but not including'
## If the second number is beyond the end of the string, it stops at the end
## M o n t y   P y t h o n
## 0 1 2 3 4 5 6 7 8 9 10 11
s = 'Monty Python'
print(s[0:4])  ## up to but do not include the index position 4, so only 0 1 2 3
## Mont
print(s[6:7])
## P
print(s[6:20])
## Python
## If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively
print(s[:2])
## Mo
print(s[8:])
## thon
print(s[:])
## Monty Python

## Manipulating Strings - Continued
## String Concatenation
## When the + operator is applied to strings, it means 'concatenation'
a = 'Hello'
b = a+ 'There'
print(b)
## HelloThere
c = a + ' ' + 'There'
print(c)
## Hello There

## Using 'in' as a Logical Operator
## The 'in' keyword can also be used to check to see if one string is 'in' another string
## The 'in' expression is a logical expression that returns True or False and can be used in an if statement
fruit = 'banana'
'n' in fruit    ## 'in' is like '=='
## True
'm' in fruit
## False
'nan' in fruit
## True
if 'a' in fruit :
    print('Found it')
## Found it

## String Comparison
word = input('Your word: ')
if word == 'banana' :
    print('All right, bananas.')
if word < 'banana' :
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana' :
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

## String Library  (String Method)
## Python has a number of string functions which are in the string library
## These functions are already built into every string - we invoke them by appending the function to the string variable
## These functions do not modify the original string, instead they return a new string that has been altered
greet = 'Hello Bob'
zap = greet.lower()  ## string.lower(), basically is pass the string to the lower() function
print(zap)
## hello bob
print(greet)
## Hello Bob
print('Hi There'.lower())  ## .lower() make a copy and turn all cases into small letters
## hi there
## .lower()  : OBJECT METHOD
stuff = 'Hello World'
type(stuff)   ## class str
dir(stuff)  ## it shows what a string is capable of, methods in class str
#['__add__',
# '__class__',
# '__contains__',
# '__delattr__',
# '__dir__',
# '__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__getitem__',
# '__getnewargs__',
# '__gt__',
# '__hash__',
# '__init__',
# '__init_subclass__',
# '__iter__',
# '__le__',
# '__len__',
# '__lt__',
# '__mod__',
# '__mul__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__rmod__',
# '__rmul__',
# '__setattr__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# 'capitalize',
# 'casefold',
# 'center',
# 'count',
# 'encode',
# 'endswith',
# 'expandtabs',
# 'find',
# 'format',
# 'format_map',
# 'index',
# 'isalnum',
# 'isalpha',
# 'isdecimal',
# 'isdigit',
# 'isidentifier',
# 'islower',
# 'isnumeric',
# 'isprintable',
# 'isspace',
# 'istitle',
# 'isupper',
# 'join',
# 'ljust',
# 'lower',
# 'lstrip',
# 'maketrans',
# 'partition',
# 'replace',
# 'rfind',
# 'rindex',
# 'rjust',
# 'rpartition',
# 'rsplit',
# 'rstrip',
# 'split',
# 'splitlines',
# 'startswith',
# 'strip',
# 'swapcase',
# 'title',
# 'translate',
# 'upper',
# 'zfill']
str.capitalize()    ## abc -- Abc; ABC -- Abc
str.center(width[, fillchar])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])
str.replace(old, new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()

## Searching a String
## We use the find() function to search for a substring within another string
## find() finds the first occurrence of the substring, returns the first position index
## If the substring is not found, find() returns -1
## Remember that string position starts at zero
fruit = 'banana'
pos = fruit.find('na')
print(pos)
## 2 the index position
aa = fruit.find('z')
print(aa)
## -1  did not find it

## Making Everything UPPER CASE
## You can make a copy of a string in lower case or upper case
## Often when we are searching for a string using find() we first convert the string to lower case so we can search a string regardless of case
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
## HELLO BOB
www = greet.lower()
print(www)
## hello bob

## Search and Replace: replace(old, new)
## The replace() function is like a 'search and replace' operator in a word processor  
## It replaces all occurrences(all!!) of the search string with the replacement string
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
## Hello Jane
nstr = greet.replace('o', 'X')
print(nstr)
## HellX BXb
                                                  
## Striping Whitespace
## Sometimes we want to take a string and remove whitespace at the beginning and /or end
## lstrip() and rstrip() remove whitespace at the left or right
## strip() removes both beginning and ending whitespace
greet = '        Hello Bob     '
greet.lstrip()
## 'Hello Bob       '
greet.rstrip()
## '        Hello Bob'
greet.strip()
## 'Hello Bob'

## Prefixes
line = 'Please have a nice day'
line.startswith('Please')
## True
line.startswith('p')
## False
## Later we can use if to do something if there is a specific prefixes

## Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
## we want to extract 'uct.ac.za
atpos = data.find('@')
print(atpos)
## 21 which means we should extract at the index position 22
sppos = data.find(' ', atpos)  ## it means find the position of data that starts from atpos and the first space index position is ?
print(sppos)
## 31  This is where we up to but not include
host = data[atpos + 1: sppos]
print(host)

## Chapter 6 Exercises
## 6.5 Parsing Text Strings
text = "X-DSPAM-Confidence:    0.8475";
print(text)
pos = text.find(' ')
print(float(text[pos+1:]))
## Charles Method
ipos = text.find(':')
print(ipos)
piece = text[ipos+1 : ]
print(piece)
## strip(piece)
value = float(piece)
print(value)

## Chapter 7 - 7.1 - Files
## Flat Textfiles: set of lines that program can read
## File Processing: A text file can be thought of as a sequence of lines

## Opening a File
## Opening a File (It is not reading the file, it just making the file available to the code that to be write)
## Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file
## This is done with the open() function
## open() returns a 'file handle' -  a variable used to perform operations on the file
## Similar to "File -> Open" in a window Processor

## Using open()
handle = open(filename, mode)  ## mode can be read or write ('w'), default is read ('r')
## It returns a handle use to manipulate the file
## Filename is a string
## mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file
fhand = open('mbox.txt', 'r')  ## file handle is not the data, it is just the connecyions to the data
print(fhand)   ## <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
## Handle is a portal between the file and code so that we can open, read, write and close

## The newline Character
## We use a special character called the 'newline' to indicate when a line ends
## We represent it as \n in strings
## Newline is still one character - not two
stuff = 'Hello\nWorld!'
stuff   ## 'Hello\nWorld!'
print(stuff)
## Hello
## World!
stuff = 'X\nY'
stuff[1]  ##\n
print(stuff)
## X
## Y
len(stuff)   ## 3 (notice: not 4)

## Files - 7.2 Processing Files  (Read in Python)
## File Handle as a Sequence
## A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
## We can use the for statement to iterate through a sequence. The number of iterates in for loop is the number of lines in the file.
## Remember - a sequence is an ordered set
xfile = open('mbox.txt', mode='r')
for cheese in xfile:
    print(cheese)

## Counting Lines in a File
## Step 1: Open a file read-only
## Step 2: Use a for loop to read each line
## Step 3: Count the lines and print out the number of lines
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

## Reading the *Whole* File
## We can read the whole file(newlines and all) into a single string
fhand = open('mbox-short.txt')
inp = fhand.read()  ## the read() function does not split into lines, it is like abcdefg\nabcdefg\nabcdefg\n......
## read whole things into a string
print(len(inp))  ## 94626
print(inp[:20])   ## From stephen.marquar

## Seaching Through a File
## We can put an if statement in our for loop to only print lines that meet some criteria
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
## Actually, the output above will cause some problem, it will have a blank line between each line.
## What are all these blank lines doing here?
## Each line from the file has a newline at the end 
## And the print statement adds a newline to each line
## Output:
#    abcdefg\n --- the text file ends with this
#    \n   --- the print statement did this
#    abcdefg\n
#    \n
#    abcdefg\n
## Solution Fixed
## We can strip the whitespace from the right-hand side of the string using rstrip() from the string library.
## The newline is considered 'white space' and is stripped
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()  ## wipe out the new line on the string
    if line.startswith('From:'):
        print(line)  ## print() add new line
## Output:
#    abcdefg/n
#    abcdefg/n
#    abcdefg/n

## Skipping with Continue (the same output above)
## We can conveniently skip a line by using the continue statement
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue   ## skip
    print(line)

## Using in to Select lines
## We can look for a string anywhere in a line as our select criteria
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

fname = input('Enter the file name: ')
## mbox.txt
## mbox-short.txt
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()  ## quit() from reading next line, quit but never returns from
    
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)


## Exercise 7.1  
# Use words.txt as the file name
## The file should be in the same directory 
pwd()
#'C:\\Users\\D17911'
## so we need to change directory
from os import chdir, getcwd
getcwd()  #'C:\\Users\\D17911'
chdir('\\\\WIL-HOMEDRIVE01\D17911$\Desktop\Courses\Python for Data Science\Week 1')
getcwd()   ## '\\\\WIL-HOMEDRIVE01\\D17911$\\Desktop\\Courses\\Python for Data Science\\Week 1'
fname = input("Enter file name: ")
fh = open(fname)
print(fh)   ## <_io.TextIOWrapper name='mbox-short.txt' mode='r' encoding='cp1252'> is not the data.
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)

## Exercise 7.2
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    line = line.rstrip()
    count = count + 1
    pos = line.find(':')
    total = total + float(line[pos+1:])

print('Average spam confidence:', float(total/count))


## Chapter 8: Lists --  Ways to use variables differently
## Algorithms: A set of rules or steps used to solve a problem 
## Data Strunctures: A particular way of organizing data in a computer. Lists, Dictionaries and Tuples are the first three data structures
## Collections of variables: more than one value in a variables

## What is Not A 'Collection'?
## Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten
## Example:
    x = 2
    x = 4
    print(x)   ## 4

## A List is a Kind of Collection
## A collection allows us to put many values in a single 'variable'
## A collection is nice because we can carry many values around in one convenient package
friends = ['Joseph', 'Glenn', 'Sally']   ## square bracket is a list constant
carryon = ['socks', 'shirts', 'perfume']

## List Constants
## List constants are surrounded by square brackets and the elements in the list are separated by commas.
## A list element can be any Python object/type - even another list.  
## A list can be empty
print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5, 6], 7])  ## This is a three elements list: integer, list, string
print([])

## We Already Use Lists
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']  
for friend in friends:
    print('Happy New Year:', friend)
print('Done')

## Looking Inside Lists
## Just like strings, we can get at any single element in a list using an index specified in square bracket
print(friends[1])    ## use the index postion, answer is 'Glenn'

## Lists Are Mutable, Can be change!!!!!!!
## Strings are immutable - we can not change the contents of a string -  we must make a new string to make any change
## Lists are mutable -  We can change an element of a list using the index operator
## Lists through the function operation can not be assigned to a new variable
fruit = 'Banana'
fruit[0] = 'b'   ## String is immutable
## This gives a traceback, Type Error
x = fruit.lower()
print(x)    ## We can only do this to change string, make a new variable
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)
## [2, 14, 28, 41, 63]   This is the output  

## How Long is a List?
## The len() function takes a list as a parameter and returns the number of elements in the list
## Actually len() tells us the number of elements of any set or sequqence(such as a string)....
greet = 'Hello Bob'
print(len(greet))  ## 9
x = [ 1, 2, 'joe', 99]
print(len(x))   ## 4: means four elements in this list

## Using Range Function, range() returns a list
## The range function returns a list of numbers that range from zero to one less than the parameter, like the index position.
## We can construct an index loop using for and an integer iterator
print(range(4))   ## Answer: [0, 1, 2, 3]
friends = ['Joseph', 'Glenn', 'Sally'] 
print(len(friends))  ## 3
print(range(len(frineds)))   ## [0, 1, 2]

## A Tale of Two Loops...
friends = ['Joseph', 'Glenn', 'Sally']  

for friend in friends:
    print('Happy New Year:', friend)
for i in range(len(friends)):     ## The same output but it is a counted a loop, we know the position
    friend = friends[i]
    print('Happy New Year:', friend)
print(len(friends))   ## 3
print(range(len(friends)))   ## [0, 1, 2]

## 8.2 Manipulating Lists
## Operations to do with Lists

## Concatenating Lists Using '+'
## We can create a new list by adding two existing lists together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)    ## [1, 2, 3, 4, 5, 6]
print(a)    ## [1, 2, 3]

## Lists Can Be Sliced Using ':' -- Just like String Slicing
## Remember: Just like in strings, the second number is 'up to but not including'
t = [9, 41, 12, 3, 74, 15]
t[1:3]    ## [41, 12]
t[:4]    ## [9, 41, 12, 3]
t[3:]    ## [3, 74, 15]
t[:]     ## [9, 41, 12, 3, 74, 15]

## Lists Librarys  (Lists Methods)
x = list()
type(x)   ## list
dir(x)
#['__add__',
# '__class__',
# '__contains__',
# '__delattr__',
# '__delitem__',
# '__dir__',
# '__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__getitem__',
# '__gt__',
# '__hash__',
# '__iadd__',
# '__imul__',
# '__init__',
# '__init_subclass__',
# '__iter__',
# '__le__',
# '__len__',
# '__lt__',
# '__mul__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__reversed__',
# '__rmul__',
# '__setattr__',
# '__setitem__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# 'append',
# 'clear',
# 'copy',
# 'count',
# 'extend',
# 'index',
# 'insert',
# 'pop',
# 'remove',
# 'reverse',
# 'sort']

## Building a List from Scratch
## We can create an empty list and then add elements using the append method
## The list stays in order and new elements are added at the end of the list
stuff = list()  ## this is constructor and list is a predefined type
stuff.append('book')
stuff.append(99)
print(stuff)   ## ['book', 99]
stuff.append('cookie')
print(stuff)    ## ['book', 99, 'cookie']
## lists are mutable, so append() method change variable unlike (string immutable and return variable)
## So that why we can use 'line = line.rstrip() when line is a string' because string can return variable
## We can not use "stuff = stuff.append('book')" when stuff is list because list can change variable
stuff = stuff.append('abc')
print(stuff)    ## Answer: None

## Is Something in a List?
## Python provides two operators that let you check if an item is in a list (in, not in)
## These are logical operators that return True or False, they do not modify the list
some = [1, 9, 21, 10, 16]
9 in some     ## True
15 in some    ## False
20 not in some    ## True

## Lists are in Order
## A list can hold many items and keeps those items in the order until we do something to change the prder (insert, etc)
## A list can be sorted (i.e., change its order)
## The sort method (unlike in strings) means 'sort yourslf'
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)    ## ['Glenn', 'Joseph', 'Sally']
print(friends[1])   ## Joseph

## Built-in Functions and Lists
## There are a number of functions built into Python that take lists as parameters
## Remember the loops we built? (min, max, sum, count, mean). These built-in functions are much simpler
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))    ## 6
print(max(nums))   ## 74
print(min(nums))    ## 3
print(sum(nums))    ## 154
print(sum(nums)/len(nums))    ## 25.6

## Compare we do the loop versus how we use the method to calculate the same thing
## Earlier chapter
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    count = count + 1
    total = total + float(inp)
average = total / count
print('Average', average)

## Function Calculation
numlist = list()
while True:
    inp = input('Enter a Number: ')
    if inp == 'done':
        break
    numlist.append(float(inp))
average = sum(numlist) / len(numlist)
print('Average:', average)
## The difference is that the function calculation keeps all the numbers in memory and create a list
## The first method loop calculation does not keep all the numbers, it just keep the latest count and total (two numbers) in memory which is good when we have super large dataset
## But the function calculation is somehow convenient when you have numbers in the list, which do not need to use for loop to accumulate

## 8.3 Lists and Strings
## Best Friends: Strings and LIsts
abc = 'With three words'
stuff = abc.split()       ## split() string method and takes a string and gives us back a list
print(stuff)    ## ['With', 'three', 'words']
print(len(stuff))   ## 3
print(stuff[0])   ## With
print(stuff)     ## ['With', 'three', 'words']
for word in stuff:
    print(word)
## With
## three
## words
## split() function breaks a string into parts and produces a list of strings(list). We think of these as words
## We can access a particular word or loop through all the words
line = 'A lot          of spaces'
etc = line.split()
print(etc)    ## ['A', 'lot', 'of', 'spaces']
line = 'first;second;third'
thing = line.split()
print(thing)    ## ['first;second;third']
print(len(thing))   ## 1
thing = line.split(';')  ## It will only split by the things we specified and remain the space
print(thing)  ## ['first', 'second', 'third']
print(len(thing))   ## 3
## When you do not specify a delimiter, multiple spaces are treated like one delimiter(space)
## You can specify what delimiter character to use in the splitting
## Example, we want to know the weekdays in string
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'   ## get Sat
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words)
    print(words[1])
    
## Another example we want to extract 'uct.ac.za
## Old ways
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
## 21 which means we should extract at the index position 22
sppos = data.find(' ', atpos)  ## it means find the position of data that starts from atpos and the first space index position is ?
print(sppos)
## 31  This is where we up to but not include
host = data[atpos + 1: sppos]
print(host)
## New Way --  Not right, It has duplicates
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    new_words = words[1].split('@')
    print(new_words[1])

## The Double Split Pattern, Not right, have traceback IndexError: list index out of range
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    email = words[1]
    pieces = email.split('@')    
    print(pieces[1])

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')    
print(pieces[1])
## Chapter 8 Exercise 8.4
## Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
## The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for piece in words:
        if piece in lst:
            continue
        lst.append(piece)
lst.sort()
print(lst)

## Exercise 8.5  *solve the wrong palce above about duplicate and traceback
## Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
## You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
## Wrong way --  Duplicates:   why?? It does not need to deal with dangerous code, but it has duplicates
## The reason why duplicates is in the context we have 'From' and 'From:', so we have to use words[0]=='From'
fname = input('Enter your file: ')
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From:'):   
        continue
    count = count + 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")

## Correct Way
han = open('mbox-short.txt')
count = 0
for line in han:
    line = line.rstrip()
    words = line.split()   ## The last line is blank so that last list is also blank
    ## print('words:', words)
    ## Guardian Pattern a little bit stronger
    if len(words) < 2:
        continue
    if words[0] != 'From':  ## That why cause trackback in the last row, because blank list can not use position index
       ## print('Ignore')
        continue
    count = count + 1
    print(words[1])
print('There were', count, 'lines in the file with Fron as the first word')

han = open('mbox-short.txt')
count = 0
for line in han:
    line = line.rstrip()
    words = line.split()   ## The last line is blank so that last list is also blank
    ## print('words:', words)
    ## Guardian in a compund statement
    if len(words) < 2 or words[0] != 'From':  ## That why cause trackback in the last row, because blank list can not use position index
    ## We must put the len() and words[0] != 'From' in order otherwise we will have traceback again
    ## Because if words[0] != 'From' at the front, it will check this first and still have error with the line is blank
    ## print('Ignore')
        continue
    count = count + 1
    print(words[1])
print('There were', count, 'lines in the file with From as the first word')


## Chapter 9. Dictionaries
## Chapter 9.1 Dictionaries
## What is a Collection?
## 1. A collection is nice because we can put more than one value in it and carry them all around in one convenient package
## 2. We have a bunch of values in a single 'variable'
## 3. We do this by having more than one place 'in' the variable
## 4. We have ways of finding the different palces in the variable
## List: A linear collection of values that stay in order, position index is the key
## Distionary: A 'bag' of values, each with its own label. Their order shifts around but it is key value pair and you give each item a key and also a label

## 1. Dictionaries are Python's most powerful data collection
## 2. Dictionaries allow us to do fast database - like operations in Python
## 3. Dictionaries have different names in different languages:
##    -- Dictionaries - Python
##    -- Associative Arrays - Perl / PHP
##    -- Properties or Map or HashMao - Java
##    -- Property Bag - C# / .Net

## Lists index('money', 'candy', 'tissues') their entries based on the position in the list
## Dictionaries are like bags - no order
## So we index the things we put in the dictionary with a 'lookup tag'
purse = dict()   ## constructor an empty dictionary object
purse['money'] = 12  # money' is the key (label) and 12 is value, key-value pair
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
# {'money': 12, 'candy': 3, 'tissues': 75},  curly braces are for dictionaries, note for the order, order is unpredictable
print(purse['candy'])
# 3
purse['candy'] = purse['candy'] + 2   ## dictionary contents are mutable and can be assigned to a variable
print(purse)     
# {'money': 12, 'candy': 5, 'tissues': 75}
## Comparing Lists and Dictionaries
## Dictionaries are like lists except that they use keys instead of numbers to look up values and dictionary do not have order
lst = list()
lst.append(21)
lst.append(183)
print(list)   ## [21, 183]
lst[0] = 23
print(lst)  ## [23, 183]

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)   ## {'age': 21, 'course': 182}
ddd['age'] = 23
print(ddd)   ## {'age': 23, 'course': 182}
## Dictionary Literal (Constants)
## Dictionary literals use curly braces and have a list of key : value pairs
## You can make an empty dictionary using empty curly braces
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}  ## Dictionary Constant ## Usually, we use string for keys and numbers for values, but that does not necessary
print(jjj)
ooo = { }
print(ooo)

## 9.2 Counting with Dictionaries
## Count the number of words appear and the most common name
## One common use of dictionaries is counting how often we 'see' something
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)  ## {'csev': 1, 'cwen': 1}
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)  ## {'csev': 1, 'cwen': 2}
## Dictionary Tracebacks
## It is an error to reference a key which is not in the dictionary
## We can use the in operator to see if a key is in the dictionary
ccc = dict()
print(ccc['csev']) ## KeyError: 'csev'
'csev' in ccc    ## False

## When We See a New Name
## When we encounter a new name, we need to add a new entry in the dictionary and if this the second or later time we have seen the name, 
## we simply add one to the count in the dictionary under that name.
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
## {'csev': 2, 'cwen': 2, 'zqian': 1}

## The get() Method for Dictionaries
## The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us.
## Default value if key does not exist (and no Traceback)
if name in counts :
    x = counts[name]
else :
    x = 0
x = counts.get(name, 0)  ## It will not give trackback, if we did not find the key
## name is the key and 0 is default, if the key is not in the dictionary, it will return back 0
## Below does exactly the same thing in the if and else conditional statement
## Simplifies Counting with get()
## We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1  
print(counts)   ## {'csev': 2, 'cwen': 2, 'zqian': 1}

## 9.3 Dictionaries and Files

## Counting Pattern
counts = dict()
print('Enter a line of text:')
line = input('')  ## give a string within the quote
words = line.split()
print('Words:', words)
print('Counting ...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)
## The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently.
    
## For loop go through a Dictionary
## Definite Loops and Dictionaries
## Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary -- 
## actually it goes through all of the keys in the dictionary and looks up the values
counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts :   ## Unlike strings or lists, the dictionary goes through keys, strings and lists go through values
    print(key, counts[key])
#chuck 1
#fred 42
#jan 100

## Retrieving lists of Keys and Values
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))   ## Get a list of keys
## Answer: ['chuck', 'fred', 'jan']
print(jjj.keys())  ## dict_keys(['chuck', 'fred', 'jan'])
print(jjj.values())  ## dict_values([1, 42, 100])   ## This is the corresponding order of dictionary keys
print(jjj.items())  ## dict_items([('chuck', 1), ('fred', 42), ('jan', 100)]), 3 item list, each item is a data structure called tuple
## You can get a list of keys, values, or items(both) from a dictionary

## the .items() gives us Two Iteration Variables!!p
## We loop through the key-value pairs in a dictionary using *two* iteration variables
## Each iteration, the first variable is the key and the second variable is the corresponding value fro the key
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa, bbb in jjj.items():
    print(aaa, bbb)
#chuck 1
#fred 42
#jan 100
## Application Example, find the word with the largest number of appearance 
name = input('Enter a file: ')
handle = open(name)
counts = dict()
for line in name :
    line = line.rstrip()   ## do not necessary for the strip, because split() will do this automatically
    line = line.split()
    for word in line :
        counts[word] = counts.get(word, 0) + 1
bigcount = None   ## we can not use the max() to find the maximum, because all of them are hidden inside the dictionary
bigword = None
for word, count in counts.items() :
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)

## Exercise chapter 9.4
## Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
## he program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
fhand = open(name)
counts = dict()

for line in fhand :
    line  = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    word = words[1]
    counts[word] = counts.get(word, 0) + 1
## print(counts)
        
bigname = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = word
        bigcount = count
    ## print(bigname, bigcount)
print(bigname, bigcount)

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words :
        # If the key is not there the count is zero, alternative way:
        # oldcount = counts.get(word, 0)
        # print(word, 'old', oldcount)
        # newcount = oldcount + 1
        # counts[word] = newcount  
        print(word)
        if word in counts : 
            counts[word] = counts[word] + 1
            print('** Existing **')
        else :
            counts[word] = 1
            print('** New **')
        print(counts[word])
print(counts)


fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words :
        ## Idiom: retrieve/create/update counter
        counts[word] = counts.get(word, 0) + 1      
print(counts)
## Now we want to find the most common words
largest = -1
word = None
for key, value in counts.items():
    if value > largest :
        largest = value
        word = key  ## capture/remember the key that was the largest
print('Done', word, largest)


## Chpater 10 Tuples
## Def: Tuples are a limited version of lists which is unable to modify
## Tuples are Like Lists:
## Tuples are another kind of sequence that functions much like a list - They have elements which are indexed starting at 0
x = ('Glenn', 'Sally', 'Joseph')   ## Note: Not bracket, it is the parentheses  ## x is a three tuples with three strings in it
print(x[2])   ## Joseph
y = (1, 9, 2)
print(y)  ## (1, 9, 2)
print(max(y))   ## 9
for iter in y:
    print(iter)                                              
## Comparing with Lists, Tuples are Immutable
## Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
x = [9, 8, 7]                                              
x[2] = 6
print(x)   ## [9, 8 ,6]
y = 'ABC'
y[2] = 'D'   ## Trackback Error, strings are immutable
z = (5, 4, 3)
z[2] = 0    ## Trackback, Error, tuples are immutable
## Things not to do with Tuples
x = (3, 2, 1)
x.sort()   ## Traceback
x.append(5)  ## Traceback, immutable
x.reverse()   ## Traceback
## Look at the directory(method) of Tuple
l = list()
dir(l)
d = dict()
dir(d)
t = tuple()
dir(t)   ## count, index
#['__add__',
# '__class__',
# '__contains__',
# '__delattr__',
# '__dir__',
# '__doc__',
# '__eq__',
# '__format__',
# '__ge__',
# '__getattribute__',
# '__getitem__',
# '__getnewargs__',
# '__gt__',
# '__hash__',
# '__init__',
# '__init_subclass__',
# '__iter__',
# '__le__',
# '__len__',
# '__lt__',
# '__mul__',
# '__ne__',
# '__new__',
# '__reduce__',
# '__reduce_ex__',
# '__repr__',
# '__rmul__',
# '__setattr__',
# '__sizeof__',
# '__str__',
# '__subclasshook__',
# 'count',
# 'index']                                           
                                              
## Tuples are More Efficient
## Reason 1: Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists
## Reason 2: So in our program when we are making 'temporary varibales', we prefer tuples over lists
                                              
## Tuples and Assignmnet
## We can also put a tuple on the left-hand side of an assignment statement
## We can even omit the parentheses
(x, y) = (4, 'Fred')  ## simultaneous assignment statement
print(y)  ## Fred
(a, b) = (99, 98)
print(a)   ## 99
## Tuple on the left hand side so it expects a tuple on the right hand side
                                              
## Tuples and Dictionaries
## The items() method in dictionaries returns a list of (key, value) tuples
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
#csev 2
#cwen 4
tups = d.items()
print(tups)                                             
#dict_items([('csev', 2), ('cwen', 4)]), a list of two tuples                                              
 
## Tuples are Comparable
## The omparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ.
## Once it find the match comparison, it will ignore the following comparisons
(0, 1, 2) < (5, 1, 2)                                             
## True, it will not compare 1 and 2   
(0, 1, 2) == (0, 5, 2)
## False                                      
(6, 1, 2) < (5, 1, 2)                                               
## False
(0, 1, 200000) < (0, 3, 4)
## True
('Jones', 'Sally') < ('Jones', 'Sam')                                           
## True
('Jones', 'Sally') > ('Adams', 'Sam')                                              
## True

## Sorting Lists of Tuples
## Lists of Tuples can be sorted, but Tuple can not be sorted
## We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
## First we sort the dictionary by the key using the items() method and sorted() function
d = {'a':10, 'c':22, 'b':1}
d.items()
sorted(d.items())        ## [('a', 10), ('b', 1), ('c', 22)]
## It will be sorted based on the keys first
## In dictionaries, you can not have two keys, constructing the dictionary, they keys are going to be unique.
## You can put the value in Dictionaries more than once, but keys can not
                                  
## Using sorted()
## We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence
for k,v in sorted(d.items()):
    print(k, v)        ## It will print out based on the key order                                        
#a 10
#b 1
#c 22                                              

## Sorted by Values Instead of Key
## If we could construct a list of tuples of the form of (value, key) we could sort by value
## We do this with a for loop that creates a list of tuples
c = {'a':10, 'b':1, 'c':22}        
tmp = list()
for (k, v) in c.items():
    tmp.append((v, k))        
print(tmp)  ## [(10, 'a'), (1, 'b'), (22, 'c')]
tmp = sorted(tmp, reverse = True)         
print(tmp)   ## [(22, 'c'), (10, 'a'), (1, 'b')]
tmp = sorted(tmp)         ## Values can be duplicates
print(tmp)  ## [(1, 'b'), (10, 'a'), (22, 'c')]
## Use built-in function can return variable/list, however, use list method, we can not return variable for list
         
## Example: The top 10 most common words
fhand = open('romeo.txt')         
counts = dict()
lst = list()
for lines in fhand:
    lines = lines.rstrip()
    lines = lines.split()
    for word in lines:
        counts[word] = counts.get(word, 0) + 1
for key, value in counts.items():
    ## newtup = (value, key)
    ## lst.append(newtup)
    lst.append((value, key))
lst = sorted(lst, reverse = True)
for value, key in lst[:10] :
    print(key, value)
         
## Even Shorter Version -- List Comprehension
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v, k) for (k, v) in c.items()]))   ## The list in the sorted() is an expression        
## [(1, 'b'), (10, 'a'), (22, 'c')]
## List Comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it         
         
fhand = open('romeo.txt')         
counts = dict()
lst = list()
for lines in fhand:
    lines = lines.rstrip()
    lines = lines.split()
    for word in lines:
        counts[word] = counts.get(word, 0) + 1
print(sorted([(v, k) for (k, v) in counts.items()], reverse = True)[:10])
#[(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'), (1, 'what'), (1, 'through'), (1, 'soft')]         
         
## Chapter 9 Exercise
## 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.         
## Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.         
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for lines in handle:
    lines = lines.rstrip()   
    words = lines.split()
    if len(words) < 6 or words[0] != 'From':
        continue
    word = words[5]
    word = word.split(':')
    time = word[0]
    counts[time] = counts.get(time, 0) + 1
for (k,v) in sorted(counts.items()) :
    print(('%0*d' % (2, int(k)),v))
## Solution 2: if we do not wish to have string outcomes
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
for lines in handle:
    lines = lines.rstrip()   
    words = lines.split()
    if len(words) < 6 or words[0] != 'From':
        continue
    word = words[5]
    word = word.split(':')
    time = word[0]
    counts[time] = counts.get(time, 0) + 1
for (k,v) in  counts.items():
    lst.append((k,v))
lst.sort()
for (k,v) in lst:
    print(k,v)            
                
## Exercise 2
name = input("Enter file:")
if len(name) < 1 :
    name = "clown.txt"
handle = open(name)
counts = dict()
lst = list()         
for lines in handle :
    lines = lines.rstrip()
    words = lines.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1
for (k,v) in sorted(counts.items(), reverse = True)[:5] :
    print(k,v)        
for (k, v) in counts.items():
    lst.append((v, k))         
lst = sorted(lst, reverse = True)
for v,k in lst[:5]:
    print(k, v) 
x = sorted(counts.items(), reverse = True)
print(x[:5])


























       