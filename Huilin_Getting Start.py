# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## comment  very easy steps
print "hello world" ## missing brackets, python 2 works
print("hello world")
raw_input('What is your name?')  ## raw _input only works in python 2
input('What is your name')
x = 1
print(x)
x = x+1
print(x)
exit()

## Count most common words and how many times they appear in Python
## Get the name of the file and open it
name = input('Enter file:')
handle = open(name)

## Count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

## Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

## All done      
print(bigword, bigcount)

## Reserved Words
## You cannot use reserved words as variable names / identifiers
## Reserved words such as:  False class return is finally None if for lambda continue True def from while nonlocal
## Reserved words continued: and del global not with as elif try or yield assert else import pass break except in raise, etc
## If python sees the reserved word, it means something

## Sentences or Lines
x = 2   ## Assignment statement
x = x+2  ## Assignment with expression
print(x)   ## Print function 
## Variable  Operator  Constant  Function

## Python Scripts
## Interactive Python is good for experiments and programs of 3-4 lines long
## Most programs are much longer, so we type them into a file and tell Python to run the command in the file
## In a sense, we are "gibing Python a script"
## As a convention, we add ".py" as the suffix on the end of these files to indicate they contain Python.

## Interactive versus Script
## Interactive: You type directly to Python one line at a time and it responds
## Script: You enter a sequence of statements (lines) into a file using a text editor and tell Python to execute the statements in the file
## Program Steps or Program Flow
## Like a recipe or installation instructions, a program is a sequence of steps to be done in order
x = 1
print(x)
x = x+1
print(x)
## Some steps are conditional - they may be skipped, if statements
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')
## Sometimes a step or group of steps is to be repeated
## Loops(repeated steps) have iteration variables that change each time through a loop
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
## Sometimes we store a set of steps to be used over and over as needed several places throughout the program (Chapter 4)

## Chapter 2 for Python for Everyone
## Expressions Part 1
## Constants
## Fixed values such as numbers, letters, and strings, are called 'constants' because their value does not change
## Numeric constants are as you expect
print(123)
print(98.6)
## String constants use single quotes (') or double quotes (")
print('Hello World')
## Reserved Words
## Variables
## A variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable 'name'
## Programmers get to choose the names of the variables
## You can change the contents of a variable in a later statement
x = 12.2
y = 14
x = 100  ## overwrite
## Python Variable Name Rules
## Must start with a letter or underscore
## Must consist of letters, numbers and underscores
## Case sensitive
## Goodname: spam eggs spam23 _speed
## Badname: 23spam #sign var.12
## Different: SPAM spam Spam
## Understandable Variable Names
a = 35.0
b = 12.50
c = a*b
print(c)
## Mnemonic Names
hours = 35.0
rate = 12.50
pay = hours*rate
print(pay)

## Assignment Statements
## We assign a value to a variable using the assignment statement (=)
## An assignment statement consists of an expression on the right-hand side and a variable to store the result
x = 3.9 * x * (1 -x)
## The right side is an expression. Once the expression is evaluated, the result is placed in(assigned to) the variable on the left side.

## Expressions Part 2
## Numeric Expressions
## Because of the lack of mathematical symbols on computer keyboards - we use 'computer-speak' to express the classic math operations
## Asterisk is multiplication
## Exponentiation (raise to a power) looks different than in math
## Operator: +  Addition; -  Substraction;  *  Multiplication;  /  Division;  **  Power;  %  Remainder; // the integer part;
xx = 2
xx = xx + 2
print(xx)
yy = 440 * 12
print(yy)
xx = yy / 1000
print(zz)
jj = 23
kk = jj % 5
print(kk)
print(4 ** 3)

## Order of Evaluation
## When we string operators together - Python must know which one to do first
## This is called 'operator precedence'
## Which operator 'takes precedence' over the others
x = 1 + 2 * 3 - 4 / 5 ** 6   ## we can always add parentheses
## Operator Precedence Rules:
## Highest precedence tule to lowest precedence rule:
## Parentheses > Exponential > Multiplication, Division, and Remainder > Addition and Subtraction > Left to right

## What does 'Type' Mean?
## In Python variables, literals, and constants have a 'type'
## Python knows the difference between an integer number and a string
## For example '+' means 'addition' if something is a number and 'concatenate' if something is a string
add = 1 + 4
print(add)
eee = 'hello ' + 'there'
print(eee)
## Type Matters
## This example shows Python unhappy: Python knows what "type" everything is
## Some operations are prohibited
## You cannot "add 1" to a string
## We can ask Python what type something is by using the type() function
eee = 'hello ' + 'there'
eee = eee + 1 ## We will have error here
type(eee)  ## String
type('hello')  ## string: str
type(1)  ## int

## Several Types of Numbers
## Numbers have two main types: Integers and Floating Point Numbers
## Integers are whole numbers: -14, -2, 0, 1, 100, 401233
## Floating Point Numbers have decimal parts: -2.5, 0.0, 98.6, 14.0, more ranges and less precision
## There are other number types - they are variations on float and integer
xx = 1
type(xx)
temp = 98.6
type(temp)   ## 'float'
type(1.0)   ## float
## Type Conversions
## When you put an integer and floating point in an expression, the integer is implicitly coerced to a float
print(float(99) + 100)  ## output is 199.0
i = 42
type(i)
f = float(i)
print(f)
type(f)  ## float
## You can control this with the built-in functions int() and float()
## Integer division produces a floating point result
print(10 / 2)  ## output is 5.0
print(9 / 2)
print(10.0 / 2.0)   ##  still float 5.0 

## String conversions
## You can use int() and float() to convert between strings and integers
## You will get an error if the string does not contain numeric characters
sval = ='123'
type(sval)  ## give output: str
print(sval + 1)  ## give error, bc string can not add with integer
ival = int(sval)
type(ival)  ## gives class int
print(ival + 1)
nsv = 'hello bob'
niv = int(nsv)  ## This will give error because nsv does not contain number

## Take numbers from outside world
## User Imput
## We can instruct Python to pause and read data from the user using the input() function
## The input() function always returns a string
nam = input('Who are you?')
print('Welcome', nam)  ## Unlike plus sign between welcome and nam, the comma will create a space between welcome and nam


## Expression - Part 3
## Comments in Python 
## Anything after a # is ignored by Python
## Why comment?  
## Describe what is going to happen in a sequence of code
## Document who wrote the code or other ancillary information
## Turn off a line of code - perhaps temporarily

## Converting User Input
## If we want to read a number from the user, we must convert it from a string to a number using a type conversion function, later we will deal with bad data inout
## Convert elevator floors
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)
         
## Chapter 2 Exercise 2
nam = input('Enter your name:')
print('Hello', nam)
## Chapter 2 Exercise 3
hours = input('Enter Hours:')
rate = input('Enter Rate:')
hours = float(hours)
rate = float(rate)
pay = hours*rate
pay = float(hours) * float(rate)
print('Pay:', pay)
print('Pay: '+str(pay))
## Chapter 2 Exercise 4
width = 17
height = 12.0
width / 2
width / 2.0
height/3
## %reset quit() clear() exit
tempCel = input('Enter Celsius temperature: ')
tempFar = (float(tempCel) * 5/9) + 32
print(f'{tempCel}C = {tempFar:<.0f}F')




## Chapter 3      
## Conditional Execution

## 3.1 Conditional Statements
## Conditional Steps
x = 5
if x < 10:   ## Evaluate and returns True/False, if true, execute, otherwise, skip
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

## Comparison Operators (Evaluate)
## 1. Boolean expressions ask a question and produce a Yes or No result which we use to control program flow
## 2. Boolean expressions using comparison operators evalaute to True/False or Yes/No
## 3. Comparison operators look at variables but do not chnage the variables
<    ## Less than 
<=   ## Less than or equal to
==   ## Equal to
>=   ## Greater than or Equal to
>   ## Greater than 
!=   ## Not Equal
## Remember: "=" is used for assignment   

## Example, all returns
x = 5
if x == 5 :
    print('Equals 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equal 5')
if x < 6 : print('Less than 6')
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')
         
## One-Way Decision, indention is very important, it produces a block to execute
x = 5
print('Before 5')
if x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')
## Output:
# Before 5
# Is 5
# Is Still 5
# Third 5
# Afterwards 5
# Before 6
# Afterwards 6
## End of block, we reduce the indent back or de-indent to end a block
         
## Increase/maintain after if or for, decrease to indicate end of block
x = 5
if x > 2 :
    print('Bigger than 2')  ## Conditional Code
    print('Still bigger')   ## Conditional Code
print('Done with 2')    ## Sequential Code

for i in range(5) :   ## range(5) == rang(0, 5)  is 0, 1, 2, 3, 4
    print(i)
    if i > 2 :  ## Nested
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')
        
## Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')
         
## Two-Way Decisions
## Sometimes we want to do one thing if a logical expression is true and something else if the expression is false
## It is like a fork in the road, we must choose one or the other path but not both
## Example
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')
         
## Multi-Way: key thing is it's only gonna to do one , only one is triggered
x = 1
if x < 2 :
    print('Small') 
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All done')

## Multi-Way No Else: the if and elif might not execute for both
x = 5
if x < 2 :
    print('Samll')
elif x < 10 :
    print('Medium')
print('All done')

## Multi-Way, Multiple elif
if x < 2:
    print('Samll')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 40 :
    print('Large')
elif x < 100 :
    print('Huge')
else :
    print('Ginormous')
            
## Things happen in order in conditional statement, which will never execute regardless of the value of x
if x < 2 :
    print('Below 2')
elif x >= 2 :
    print('Two or more')
else :
print('Something else')   ## The else statement will never be executed
       
## The try/except Structure, eliminate catch traceback
## You surround a dangerous section of code with try and except
## If the code in the try works - the except is skipped
## If the code in the try fails - it jumps to the except sections         
## Example
astr = 'Hello Bob'
istr = int(astr)   ## this will cause program stop as it is wrong
print('First', istr)
astr = '123'
istr = int(astr)         
print('Second', istr)         
## Try/Except, take out and insurance
astr = 'Hello Bob'
try:
    istr = int(astr)     ## dangerous code
    ## When the first conversion fails - it just drops into the except: clause and the program contimues
except :     ## except is like else, Python will execute this line if something goes wrong
    istr = -1
print('First', istr)             

astr = '123'
try :
    istr = int(astr)
## When the second conversion succeeds - -it just skips the except: clause and the program continues.
except :
    istr = -1
print('Second', istr)         
         
## Try/except a block of code
astr = 'Bob'
try :
    print('Hello')  ## execute
    istr = int(astr)  ## code blow up here
    print('There')    ## This will not be execute
except :
    istr = -1
print('Done', istr)         
         
# Sample try/except, does not work for negative numbers
rawstr = input('Enter a number:')
try :
    ival = int(rawstr)
except :
    ival = -1
if ival > 0 :
    print('Nice work')
else :
    print('Not a number')
        
## Exercise 3.1
hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
if hours > 40 :
    pay = (hours-40)*1.5*rate+40*rate
elif 0<= hours <=40 :
    pay = hours*rate
else :
    print('The hours or rate input is not right')
print('Pay:', pay)
   
## Exercise 3.2
hours = input('Enter Hours:')
try :
    hours = float(hours) 
except :
    print('Error, please enter numeric input')
rate = input('Enter Rate:')
try :
    rate = float(rate)    
except :
    print('Error, please enter numeric input')

## Chapter 4: Functions
## Using functions - store and reuse                  ## four uses: sequential, conditional, iterations and store and reuse
## Stored (and reused) Steps
def thing():    ## keyword: def: start the definition of a function, define the function. Function name is thing and in the parentheses we should have parameters
    print('Hello')
    print('Fun')   ## Python remember this but will not execute
thing()   ## calling and invoking the function
print('Zip')
thing()

## Max/Min function
big = max('Hello World')
print(big)   ## remember, smaller letter is larger than big letter
## Output is r
tiny = min('Hello World')
print(tiny)
## output is the 'space' because space is the minimum
def max(inp):       ## put in a string 'Hello World'
    blah
    blah
    for x in inp:
        blah
        blah         ## output returns a string 'r'
## A function is some stored code that we call. A function tales some input and produces an output.

## Type Conversions
## When you put an integer and floating point in an expression, the integer is implicitly converted to a float
print float(99) / 100   ## output 0.99
i = 42
type(i)   ## class 'int'
f = float(i)
print(f)    ## 42.0
type(f)   ## class 'float'
print(1 + 2 * float(3) / 4 - 5)       ## output -2.5
## You can control this with the built-in functions int() and float()

## String Conversions
## You can also use int() and float() to convert between strings and integers
sval = '123'
type(sval)    ## class str
print(sval + 1)  ## error message
ival = int(sval)
type(ival)   ## class int
print(ival + 1)   ##  124
nsv = 'hello bob'
niv = int(nsv)   ## error message
## input() function will always return a string
## You will get an error if string does not contain numeric characters

def draw(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('*', end='')
        print('\r')
draw(5)
pyramid_num = input("Please enter a number: ")
n = int(pyramid_num)
i = 1
while i < n+1:
    print(" "*(n-i)+"*"*(2*i-1))
    i = i + 1

## Building our own Functions
## We create a new function using the def keyword followed by optional parameters in parentheses
## We indent the body of the function
## This defines the function but does not execute the body of the function
def print_lyrics():
    print("I am the lumberjackgotcha, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
x=2
x = x + 2
print(x)
print_lyrics()

## Arguments
## An argument is a value we pass into the funtion as its input when we call the function
## We use arguments so we can direct the function to do different kinds of work when we call it at different times
## We put the arguments in parentheses after the name of the function
## eg:
big = max('Hello World')
    
## Parameters -- Arguments
## A parameter is a variable which we use in the function definition. It is a 'handle' that allows the code in the function to access the arguments for a particular function invocation.
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')   ## Hello
greet('es')    ## Hola
greet('fr')   ## Bonjour

## Return Values
## Often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression.
## The return keyword is used for this
def greet():
    return 'Hello'     
print(greet(), 'Glenn')
print(greet(), 'Sally')    
## Return does two things: stop the function and return the value we want
        
## 1. A 'fruitful' function is one that produces a result(or return value)
## 2. The return statement ends the function execution and 'sends back' the result of the function
def greet(lang):
    if lang == 'es':
        return 'Hola'
    if lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'), 'Glenn')  ## Hello Glenn
print(greet('es'), 'Sally')  ## Hola Sally
print(greet('fr'), 'Michael')  ##Bonjour Michael
    
## Multiple Parameters /Arguments
## We can define more than one parameter in the function definition
## We simply add more arguments when we call the function
## We match the number and order of arguments and parameters
def addtwo(a, b):
    added = a + b
    return added     ## added is the local variable
x = addtwo(3, 5)
print(x)

def stuff():
    print('Hello')
    return
    print('World')
    
stuff()

## Chapter 5. Loops and Iterations
## Repeated Steps
n = 5
while n > 0 :  ## Indefinite loops
    print(n)
    n = n - 1    ## iteration variable to control the iteration stop
print('Blastoff')
print(n)
#5
#4
#3
#2
#1
#Blastoff
#0
## Loops (repeated steps) have iteration variables that change each time through a loop. Often these iteration variables go through a sequence of numbers.

## An Infinite Loop
n = 5
while n > 0 :
    print('Lather')
    print('Rinse')    ## Do not run, it will never stop
print('Dry off!')  ## never show this output

## Another Loop
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')    ## run, it never execute
print('Dry off!')

## Statements to get out of a Loop
## Breaking Out of a Loop
## The break statement ends the current loop and jumps to the statement immediately following the loop
## It is like a loop test that can happen anywhere in the body of the loop
while True :  ## Never False, infinite Loops
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

#> hello there
#hello there
#
#> finished
#finished
#
#> done
#Done!

## Quit an Interation with Continue
## The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')
#> hello there
#hello there
#
#> # don't print this
#
#> print this!
#print this!
#
#> done
#Done      


## break skip out of the loop and continue skips to the top of the loop

## Definite Loops
## A Simple Definite Loop Example
for i in [5, 4, 3, 2, 1]:   ## for is key word, i is iteration variable in five-element sequence
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :    ## iteration variable friend
    print('Happy New Year', friend)
print('Done!')


friends = ['Joseph', 'Glenn', 'Sally']
for i in friends :
    print('Happy New Year', i)
print('Done!')
## Definite loops (for loops) have explicit iteration variables that hcnage each time through a loop.
## These iteration variables move throigh the sequence or set.

## In
## The iteration variable 'iterates' through the sequence (ordered set)
## The block(body) of code is executed once for each value in the sequence
## The iteration variable moves through all of the values in the sequence

## Making Smart Loops
## The trick is 'knowing' something about the whole loop when you are stuck writing code that only sees one entry at a time
## Step 1. Set some variables to initial values
## for thing in data, step 2: Look for something or do something to each entry separately, updating a variable
## Step 3. Look at the variables

## Loopong through a set
list_study = [9, 41, 12, 3, 74, 15]
print('Before')
for thing in list_study :
    print(thing)
print('After')

## What is the largest Number  
largest_so_far = -1
print('Before', largest_so_far)
for the_num in list_study :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
## do something before loop, do stuff during the loop and payoff is after the loop
## We make a variable that contains the largest value we have seen so far. 
## If the current number we are looking at is larger, it is the new largest value we have seen so far.

## Loop Idioms
## Counting in a Loop
zork = 0
print('Before', zork)
for thing in list_study :
    zork = zork + 1
    print(zork, thing)
print('After', zork)
## To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop.

## Summing in a Loop
zork = 0
print('Before', zork)
for thing in list_study:
    zork = zork+thing
    print(zork, thing)
print('After', zork)
## To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop.

## Finding the Average in a Loop
count = 0
total = 0
print('Before', count, total)
for thing in list_study:
    total = total + thing
    count = count + 1
    print(count, total, thing)
print('After', count, total, total/count)
## An mean/average just combines the counting and sum patterns and divides when the loop is done

## Filtering in a Loop
print('Before')
for value in list_study:
    if value > 20:
        print('Large number', value)
print('After')
## We use an if statment in the loop to catch / filter the values we are looking for.

## Searching Using a Boolean Variable
found = False
print('Before', found)
for value in list_study:
    if value == 3:
        found = True   ## found will have 'True' value since it found '3'
        ## maybe we can use break here
    print(found, value)
print('After', found)
## If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.

## None Type: means the absence of a value, has only one thing, none.
## None is a variable, a value, that we can distinctly detect different than numbers
smallest = None
print('Before')
for value in list_study:
    if smallest == None:   ## or we can use 'if smallest is None', first time is True and other times are all False
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
## We still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest.
    
## The 'is' and 'is not' Operators
## Python has an 'is' operator that can be used in logical expressions
## 'is' implies 'is the same as'
## Similar to, but strong than '=='
## 'is not' also is a logical operator

## Exercise for Chapter 5
## Exercise 5.1
total = 0
count = 0
while True:
     put=input('Enter a number: ')
     if put == 'done':
         break
     else:
         try:
             num_put=float(put)
         except:
             print('Invalid input')
             continue
     count = count+1
     total = total+num_put
print(total, count, total/count)    




## Letter Usage
mystring = input("Please enter a string: ")
mynewstring = mystring
index = 0
for letter in mystring:
    if index % 2 == 0:
        if index == 0:
            mynewstring = mynewstring[:1].lower()+mystring[1:]
        else:
            mynewstring = mynewstring[:index] + mynewstring[index:index+1].lower() + mystring[index+1:]
    else:
        mynewstring = mynewstring[:index] + mynewstring[index:index+1].upper() + mystring[index+1:]
    index = index + 1    
print(mynewstring)

mystring = input("Please enter a string: ")
mynewstring = mystring
index = 0
for letter in mystring:
    if index % 2 == 0:
        if index == 0:
            mynewstring = letter.lower() + mystring[1:]
        else:
            mynewstring = mynewstring[:index] + letter.lower() + mystring[index+1:]
    else:
        mynewstring = mynewstring[:index] + letter.upper() + mystring[index+1:]
    index = index + 1    
print(mynewstring)





## String Format
if scoreVal < 0 or scoreVal > 1:
    raise ValueError('Value is not in range 0 to 1.0')
try:
    blahblahblah
except (valueError, TypeError) as e:
    print(f'Bad Score ({e})')












