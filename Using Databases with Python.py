## Using Databases with Python

## Review Unicode, UTF-8, ASCII(American Standard Code for Information Interchange)

ASCII
## Representing Simple Strings
## Each character is represented by a number between 0 and 256 stored in 8 bits of memory
## We refer to '8 bits of memory as a "byte" of memory - (ie. my desk drive contains 3 Terabytes of memory')
## The ord() function tells us the numeric value of a simple ASCII character
print(ord('H'))  ## 72
print(ord('e'))  ## 101
print(ord('\n')) ## 10

## Based on ASCII, US computer can not talk with Asia Computer, however,
Unicode
## Using Unicode, computers can communicate, bc Unicode contains millions of characters
##Multi-Byte Characters
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
## When We read data from an external resource, we must decode it based on the character set so it is properly represented in Python 3 as a string
while True:   ## The output of while loop is the METADATA
    data = mysock.recv(512)    ## receive up to 512 characters, data is Bytes
    if (len(data) < 1):
        break    ## ends the loop until go to the file final
    mystring = data.decode()   ## decode means take the data outside work and interpret what it means internally for us
    print(mystring)   ## mystring is Unicode, decode() converts bytes(UTF-8 or ASCII) to Unicode 
    ## decode() is the opposite of encode, converts UTF-8 to unicode
bytes.decode()
str.encode()

## An HTTP Request in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
mysock.connect(('data.pr4e.org', 80))   ## a tuple in the parentheses
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()   ## take the string into bytes
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

## Objected Oriented Definition and Terminology
## Warning:
    ## This lecture is vey much about definitions and mechanics for objects
    ## This lecture is a lot more about 'how it works' and less about 'how you use it'
    ## You won't get the entire picture until this is all looked at in the context of a real problem
    ## So please suspend disbelief and learn technique for the next 40 or so slides
    
inp = input('Euro Floor')
usf = int(inp) + 1
print('US floor', usf)

## Objected Oriented
## A program is made up pf many cooperating objects
## Instead of being the 'whole program' - each object is a little 'island' within the program and cooperatively working with other objects
## A program is made up of one or more objects working together - objects make use of each other's capabilities

## Object
## An Object is a bit of self-contained Code and Data
## A key aspect of the Object apporach is to break the problem into smaller understandable parts (divide and conquer)
## Objects have boundaries that allow us to ignore un-needed detail
## We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects

## Definitions of an Object
## 1. Class - a template(shape of object) --  eg: string
## 2. Method or Message -  A defined capability of a class --  eg string.upper
## 3. Field or attribute - A bit of data in a class
## 4. Object or Instance - A particular instance of a class --  the word we give the real things-- number, ...
x = 'abc'  ## x is an object
type(x)  ## string is class, <class 'str'>, template
dir(x)  ## Methods .upper

## Our First Class and Object
## This is the template for making PartyAnimal objects, class is a reserved word
class PartyAnimal:
    x = 0  ## Each PartyAnimal object has a bit of data
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)     ## Each PartyAnimal object has a bit of code

an  = PartyAnimal()    ## Construct a PartyAnimal object and store in an variable, 'an' is an object, it is like an = list()
an.party()  ## an.x = an.x + 1
an.party()
an.party()    ## It is like passing the 'an' to parameter  PartyAnimal.party(an)
## Tell the 'an' project to run the party() code within it
#==============================================================================
# So far 1
# So far 2
# So far 3
#==============================================================================

## Playing with dir() and type()
## The dir() command lists capabilities
## Ignore the ones with underscores -  These are used by Python itself
## The rest are real operations that the object can perform
## It is like type() - it tells use something *about* a variable
print('Type', type(an))
print('Dir', dir(an))
#==============================================================================
# Type <class '__main__.PartyAnimal'>
# Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']
#==============================================================================
## We can use dir() to find the 'capabilities' of our newly created class

## Object Life Cycle
## Objects are created, used and discarded
## We have special blocks of code (methods) that get called: 
    ## 1. At the moment of creation (constructor)
    ## 2. At the moment of destruction (destructor)
## Constructors are used a lot: The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created
## Destructors are seldom used
class PartyAnimal:
    x=0
    def __init__(self):
        print('I am constructed')
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()  ## This is the moment of construction, so it will print 'I am constructed'  'I am destructed 0'
an.party()  ## So far 1
an.party()  ## So far 2
an = 42  ## This is the destruction moment, it will print out 'I am destructed 2'
print('an contains', an) ## an contains 42
## The constructor and destructor are optional. The constructor is typically used to set up variables. The destructor is seldom used.
## Constructor: In object oriented programming, a constructor in a class is a special block of statements called when an object is created

## Many Instances
## We can create lots of objects - the class is the template for the object
## We can store each distinct object in its own variable
## We call this having multiple instances of the same class
## Each instance has its own copy of the instances variables
class PartyAnimal:
    x = 0
    name = " "
    def __init__(self, z):   ## Notice, there are two '_' to become '__'
        self.name = z
        print(self.name, 'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)
s = PartyAnimal("Sally") ## so the z will be 'Sally' the name
s.party()  ## self.x = 1
j = PartyAnimal('Jim')
j.party()  ## j x=1, name='Jim'
s.party()  ## s x=2, name='Sally'
## We have two independent instances

## Defining the capabilities of Objects
## Object Inheritance
## 1. When we make a new class - we cna reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class
## 2. Another form of store nad reuse
## 3. Write once - reuse many times
## 4. The new class(child) has all the capabilities of the old class(parent) - and then some more
## Teminology: Inheritance
## 'Subclasses' are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own.
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points, self.x)
## FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more.
s = PartyAnimal("Sally")  ## 'Sally constructed'
s.party()   #'Sally party count 1'
j = FootballFan('Jim')  ## 'Jim constructed'
j.party()   ## 'Jim party count 1'
j.touchdown()   ## "Jim party count 2" the number is 2 because party() is called in touchdown().  "Jim points 7 2"
## FootballFan has x, name, points instances variables, FootballFan has a constructor, party method and touchdown method

## Summary Definitions
## Class - a template; Attribute - A variable within a class(data);  Method - A function within a class;   Object - A particular instance of a class
## Constructor - Code that runs when an object is created; Inheritance - The ability to extend a class to make a new class

## Relational Databases
## Basic Structured Query Language: Database Introduction
## Relational databses model data by storing rows and columns in tables. The power of the relational database lines in its ability to efficiently retrieve data from those tables 
## and in particular where there are multiple tables and the relationships between those tables involved in the query.
## Terminology
## Database - Contains many tables
## Relation (or table) - contains tuples and attributes
## Tuple (or row) - a set of fields that generally represents an "object" like a person or a music track
## Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row.

## SQL 
## Structured Query Language is the language we use to issue commands to the database
## 1. Create a table  2. Retrieve some data   3. Insert data (Update Data)    4. Delete data

## Using Databases
## Two roles in Large Projects( Website tracking data has a databse):
## 1. Application Developer - Builds the logic for the application, the look and feel of the application - monitors the application for problems
## 2. Database Administrator - Monitors and adjusts the database as the program runs in production
#### Often both people participate in the building of the 'Data model'

## Database Model:
##  A database model or database schema is the structure or format of a database, described in a formal language supported by the database management system
## In other words, a 'database model' is the application of a data model when used in conjunction with a database management system.

## Operate some staff in SQLite Browser

/* 1 */
CREATE TABLE Users(
  name VARCHAR(128),
  email VARCHAR(128));
  
insert into 'Users' (name, email) VALUES('Chuck', 'csev@umich.edu');
insert into 'Users' (name, email) VALUES('Colleen', 'vit@umich.edu');
insert into 'Users' (name, email) VALUES('Sally', 'sally@umich.edu');
## SQL Insert
## The Insert statement inserts a row into a table
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu');
                  
## SQL Delete
## Deletes a row in a table based on a selection criteria
DELETE FROM Users WHERE email='ted@umich.edu';

## SQL: Update
## Allows the updating of a field with a where clause
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu';

## Retrieving Records: SELECT
## The select statement retieves a group of records - you can either retrieve all the records or a subset of the records with a WHERE clause
SELECT * FROM Users
SELECT * FROM Users WHERE email='cesv@umich.edu';

## Sorting with ORDER BY
## You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name DESC

## Working Example: Counting Email in a Database: emaildb.py file
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')  ## Create the file called 'emaildb'
cur = conn.cursor()  ## open the handle and also able to send SQL commands and get responses through that same cursor
dir(cur)
## [ 'arraysize', 'close', 'connection', 'description', 'execute', 'executemany', 'executescript', 'fetchall', 'fetchmany', 'fetchone', 'lastrowid', 'row_factory', 'rowcount', 'setinputsizes', 'setoutputsize']
cur.execute('''
DROP TABLE IF EXISTS Counts''')   ## drop the table unless it exists in emaildb file

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From:'): continue
    line = line.strip()
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))  ## '?" is a placeholder, make sure that we don't allow SQL injection
    ## (email,) is a one-thing tuple, "?" let the email to replace it
    ## The above step is not retrieving the data, is to make sure table name is right or if there is any syntax errors
    row = cur.fetchone()  ## grab the first one and give it back to row
    ## the row will be a list, but only one thing, a list of None
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) Values (?, 1)''', (email,))  ## row is None, and then count will be initiate as 1
        ## Then a record will be added in a table
    else: 
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE email= ?''', (email,))  ## row is not None and then the count in Count will be updated
    print((email, row))
    conn.commit()  ## force to write into the disk memory

## https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()


## Exercise on the mbox document
import sqlite3

conn = sqlite3.connect('domain.sqlite')  ## Create the file called 'emaildb'
cur = conn.cursor()  ## open the handle and also able to send SQL commands and get responses through that same cursor
dir(cur)
## [ 'arraysize', 'close', 'connection', 'description', 'execute', 'executemany', 'executescript', 'fetchall', 'fetchmany', 'fetchone', 'lastrowid', 'row_factory', 'rowcount', 'setinputsizes', 'setoutputsize']
cur.execute('''
DROP TABLE IF EXISTS Counts''')   ## drop the table unless it exists in emaildb file

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From:'): continue
    line = line.strip()
    pieces = line.split()
    email = pieces[1]
    email = email.split('@')
    org = email[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))  ## '?" is a placeholder, make sure that we don't allow SQL injection
    ## (email,) is a one-thing tuple, "?" let the email to replace it
    ## The above step is not retrieving the data, is to make sure table name is right or if there is any syntax errors
    row = cur.fetchone()  ## grab the first one and give it back to row
    ## the row will be a list, but only one thing
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) Values (?, 1)''', (org,))  ## row is None, and then count will be initiate as 1
        ## Then a record will be added in a table
    else: 
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org= ?''', (org,))  ## row is not None and then the count in Count will be updated
    #print(row)
    conn.commit()  ## force to write into the disk memory

## https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()

## Worked Example: Twspider.py
from urllib.request import urlopen
import urllib.eror
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER)')

## Ignore SSL certificate errors
cts = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')  ## read from the database on unretrieved Twitter person and then grab all that person's friends
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue
    url = twurl.augment(TWITTER_URL, {'screen_name':acct, 'count': '5'})  ## this has the hidden.py whihc has our secrets and tokens
    ## five recent friends only
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    
    print('Remaining', headers['x-rate-limit-remaing'])
    js = json.loads(data)  ## it returns a list
    ## Debugging
    ## print json.dumps(js, indent = 4)
    
    cur.execute('UPDATE TABLE Twitter SET retrieved=1 WHERE name=?', (acct,))
    
    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(frined)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend,))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()
    
cur.close()


## Data Models and Relational SQL: Designing a Data Model 
## Database Design
## 1. Database design is an art form of its own with particular skills and experience
## 2. Our goal is to avoid the really bad mistakes and design clean and easily understppd databases
## 3. Others may performance tune things later
## 4. Databse design starts with a picture...

## Building a Data Model
## 1. Drawing a picture of the data objects for our application and then figuring out how to represent the objects and their relationships.
## 2. Basic Rule: Don't put the same string data in twice - use a relationship instead.
## 3. When there is one thing in the 'real world' there should be one copy of that thing in the database.

## There are rules about do not put the same string in twice, what if that is the users exactly want to see?
## We need to write a very efficient data model to show this information to user
## For each 'piece of info':
## 1. Is the column an onject or an attribute of another object?
## 2. Once we define objects, we need to define the relationships between objects

## Building the data Model: Consider
## 1. What is the thing that is the most essential to this application? (eg. a thing that manages tracks )
## 2. When confirm the thing is track: Consider which of these columns are themselves tables, and which of these things are just attributes of track
#### The time, ratings are part of the track (attribute of track)
#### So first table is Track: Title, Rating, Len, Count
## 3. Tracks belong to albums, albums belong to artists
#### What if some fields is not an attribute and also not an object? Like genre
#### Consider if you change genre in one row, the album/artist will change all the genre value if genre is attribute of album or artist.
####  but the track will only change one row

## Create the tables
## The end point of the arrow can be the primary key which is a unique to each row in the table, 
## The start point of the arrow canbe a foreign key in one table
## The logical key is the unique thing that we might use to look up this row from the outside world. Logical Keys might be used in WHERE clause.


## Creating a Database with Primary Key, Foreign Key, Logical Key, Attributes
CREATE TABLE Track(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title TEXT,
  album_id INTEGER,
  genre_id INTEGER,
  len INTEGER, rating INTEGER, count INTEGER);
        
## Inserting Relational Data
INSERT INTO table(var) VALUES('values')
INSERT INTO Album(title, artist_id) VALUES('Who Mde Who', 2);
INSERT INTO Album(title, artist_id) VALUES('IV', 1);
## Model relationships and connection points rather than replicating data

## Reconstructing Data with JOIN 
## Relational Power
#### 1. By removing the replicated data and replacing it with references to a single copy of each bit of data we build a 'web' of information that the relational database can read through very quickly - even for every large amounts of data.
#### 2. Often when you want some data it comes from a number of tables linked by these foreign keys.

## The JOIN Operation
#### 1. The JOIN operation links across several tables as part of a select operation.
#### 2. You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause.
## For example:
SELECT album.title, artist.name FROM album JOIN artist ON album.artist_id=artist.id;
SELECT album.title, album.artist_id, artist.name FROM album JOIN artist ON album.artist_id=artist.id;
SELECT track.title, genre.name FROM track JOIN genre ON track.genre_id=genre.id;
## Joining two tables without an ON clause gives all possible combinations of rows.
## Complex Inner Join 
SELECT track.title, artist.name, album.title, genre.name FROM track JOIN genre JOIN album JOIN artist 
ON track.genre_id=genre.id AND track.album_id=album.id AND album.artist_id=artist.id;
## We can reconstruct the replication, but we don't actually store the replication.

## Worked Example: Tracks.py
## Combined the SQL and Python
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()   ## like a file handle

## Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
        
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter file name: ')
if (len(fname)< 1): fname = 'Library.xml'

## Example
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')  ## find to the third level dictionary, find all the tracks(songs include the information)
print('Dict count:', len(all))

for entry in all: 
    if ( lookup(entry, 'Track ID') is None ) : continue
    
    name = lookup(entry, 'Name')
    genre = lookup(entry, 'Genre' )
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    if genre is None or name is None  or artist is None or album is None: continue
    print(name, artist, genre, album, count, rating, length)
## IGNORE in SQL means if you insert the same thing twice, ignore once with violate the UNIQUE criteria    
    cur.execute('''INSERT OR IGNORE INTO Artist(name)       
    VALUES ( ? )''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name= ?', (artist, ))    ## Get the PRIMARY KEY for this particular INSERTED new row
    artist_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre(name)       
    VALUES ( ? )''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name= ?', (genre, ))    ## Get the PRIMARY KEY for this particular INSERTED new row
    genre_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
    VALUES (?, ? )''', ( album, artist_id))                              ## This artist_id is just retrieved from the previous execute statement
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]   ## This is the foreign key for other table
    
## REPLACE in SQL means if the UNIQUE criteria is violated, then this turns into an update
    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
    VALUES (?, ?, ?, ?, ?, ? )''',
    (name, album_id, genre_id, length, rating, count ) )

    conn.commit()
    
            
## Many-to-Many Relationships
#### 1. Sometimes we need to model a relationship that is many-to-many (for example: books -- authors)
#### 2. We need to add a 'connection' table with two foreign keys.
#### 3. There is usually no separate primary key.

## Examples of Coursear
## Start with a Fresh Database
CREATE TABLE User (
        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT,
        email   TEXT
)

CREATE TABLE Course (
        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title   TEXT
)
## conjunction table / connector table
## The 'PRIMARY KEY(user_id, course_id) force that the combination of (user_id and course_id) must be unique in this table
CREATE TABLE Member (
        user_id    INTEGER,
        course_id  INTEGER,
        role       INTEGER,
        PRIMARY KEY (user_id, course_id)
)

## Insert Users and Courses
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');
INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');
                   
## Insert Memberships
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);
                   
INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);
        
INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name;

## Worked Example: roster.py: Many to Many tables
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

## Do some Setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id      INTEGER,
    course_id    INTEGER,
    role         INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

fname = input('Enter file name:')
if len(fname) < 1: 
    fname='roster_data_sample.json';
    
# [
#   [ "Charley",  "si110", 1 ],
#   [ "Mea", "si110", 0],  

str_data = open(fname).read()
json_data = json.loads(str_data)   ## Parsing the JSON data and json_data will be an array of arrays

for entry in json_data:   ## entry itself is a row
    name = entry[0];
    title = entry[1];
    role = entry[2];
    
    print((name, title))
    
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    user_id=cur.fetchone()[0]   ## sub 0 means if there are more than one thing selected, just fetch the first one
    ## Ignore the older duplicated record and keep the latest one 
    cur.execute('''INSERT OR IGNORE INTO Course (title)   
        VALUES (?)''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES (?, ?, ?)''',
        (user_id, course_id, role))
    
    conn.commit()
    
## Code Sample Worked Example: Twfriends.py
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl
## We also need to create a hidden.py file which contains th ekeys and tokens from Twitter
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS People
           (id INTEGER PRIMARY KEY, name TEXT UNQIUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
           (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

## Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit:')
    if (acct = 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
## All the new accounts we put in are the ones for which we haven't retrieved.
        try:
            (id, acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (acct, ))
## Want to find out if the acct we entered is in the DB or not
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''INSERT OR IGNORE INTO People
                        (name, retrieved) VALUES (?, 0)''', (acct, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid
            
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context = ctx)
    except:
        print('Failed to Retrieve')
        break
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    
    print('Remaining', headers['x-rate-limit-remaining'])
    
    try:
        js = json.loads(data)
    except Exception as err:
        print('Unable to parse json', err)
        print(data)
        break
    
    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent = 4))
        continue
    
    cur.execute('UPDATE People SET retrieved = 1 WHERE name = ?', (acct, ))
    
    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                       VALUES (?, 0)''', (friend, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id))
    print('New accounts=', countnew, 'revisited=', countold)
    conn.commit()
cur.close()

            
## Databases and Visualization
## Geocoding

## Multiple Steps on Data Analysis 
## Many Data Mining Technologies
#### 1. https://hadoop.apache.org/
#### 2. http://spark.apache.org/
#### 3. https://aws.amazon.com/redshift/
#### 4. http://community.pentaho.com/

## GeoData
#### Step 1. Makes a Google Map from user entered data
#### Step 2. Uses the Google Geodata API
#### Step 3. Caches data in a database to avoid rate limiting and allow restarting
#### Step 4. Visualized in a browser using the Google Maps API

## Worked Example: Geodata
## the code is geocode.py which use the Google places API to look places up, where.date is a file with list of organizations people type in
## The where.data is read by geoload.py

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
## If you have a Google Places API key, enter it here
## api_key = 'AIzaSy___IDByT70'

if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    
## Additional detail for urllib
## http.client.HTTPConnection.debuglevel =  1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

## Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200:
        print('Retrieved 200 locations, restart to retrieve more')
        break
    
    address = line.strip()
    print(' ')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (memoryview(address.encode()), ))
    
    try:
        data = cur.fetchone()[0]
        print('Found in Database', address)
        continue
    except: 
        pass
    
    parms = dict()
    parms['query'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1
    
    try:
        js = json.loads(data)
    except:
        print(data)  ## We print in case unicode causes an error
        continue
    
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print("====Failure To Retrieve ====")
        print(data)
        break
    
    cur.execute('''INSERT INTO Locations (address, geodata) VALUES (?, ?)''',
                (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    if count % 10 == 0:
        print('Pause for a bit...')
        time.sleep(5)
        
print("Run geodump.py to read the data from the database  so you can visualize it on a map")
        
## Geodump data: use the data in database to make it visualize
import sqlite3
import json
import codecs     
        
conn = sqlite3.connect('geodata.sqlite')       
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8") ## open the where.js with utf-8
fhand.write("myData = [\n")  
count = 0
for row in cur :
    data = str(row[1].decode())  ## use the geodata in the sql file
    try:
        js = json.loads(str(data))
    except: continue
 
    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0: continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try:
        print(where, lat, lng)
        
        count = count + 1
        if count > 1:
            fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






































