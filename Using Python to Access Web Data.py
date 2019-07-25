# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:17:00 2019

@author: D17911
"""
from os import chdir, getcwd
getcwd()  #'C:\\Users\\D17911'
chdir('\\\\WIL-HOMEDRIVE01\D17911$\Desktop\Courses\Python for Data Science\Week 1')
getcwd()   ## '\\\\WIL-HOMEDRIVE01\\D17911$\\Desktop\\Courses\\Python for Data Science\\Week 1'
## Using Python to Access Web Data

## Chapter 11 - Regular Expressions 
## In computing, a regular expression, also referred to as 'regex' or 'regexp', provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters.
## A regular expression is written in a formal language that can be interpreted by a regular expression processor.
## Really clever wild card expressions for matching and parsing strings

## Understanding Regular Expressions
## 1. Very powerful and quite cryptic
## 2. Fun once you understand them
## 3. Regular expressions are a language unto themselves
## 4. A language of 'marker characters' - programming with characters
## 5. It is kind of an 'old school' langugae - compact

## Regular Expression Quick Guide
^   ## Matches the beginning of a line
$   ## Matches the end of a line
.   ### Matches any character
\s  ## Matches whitespace
\S  ## Matches any non-whitespace character
*   ## Repeats a character zero or more times
*?  ## Repeats a character zero or more times (non-greedy)
+   ## Repeats a character one or more times
+?  ## Repeats a character one or more times(non-greedy)
[aeiou]      ## Matches a single character in the listed set
[^XYZ]       ## Matches a single character not in the listed set
[a-z0-9]     ## The set of characters can include a range
(            ## Indicates where string extraction is to start
)            ## Indicates where string extraction is to end

## The Regular Expression Module
## Before you can use regular expressions in your program, you must import the library using 'import re'.
## You can use re.search() -- give yes or no answer -- to see if a string matches a regular expression, similar to using the find() method for strings
## You can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]

## Using re.search() Like find()
str.find()   ## If substring exists inside the string, it returns the idnex of first occurence of the substring; If does not exist, return -1
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0 :
        print(line)

## Using regular expression, the same as above
import re
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('From:', line):   ## This returns True or False
        print(line)

## Using re.search() Like startswith(), start with string
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:')  :
        print(line)
## We fine-tune what is matched by adding special characters to the string
import re
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip
    if re.search('^From:', line):   ## Tweek matching strings, ^ beginning of the line
        print(line)

## Wild-Card Characters
## The dot character matches any character
## If you add the asterisk character, the character is 'any number of times', zero or more time
^X.*:          ## Looking for lines that has 'X' at the beginning, followed by any number of characters, followed by a ":"
^ and .* are special characters
^ ## Match the start of the line
.  ## Match any character
*   ## Many times
Outputs:
X-Sieve: CMU Sieve 2.3
X-DSPAM-Result: Innocent
X-DSPAM-Confidence: 0.8475
X-Content-Type-Message-Body: text/plain
X-Plane is behind schedule: two weeks

## Now we do not want to have 'X-Plane is behind schedule: two weeks' because of space in strings
## Fine-Tuning Your Match
## Depending on how 'clean' your data is and the purpose of your application, you may want to narrow your match down a bit
X-Sieve: CMU Sieve 2.3
X-DSPAM-Result: Innocent
## We use:
^X-\S+:
^  ## Match the start of the line of 'X-'
\S  ## Match any non-whitespace character
+  ## One or more times  >= 1

## Matching and Extracting Data(Not True or False)
## re.search() returns a True/False depending on whether the string matches the regular expression
## If we actually want the matching strings to be extracted, we use re.findall()
[0-9]+  ## One or more digits, [0-9] means any single digit between 0 to 9, + means one or more digits
[0-9.]+  ## One or more digits and period, [0-9] means any single digit between 0 to 9, + means one or more digits
import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)  ## It gives back a list, it is like a split in a for loop
print(y)    ## ['2', '19', '42']   it is a list of strings, if nothing it will give us a blank list
y = re.findall('[AEIOU]+', x)   ## Find one or more than one uppercase vowels, answer: []

## Warning: Greedy Matching
## The repeat characters (* and +) push outward in both directions(greedy) to match the largest possible string
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)    ##  ['From: Using the :']
^F.+:    ## First character in the match is an F, Last character in the match is a :, .+ means one or more characters
## Why not output 'From:', greedy matching will give the larger thing, '.+' is pushing as large as possible and then still match the entire expression
y = re.findall('^F\S+:', x)
print(y)   ## ['From:']

## Non-Greedy Matching: prefer the shortest
## Not all regular expression repeat codes are greedy!
## If you add a '?' character, the + and * chill out a bit
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)   ## ['From:']
^F.+?:   ## ^F first character in the match is an F, '.+?' one or more characters but not greedy,  ':' last character in the match in a :
    
## Fine-Tuning String Extraction
## You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)    ##  ['stephen.marquard@uct.ac.za']
\S+@\S+   ## At least one non-whitespace character:    \S@\S will have d@u outcome
y = re.findall('\S@\S+?', x)
print(y)   ## ['d@u']   Non-Greedy
y = re.findall('\S+?@\S+', x)
print(y)    ## ['stephen.marquard@uct.ac.za']

## Parentheses are not part of the match - but they tell where to start and stop what string to extract
y = re.findall('^From (\S+@\S+)', x)
print(y)   ##  ['stephen.marquard@uct.ac.za']
^From (\S+@\S+)   ## ( means start extracting after the space, require that find starts of From and extracting strings I want
y = re.findall('^From \S+@\S+', x)
print(y)   ##  ['From stephen.marquard@uct.ac.za']

## Old ways of Extracting a host name - using find and string slicing and position index
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)  #21
sppos = data.find(' ', atpos)
print(sppos)  #31
host = data[atpos+1 : sppos]
print(host)   ## uct.ac.za
## The Double Split Pattern
## Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again
words = data.split()
email = words[1]
pieces = words.split('@')
print(pieces[1])   ## uct.ac.za
##  The Regex Version
import re
y = re.findall('@([^ ]*)', data)
print(y)   ## ['uct.ac.za']
y = re.findall('@(\S*)', data)
print(y)   ## ['uct.ac.za']
'@([^ ]*)'   ## @ starts with @, () extract beginning and end, [^ ] Match non-blank character, * Match many of them
[^ ]    ## ^ means Not Everything but -- not everything but space, which means non-blank, similar \S

## Even Cooler Regex Version, pick lines and extract data
import re
y = re.findall('^From .*@([^ ]*)', data)    ## Not only extract the string but also the line filtering
print(y)   ##  ['uct.ac.za']
'^From .*@([^ ]*)'
## Starting at the beginning of the line, looking for the string 'From '
## Pick Lines and Extracting Data
## Spam Confidence
import re
handle = open('mbox-short.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))   ##  Maximum: 0.9907

## Match special(real) characters: A dollar sign, an asterisk, bracket, plus or a dot
## Escape Character
## If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)   ##  ['$10.00']
\$[0-9.]+    ## \$ means A real dollar sign   [0-9.]  means A digit or period    + means At least one or more
## $ has meaning of regular expressionand \$ means just a dollar sign

x = 'From a9 a 9  $ @'
y = re.findall('[a-z0-9]', x)
print(y)

## Chapter 12
## Networked Technology, Network Architecture
## Communications between two applications, computer program and server(PHP, java)
## TCP Connections/Sockets
## 'In computer networking, an Internet socket or network socket is an endpoint of a bidirectional inter-process comunication flow across an Internet Protocol-based computer network, such as the Internet'
## TCP Port Numbers
## A port is an application-specific or process-specific software communications endpoint
## It allows multiple networked applications to coexist on the same server
## There is a list of well-known TCP port numbers (like the extension phone numbers)

## We play with the Web Server which is port 80, port 443 is the secure HTTPS
## Common TCP Ports
## Telnet(23) - lOGIN  IMAP(143/220/993) - Mail
## SSH(22) - Secure     POP(109/110) - Mail Retrieval
## HTTP(80)   DNS(53) - Domain Name
## SMTP(25)(Mail)   FTP(21) - File Transfer

## Sockets in Python 
## Python has built-in support for TCP Sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   ## ready to connect to the far end, but not connected yet
## mysock is an object 
mysock.connect(('data.pr4e.org', 80))   
('data.pr4e.org', 80)  ## (Host -- Domain Name, Port)     
## Above is dialing the phone, make connection
     
## Communicate far off application in Python 
## Hypertext Transfer Protocol(HTTP)   
## Application Protocal: The socket have made us from transport layer to application layer 
## Since TCP( and Python) gives us a reliable socket, what do we want to do with the socket? What problem do we want to solve?
## Application Protocols  (Mail, World Wide Web)
## There are different rules of talking to different applications (Mail, World Wide Web)
     
# HTTP - Hypertext Transfer Protocol
## The dominant Application Layer Protocol on the Internet
## Invented for the Web -  to Retrieve HTML, Images, Documents, etc
## Extended to be data in addition to documents - RSS, Web Services, etc.. Basic Concept - Make a Connection - Request a Document - Retrieve the Document - Close the Connection
## HTTP: is the set of rules to allow browsers to retieve web documents from servers over the Internet
## One of the things about HTTP protocol is look at the Uniform Resource Locator (URL):
http://www.dr-chuck.com/page1.htm     
http://   ## use the HTTP Protocol
www.dr-chuck.com   ## host name
/page1.htm    ## get the document     

## Getting Data From the Server : Get the document, retrieve it, parse it and display for you on the browser
## Each the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection to the web server and issues a 'GET' request - to GET the content of the page at the specific URL
## The server returns the HTML(Hypertext Markup Language) document to the browser which formats and displays the document to the user

## Internect Standards (Build the protocols)     
## The standards for all of the internet protocols(inner workings) are developed by an organization
## Internet Engineering Task Forse(IETF)
www.ietf.org
## Standards are called ;RCFs' - 'Request for Comments'

## Making an HTTP request
## Connect to the server like www.dr-chuck.com
## Request a document (or the default document)
- GET http://www.dr-chuck.com/page 1.htm HTTP/1.0   ## GET URL protocol
- GET http://www.mlive/com/ann-arbor/ HTTP/1.0
- GET http://www.facebook.com HTTP/1.0

## Install Telnet on Windows which can connect to any server
$ telnet data.pr4e.org 80
##  Connecting here....
GET http://www.dr-chuck.com/page 1.htm HTTP/1.0  
## Press Enter
## Then it will give the information and outputs of this page    
## Outputs: headers (blank line) contents
HTTP/1.1 200 OK
Date: Thu, 08 Jan 2015 01:57:52 GMT
Last-Modified: Sun, 19 Jan 2014 14:25:43 GMT
Connection: close
Content-Type: text/html

<h1>The First Page</h1>
<p>If you like, you can switch to
the <a href="http://data.pr4e.org/page2.htm">Second Page</a>.</p>
Connection closed by foreign host  ## not text, shows connection close

## An HTTP Request in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   ## ready to connect to the far end, but not connected yet
## mysock is an object 
mysock.connect(('data.pr4e.org', 80))   ## two parentheses
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()   ## call method, prepare for sending
## two new line r\n\r\n: means enter enter, is what I did when we are in Telnet
mysock.send(cmd)  ## send the staff to the server

while True:   ## The output of while loop is the METADATA
    data = mysock.recv(512)    ## receive up to 512 characters
    if (len(data) < 1):
        break    ## ends the loop until go to the file final
    print(data.decode())   ## decode means take the data outside work and interpret what it means internally for us
mysock.close()  ## close the socket
     
## In program, socket has four functions: socket, conect, send, recv   
## socket: doorway get out of your computer
## connects: extends out of your computer and could fail if server does not exist
## send: send the data first to the server, might need several sends to print stuff out
## recv: receive is a method in the socket object 

## Worked Example: Sockets
## if you have problem with '\r\n\r\n', you can change to '\n\n'

## Do the things in telnet
## Hack the html of this link: http://data.pr4e.org/romeo.txt
telnet data.pr4e.org 80  ## Enter
http://data.pr4e.org/romeo.txt ## hit Enter Twice
## go to this link ib browser and use developer: Javascript Console, we will see the header and document body

## Do the thing in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
mysock.connect(('data.pr4e.org', 80))   ## a tuple in the parentheses
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
## Strings inside Python which is UNICODE, so we have to send them out in UTF-8 format
## encode() converts from unicode internally to UTF-8
mysock.send(cmd) 

while True:   ## The output of while loop is the METADATA
    data = mysock.recv(512)    ## receive up to 512 characters
    if (len(data) < 1):
        break    ## ends the loop until go to the file final
    print(data.decode())   ## decode means take the data outside work and interpret what it means internally for us
    ## decode() is the opposite of encode, converts UTF-8 to unicode
mysock.close() 


## Using the Developer Console to Explore HTTP
## Open this website : http://data.pr4e.org/page1.htm
## Use the developer tools adn look at the 'Network'- Headers, Preview, Response, Timing
## Below is the contents for 'Web Applications'
https://www.wa4e.com/code/arrays/guess.php
## add parameters
https://www.wa4e.com/code/arrays/guess.php?guess=12
## these parameters that go on in addition to the URL, called get parameters or query string parameters, we can add more at the end
https://www.wa4e.com/code/arrays/guess.php?guess=12&x=14&abc=22   ## in the Query String Parameters we will get 3 strings
## Status Code can be changed
## Try a bad URL:
https://www.wa4e.com/zap
### Status Code changed to 404
## Explore another Status Code
https://www.wa4e.com/code/route/redir1.php
## Status Code is 302 means send other thing back to server and redirect to this other page. Now is the wrong page and will direct to right page
## The response of Content-Type can be image/jpeg or text/html, text/plain

## Programs that Surf the Web
## Unicode Characters and Strings
## ASCII Maps: American Standard Code for Information Interchange
## Example: From 0 to 128, which means you can not put every character into a 0 through 127
New line: LF number 10 Bin: 0001010
Letter: H number 72 Bin: 1001000
Letter: e number 101 Bin: 1100101

## Representing Simple Strings
## Each character is represented by a number between 0 and 256 stored in 8 bits of memory
## We refer to '8 bits of memory as one 'byte' of memory - (i.e. my disk drive contains 3 Terabytes of memory)
## The ord() function tells us the numeric value(real number) of a simple ASCII character
ord() ## ordinal()
print(ord('H'))   ## 72
print(ord('e'))   ## 101
print(ord('\n'))  ## 10
'Hi' < 'aaa'   ## True


## Unicode Characters and Strings
## Unicode --  Universal Code used for thousands of characters for computers to exchange data from different places
## Multi-Byte Characters
## To represent the wide range of characters computers must handle we represent characters with more than one byte
### UTF-16 -- Fixed Length - Two bytes
### UTF-32 -- Fixed Length - Four Bytes
### UFT-8 -- 1~4 Bytes
#### Upwards compatible with ASCII
#### Automatic detection between ASCII and UTF-8
#### UTF-8 is recommended practice for encoding data to be exchanged between systems

## In Python edition 2, there are two kinds of strings: str and unicode
## In Python 3, all strings are Unicode
Python 2.7.10
x = '编程'  ## regular string
type(x)   ## <type 'str'>
x = u'编程'   ## unicode string
type(x)  ## <type 'unicode'>

Python 3.5.1
x = '编程'
type(x)   ## <class 'str'>
x = u'编程'
type(x)   ## <class 'str'>

Python 2.7.10  ## Byte String is the same with Regular String and they are different from Unicode String
x = b'abc'
type(x)  ## <type 'str'>
x = '编程'  ## regular string
type(x)   ## <type 'str'>
x = u'编程'   ## unicode string
type(x)  ## <type 'unicode'>

Python 3.5.1 ## Byte String is different from Regular String and Regular String is the same with Unicode String
x = b'abc'
type(x)   ## <class 'bytes'>
x = '编程'
type(x)   ## <class 'str'>
x = u'编程'
type(x)   ## <class 'str'>

## Python 3 and Unicode
## In Python 3, all strings internally are UNICODE
## Working with string variables in Python programs and reading from files usually 'just works'
## When we talk to a network resource using sockets to talk to a database we have to encode(send) and decode(receive) data(usually to UTF-8)

## When we talk to an external resource like a network socket we send bytes, so we need to encode Python 3 strings into a given character encoding
## WWhen We read data from an external resource, we must decode it based on the character set so it is properly represented in Python 3 as a string
while True:   ## The output of while loop is the METADATA
    data = mysock.recv(512)    ## receive up to 512 characters, data is Bytes
    if (len(data) < 1):
        break    ## ends the loop until go to the file final
    mystring = data.decode()   ## decode means take the data outside work and interpret what it means internally for us
    print(mystring)   ## mystring is Unicode, decode() converts bytes(UTF-8 or ASCII) to Unicode 
    ## decode() is the opposite of encode, converts UTF-8 to unicode
bytes.decode()
str.encode()

## Retrieving Web Pages
## Using urllib in Python
## Since HTTP is so common, we have a library that does all the socket work for us and mkaes web pages look like a file
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())  ## line is the byte array and decode it 

## urllib treats things like a file
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count=dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)

## Reading Web Pages, not only yexy/plain file but also html file
## If you want to review the header, you need to ask for it in urllib by a different way
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
## HTML is ugly and does not work well with regular expressions

## Worked Example: Using Urllib --  Web Crawler @ Google
## Example 1
import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
## Example 2
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().rstrip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

## Parsing Web Pages (Web Scraping, HTML does not work well)
## What is Web Scraping?
## When a program or script pretends to be a browser and retrieves web pages(browser talk to servers),
## looks at those web pages, extracts information, and then looks at more web pages
## Search engines scrape web pages - we call this 'spidering the web' or 'web crawling'
 
## Why Scrape?
## Pull data - particularly social data - who links to who
## Get your own data back out of some system that has no 'export capability'
## Monitor a site for new information
## Spider the web to make a database for a search engine
## There is some controversy about web page scraping and some sites are a bit snippy about it
## Republishing copyrighted information is not allowed
## Violating terms of service is not allowed

## Parsing HTML -- The Easy Way - Beautiful Soup
## You could do string searches the hard way
## Or use the free software library called BeautifulSoup from www.crummy.com

## BeautifulSoup Installation
## Method 1: personal Computer
## To run this, you can install BeautifulSoup
## https://pypi.python.org/pypi/beautifulsoup4
## Method 2: Company Computer
## Or download the file
## http://www.py4e.com/code/bs4.zip
## and unzip it in the same directory as this file   
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
html = urllib.request.urlopen(url)  ## this is a for loop returns line by line
url = input('Enter - ')    ## Enter - http://www.dr-chuck.com/page1.htm   http://www.dr-chuck.com/page2.htm
html = urllib.request.urlopen(url).read() ## read()  reads the whole blob with newlines at the end and comes in to one big string
soup = BeautifulSoup(html, 'html.parser')  ## parse the whole string of HTML, and get back with an object 
## Retrieve all of the anchor tags
tags = soup('a')   ## ask Soup to give me a list of anchor tags 
##[<a href="http://www.dr-chuck.com/page2.htm">
## Second Page</a>]
for tag in tags:
    print(tag.get('href', None))  ## tags is a list and tag is a dictionary, get the href key

## Worked Example of BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

## Ignore SSL certificate errors, for the HTTPS application
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')  ## http://www.dr-chuck.com http://www.dr-chuck.com/page1.htm  https://www.si.umich.edu/
html = urllib.request.urlopen(url, context=ctx).read()  ## For loop of lines -- a whole string with newlines -- UTF-8 string
soup = BeautifulSoup(html, 'html.parser')  ## clean soup object
## Retrieve all of the anchor tags, <a through /a>
tags = soup('a')   ## list of anchor tags
for tag in tags:
    print(tag.get('href', None))

## Exercise 4
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup 
import ssl 

ctx = ssl.create_default_context() 
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE 

url = input('Enter the URL and I will count the paragraphs: ') 
html = urllib.request.urlopen(url, context=ctx).read() 
soup = BeautifulSoup(html, 'html.parser') 
count = 0                                
tags = soup('p') 
for tag in tags:    
    count += 1 
print("The Number of Paragraphs on:", url, "is", count) 







## Chapter 13 Web Services and XML
## Data on the Web
## Retrieve and parse XML(eXtensible Markup Language) data
## With the HTTP Request/Response well understood and well supported, there was a natural move towards exchanging data between programs using these protocols
## We needed to come up with an agreed way to represent data going between applications and across networks
## There are two commonly used formats: XML and JSON

## Sending Data across the 'Net'
## Two programs sending and receiving data(Python Dictionary and Java HashMap) communicate through Network
## a.k.a. 'Wire Protocol' - What we send on the 'wire'
## Step 1: Python producing the data(reading a database or a file), and then has a Python structured dictionary
## Step 2: Send that across the network,
## Step 3: Wire Protocol: How the data is put on the wire, how the data leaves one system, transits a network, and then enters another system
## Step 4: Destination System: Another program(Java HashMap)

## Agreeing on a 'Wire Format'
## XML is one of the wire formats
## Python Dictionary(internal data) 'Serialize' to a wire format and then 'De-Serialize'(taking data off the wire) to a new internal data structure
## Two types of serialization formats are XML and JSON

## Take Python Dictionary and we produce JSON and send JSON across the network as a string or document and turn into other programs
## XML: Marking up data to send across the network...

## XML "Elements' (or Nodes)
<people>  ## Complex Element, start
  <person>  ## Complex Element, start
    <name>Chuck</name>  ## Simple Element
    <phone>303 4456</phone>  ## Simple Element, start and end tag
  </person>  ## Complex Element, end
  <person>  ## Complex Element, start
    <name>Noah</name>  ## Simple Elements
    <phone>622 7421</phone>  ## Simple Elements
  </person>  ## Complex Element, end
</people>  ## Complex Element, end

## eXtensible Markup Language
## Primary purpose is to help information systems share structured data
## It started as a simplified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible
## XML Basics: Start Tag, End Tag, Text Content, Attribute, Self Closing Tag
<person>  ## Start Tag
 <name>Chuck</name>  ## Chuck is Text Content, </name> is End tag    
 <phone type="intl"> ## type="intl" is the Attribute
  +1 734 303 4456
 </phone>
 <email hide="yes" />  ## <email /> is Self Closing Tag
</person>
## White Space
## Line ends do not matter. White space is generally discarded on text elements. Except for the white space in the text content
## We indent only to be readable.
## Tags: indicate the beginning and ending of elements
## Attributes: - Keyword/value pairs on the opening tag of XML
## Serialize / De-Serialize - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner
## XML as a Tree (Text Node): Attributes child and Text child under a Node
## XML as Path:  /a/b  text: X  /a/c/d  text: Y  /a/c/e   text: Z

## XML Schema: Describing a 'contract' as to what is acceptable XML
## XML Schema(when data blow up in either of two sides, use XML Schema to decide)
## XML Schema
## Description of the legal format of an XML document
## Expressed in terms of constraints on the structure and content of documents
## Often used to specify a 'contract' between systems - 'My system will only accept XML that conforms to this particular Schema.'
## If a particular piece of XML meets the specification of the Schema - it is said to 'validate'

## XML Validation
## XML validation is the act of taking an document and a Schema Contract(also a XML document), send to validator
## Example
XML Document
<person>
 <lastname>Severance</lastname>
 <age>17</age>
 <dateborn>2001-04-17</dateborn>
</person>
XML Schema Contract
<xs:complexType name="person">
 <xs:sequence>
  <xs:element name="lastname" type="xs:string"/>
  <xs:element name="age" type="xs:integer"/>
  <xs:element name="dateborn" type="xs:date"/>
 </xs:sequence>
</xs:complexType>

## Many XML Schema Languages
## 1. Document Type Definition (DTD)
## 2. Standard Generalized Markup Language (ISO 8879:1986 SGML)
## 3. XML Schema from W3C(World Wide Web Consortium) - (XSD)
## XSD XML Schema (W3C spec)
## We will focus on the World Wide Web Consortium (W3C) version
## It is often called 'W3C Schema' because 'Schema' is considered generic
## More commonly it is called XSD because the file names end in .xsd
XSD Structure: xs:element xs:sequence xs:complexType
<person>
 <lastname>Severance</lastname>
 <age>17</age>
 <dateborn>2001-04-17</dateborn>
</person>
XML Schema Contract
<xs:complexType name="person">
 <xs:sequence>
  <xs:element name="lastname" type="xs:string"/>
  <xs:element name="age" type="xs:integer"/>
  <xs:element name="dateborn" type="xs:date"/>
 </xs:sequence>
</xs:complexType>

## XSD Constraints
<xs: element name="person">
 <xs: complexType>
  <xs:sequence>
   <xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1" />  ## Exactly only one event/occur
   <xs:element name="child_name" type="xs:string" minOccurs="0" maxOccurs="10" />  ## Can have 0 to 10 records
  </xs: sequence>
 </xs: complexType>
</xs:element>
## Example
<person>
 <full_name>Tove Refsnes</full_name>
 <child_name>Hege</child_name>
 <child_name>Stale</child_name>
 <child_name>Jim</child_name>
 <child_name>Borge</child_name>
</person>

## XSD Data Types
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>   ## the date formate is yyyy-mm-dd bc it can be sorted and computer likes this way
<xs:element name="startdate" type="xs:dateTime"/>  ## yyyy-mm-ddThh:mm:ssZ
<xs:element name="prize" type="decimal"/>  ## float
<xs:element name="weeks" type="xs:integer"/>  ## integer
## It is common to represent time in UTC/GMT, given that servers are often scattered around the world
<customer>John Smith</customer>
<start>2002-09-24</date>
<startdate>2002-05-30T09:30:10Z</startdate>  ## Time and Zone
<prize>999.50</prize>
<weeks>30</weeks>
## Time matters in web and computer
## ISO 8601 Date/Time format
2002-05-30T09:30:10Z
Year-month-day Time of day  Z: Timezone - typically specified in UTC(Universal Time) / GMT(Greenwich Mean Time) rather than 

## Parsing XML in Python
import xml.etree.ElementTree as ET  # ET is alias
data = '''<person>               
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''         #####   triple-quoted string ''' is a potentially multi-line string, has a newline at the end of each line
tree = ET.fromstring(data)    ## fromstring() transform the string data to the tree pictures, this step can blow up if the string is bad
print('Name:', tree.find('name').text)  ## in the XML, find the tag name and text is an attribute under the tag node
print('Attr:', tree.find('email').get('hide'))  ## Email tag has an attribute of hide(value is yes) and do not have text
## Under a tag Node, there can be text child and multiple attributes child
## A self-closing tag do not have text child

## Child tags under tag, a tag can have multiple child tags
## Loops through a list of trees
import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
      <user x="2">
         <id>001</id>
         <name>Chuck</name>
      </user>
      <user x="7">
         <id>009</id>
         <name>Brent</name>
      </user>
   </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')  ## find all of the user under the users, this is a list of tags with all child tag information
print(lst)
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))  ## Get the attribute in the tag
    
## JSON and the REST Architecture
## JavaScript Object Notation(JSON)
## Douglas Crockford - 'Discovered' JSON
## Object literal notation in JavaScript
## Dictionaries in JSON
import json
data = '''{
"name" : "Chuck",
"phone" : {
  "type" : "intl",
  "number" : "+1 734 303 4456"
 },
"email" : {
  "hide" : "yes"
  }
}'''
## JSON represents data as nested "lists' and "dictionaries"
## JSON does not have start and end tags and there is no attributes
info = json.loads(data)   ## This can have traceback, get back an object
## the thing get back 'info' is a python dictionary
print('Name:', info["name"])
print('Name:'), info.get('name')
print('Phone:', info.get('phone').get('number'))
print('Hide:', info["email"]["hide"])
print('Phone:', info["phone"]["number"])

## Another example, List in JSON
import json 
input = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    { "id" : "009",
    "x" : "7",
    "name" : "Chuck" 
    }
  ]'''
info = json.loads(input)   ## info is a list
print('User count:', len(info))   ## two things in the list
for item in info:    ## items in info is dictionary
    print('Name', item["name"])
    print('ID', item['id'])
    print('Attribute', item['x'])

## Sevice Oriented Approach/Architectures
## Most non-trivial web applications use services
## They use services from other applications (Credit Card Charge, Hotel Reservation systems)
## Services publish the 'rules', applications must follow to make use of the service (API)
## API: Application Program Interfaces, which are ways to use web protocols to access data on systems, using well-defined and structured approaches
## Multiple Systems
## Initially - Two systems cooperate and split the problem
## As the data/service becomes useful - multiple applications want to use the information / application

## The Service Oriented Architectures (SOA)
## Using Application Programming Interfaces (API)
## We are the consumers of the data interchange
## The API is the specification for what the URL patterns are, what the syntax of the data we are supposed to send, what the syntax of data we can expect to get back
## Example, Google Geocoding API: addresses

## Example: Google APIs
## Get some JSON back from Google Geocoding APIs
http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI          ## We type in Ann Arbor, MI in the search box
## '+' is a space, '%2C' is a common in the URL syntax
## JSON, data in the following code
{
  "status": "OK",
   "results": [
      {
        "geometry": 
        { 
         "location_type": "APPROXIMATE",
          "location": {
            "lat": 42.2808256,
            "lng": -83.7430378
            }
        },
        "address_components": [
           {
              "long_name": "Ann Arbor",
              "types": [
                 "loyalty",
                 "political"
                 ],
                 "short_name": "Ann Arbor" 
          }
      ],
      "formatted_address": "Ann Arbor, MI, USA",
      "types": [
              "loyalty",
              "political"
              ]
      }
   ]
}
           
import urllib.request, urllib.parse, urllib.error
import json

serviceurl  = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})  ## This will turn the location in URL Syntax format
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)  ## This is a handle, not pull the data yet, the read() function read the data in a whole string
    data = uh.read().decode()  ## This gives back the previous JSON document in Unicode(UTF-8 transfer to Unicode),
    ## data is a string
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK':   ## if js is false or status key not in js, js status is not 'OK'
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dump(js, indent=4))
    
    lat = js["results"][0]["geometry"]["location"]["lat"]    ## go over the tree
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    
## Results:    
## Enter location: Ann Arbor, MI
## Retrieving http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
## Retrieved 237 characters
## lat 42.2808256 lng -83.7430378
## Ann Arbor, MI, USA

## Securing API Requests
## API Security and Rate Limiting
## The compute resources to run these APIs are not 'free'
## The data provided by these APIs is usually valuable
## The data providers might limit the number of requests per dat, demand an API 'key', or even charge for usage
## They might change the rules as things progress...

## Twitter APIs: need authorized for each request unlike other APIs(google)
import urllib.request, urllib.parse, urllib.error
import twurl   ## This is the code written by Chuck
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count' : '5'})
    
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(jspn.dumps(js, indent = 4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

## Below is the Twitter JSON file
Enter Twitter Account: drchuck
Retrieving https://api.twitter.com/1.1/friends/...
Remaining 14
{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one ._.",
                "created_at": "Fri Sep 20 08:36:34 +0000 2013", ...
            },
            "location": "San Francisco, California",
            "screen_name": "leahculver",
            "name": "Leah Culver", ...
        },
        {
            "status": {
                "text": "RT @WSJ: Big employers like Google ...",
                "reated_at": "Sat Sep 28 19:36:37 +0000 2013", ...
            },
            "location": "Victoria Canada",
            "screen_name": "_valeriei",
            "name": "Valerie Irvine", ...
        }, ...  ## Can have a very long list
        ]
}

## This is the Twitter JSON outputs:
Leahculver
    @jazzychad I just bought one .__.-  
Valeriei
    RT @WSJ: Big employers like Google, AT&amp;T are h
Ericbollens
    RT @lukew: sneak peek: my LONG take on the good &a
halherzog
    Learning Objects is 10. We had a cake with the LO,
    
## twurl code which creates the Signed URL
## hidden.py is the four keys that we need to put in that we get from Twitter
import urllib
import oauth
import hidden

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token = token, http_method='GET', http_url = url, parameters = parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()

## The above code will give us the true URL like:
https://api.twitter.com/1.1/statuses/user_timeline.json?count=2&oauth_version=1.0&oauth_token=101...SGI&screen_name=drchuck
&oauth_nonce=09239679&oauth_timestamp=1380395644&oauth_signature=rLK...BoD&oauth_consumer_key=h7Lu...GNg&oauth_signature_method=HMAC-SHA1

## Work Example: Twitter API

## Keep this file separate

## https://apps.twitter.com/
## Create new App and get the four strings

def oauth():
    return {"consumer_key": "h7Lu...Ng".
            "consumer_secret": "dNKenAC3New...mmn7Q",
            "token_key": "10185562-eibxCp9n2...P4GEQQOSGI",
            "token_secret": "H0ycCFemmC4wyf1...qoIpBo"}
## We need these four strings from the website

import urllib.request, urllib.parse, urllib.error
from twurl import augment    ##OAuth website
import ssl

## https://apps.twitter.com/
## Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'drchuck', 'cbunt':'2'})

print(url)

## Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data.decode())  ## byte array
headers = dict(connection.getheaders())  ## url does not show headers but we can get the headers by using getheaders
print(headers)    ## dictionary


     
## Parse the JSON very interested part
import urllib.request, urllib.parse, urllib.error
from twurl import augment    ##OAuth website
import ssl

## https://apps.twitter.com/
## Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'drchuck', 'cbunt':'2'})

print(url)

## Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    ## print headers
    print('Remaining', headers['x-rate-limit-remaining'])

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

## https://apps.twitter.com/
## Create App and get the four strings, put them in hidden.py
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
## Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})  ## ask for the forst five friends
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode() ## gives an arrays of users
    headers = dict(connection.getheaders())
    ## print headers
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)  ## This is a dictionary
    print(json.dumps(js, indent = 2))

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('No status found')
            continue
        s = u['status']['text']
        print(' ', s[:50])

















     
     