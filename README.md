Comments are the none executable statement in a program.



\# Indentation-

White space at the beginning of the line is called indentation.



\# Sequence-

It is an ordered collection of items, indexed by positive integers. It is a combination of mutable and non-mutable data types.

There are following types of sequence datatype in python :

 A)- Strings - It is an ordered sequence of letters or characters, they are enclosed between quotes. They can have any character or sign including space in them. (Immutable). I string with len 1, represents character in python.

B) - List - It consists of items separated by "," and enclosed within []. The value stored in list are accessed using indexes. The index of the first element is 0 and last is (n-1) or -1, where n are total elements in a list. Operations performed on list are - 1)- Slice, 2) Concatenation, 3) - Repetition.

C) - Tuple - It is similar to list, its values are separated by commas, but enclosed within (), tuple is immutable. (read only datatype)

 

\# Type Conversion-

int(x) - converts to int

long(x) - converts to long int

float(x) - converts to float

str(x) - converts to string

tuple(x) - converts to tuple

list(x) - converts to list

set(x) - converts to set

ord(x) - converts a single char to its integer value

oct(x) - converts an int to octal string

hex(x) - converts an int to hexadecimal string

chr(x) - converts int to char

unichr(x) - converts int to Unicode char

dict(x) - creates a dict if x forms a (key-value) pair



\# Dictionary-

It stores data in key-value pairs, the key value are usually string and value can be of any datatype. (Enclosed within {}). Each key-value pair is separated using colon. To access any value in dictionary, its keys needs to be specified in \[] braces. They are used for fast retrieval of data.



\# Unary Operator -

\# Bitwise Operator (Only works on integers in Python)

OR - |

And - \&

Not - !

XOR - ^



unasigned char a = 5, b = 9



printf("a>>1 = %d\\n", a>>1)



x = 2^y --> this represent magnitude of shift

or

a = 2^1



128 >> 5

128/(2^5)

128/32

4



right shift



12 << 3

12 \* 2^3

12 \* 8

96



no \* 2^n





logical operators:



Logical AND : (a>b) \&\& (b>c)

Logical OR  : (a>b) || (b>a)

Logical NOT : It produces 0 if the expression evaluates to anything except zero and produces 1 if the expression produces 0. a = 10, b = !a = 0



Assignment operators:



Assign (=)

Add and assign (+=)

Subtract and Assign (-=

Multiply and Assign \*=

Divide and Assign /=

Modulus and Assign %=

Divide (floor) and Assign //=

Exponent and Assign \*\*=

Bitwise AND and Assign \&=

Bitwise OR and Assign |=

Bitwise XOR and Assign ^=

Bitwise right shift and Assign >>=

Bitwise left shift and Assign <<=



Membership Operators: Checks the availability or existence of a value in a specified sequence a sequence can be a string, tuple, dictonary and list.

They are of two types:-



in operators: Returns True if the specified value is the member of the sequence

NOT IN operators: Returns True if the specified value is not the member of the sequence



Identity operator: It Compares the id() of the objects.

It is of two types:



is operator: Returns True when the both the operands have the same id

is not operator: Returns true when both the operands do not have the same id



\#python is only an OOP language so everything in py is an object and every object is assigned an address



Understand the id() function: Each object in python has a memory location identified using a unique ID

That ID of a object can be checked using id() function.

Syntax - id(object\_name)



id will belong to the value not the variable and if we type only the string again it will show the same value bcz python doesn't allocate diff memory location for string.



is= operators and is operators diff:



equality operators is used to compare the values, whereas the identity operators is used to compare the id's.



\#In python list can be modified so that's why python do not allocate same id to the list where as integers, strings and non amendable objects so the same memory location remains once given to any object.



Expressions: It is a legal combination of symbol that represent the value. It must have at least one operands and one or more operators

1\. Constant expression

2\. Internal exp

3\. Floating point exp

4\. Logical exp

5\. Bitwise

6\. Assignment



for loop - for i in range(beg, end, \[step]):



Counter-controlled:-

No. of execution - Used when number of times the loop has to be executed is known in advance

Condition variable - We have a counter variable

Value and limitation of var - Condition for execution and counter variable are strict



while (i <= 10):

 	print(i, end=" ")

 	i += 1



Condition-controlled:-

No. of execution - Used when number of times the loop has to be executed is not known in advance

Condition variable - We have a sentinel variable

Value and limitation of var - Condition for execution and counter variable are strict



i = 1

while (i > 0):

 	print(i, end=" ")

 	i += 1

 	if (i == 10):

 		break



Python treats string as continuous series of characters delimited by single, double or triple quotes. Python has built in string class named str.



Indexing: Each character in a string are accessed using a subscript operator\[] the expression in the \[] is called as index.



Positive subscript helps to index from the beginning

Negative subscript helps to index from the end

positive starts from 0 and ends at n-1 whereas negative starts from -n+n-14 and ends at -n



mutable variable value changes whereas immutable variable values will not change, modifying an immutable variable will rebuilt the same variable. Strings are immutable and contents of strings cannot change after they are created.



traversing is indexing all char action from beg to end.



Operation of strings:



Concertation



repetition



in(Membership)



not in





Slice





Striding in python:



W e l c o m e   t o    t  h  e     w  o  r  l  d     o  f     P  y  t  h  o  n

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29



String formatting operators:

The % operator takes formatted var on left and the corresponding value of tuple on right. The formatting operator allow to construct string, replacing string with data store in the variable.



%s for string

%d for integer

%f for float

%b for binary

%o is for octal numbers

%x is for hexadecimal numbers

%e is for floating point in an exponent format



Floating point numbers use the format %a.bf, where 'a' would be the minimum number of digits to be presented in the string and 'bf' represent how many digits are displayed after decimal point.



Method of formatting  using format() method:

Formatting is used in python3 for handling complex string more efficiently. Formatters work by putting in one or more replacement fields and placeholders defined by a pair of curly braces{} into a string and calling it str.format(). The value we wish to put into the placeholders and concatenate with the string passed as parameters into a format function.



Float precision with the .format() method:



Syntax: {\[index]:\[width]\[.precision]\[type]}



ord() and chr() function:

ord() function returns the ASCII code of the character and chr() function returns the character represented by an ASCII number.



ASCII and Unicode are two popular encoding schemes. ASCII encodes symbols, digits, letters, etc., whereas Unicode encodes special texts from different languages, letters, symbol, etc. It can be said that ASCII is a subset of the Unicode encoding scheme.



ASCII   	Is known as American Standard code for information interchange.

 		It is the standard that encodes the charter of communication.

 		It has two standards - 			7bit: 128 characters 			8bit: 256 characters

 		It supports specific characters and occupy less space.

 		0-9 -> 47-57   		a-z -> 97-122  		A-z -> 65-90		"space" -> 32



Unicode 	Is also known as universal character set of universal coding system.

 		It is the IT standard that encodes the text for Computer and other communication devices.

 		Three standards. 			UTF-8: 256				UTF-16: 65536					UTF-32: 4294967296

 		UTF- Unicode transformation format

 		Occupies more space and large no of characters.



since, chr() function takes an integer argument and converts it into a character, there is a valid range for the input. The valid range for the argument is from 0 through 1,114,111 (0\*10FFFFin hexadecimal format). Value error will be raised if the input integer is outside this range.



ord() takes only one single character.



Comparing Strings:



Operators			Description									Example



==				If two strings are equal it returns True					"AbC" == "AbC"



!= or <>			If two strings are not equal, it returns True					"AbC" != "Abc"

 														"abc" <> "ABC"



>				If the first string is greater than the second, it returns True			"abc" > "Abc"



<				If the first string is smaller than the second, it returns True			"abC" < "abc"



>=				If the first string is greater or equal to the second, it returns True		"aBC" >= "ABC"



<=				If the first string is smaller or equal to the second, it returns True		"ABc" <= "ABc"





Function declaration: It is the statement that identifies the function with its name, a list of arguments that it accepts and the type of data it returns.



Function definition: It consists of functions headers which identifies the function followed by the body of the function containing the executable code for the function. The input that the function takes is known as arguments.





Parameter:  A parameter is the variable always listed inside the parenthesis in the function definition.



Argument :  An argument is the value that sent to the function when it is called.





Local variable: A variable which is defined within the function is local to the function, a local variable can be accessed from the point of its definition until the end of the function.

Global variable: A variable which are defined in the main body of the program file, they are visible throughout the program file.



Return statement:



Return a value to the caller.

To end and exit a function and go back to its caller.



Syntax:

 		return\[expression]



Required arguments:	In the required arguments, the arguments are passed to a function in correct positional order. Also, the number of arguments in the function call should exactly match the number of arguments specified in the functions.



Keywords Arguments: When we call a function with some value the values are assigned to the arguments based on their position. Python allows function to be called using keywords argument in which the order or the position of the argument can be changed. The values are not assigned to the argument according to their position but based on their name or keywords.



i)  Keywords argument is beneficial in two cases is when you skip the argument.

ii) If in function called you change the order of parameters.



Variable length arguments: In some situations it is not known in advance how many arguments will pass through the function in such case python allows the programmer to make function calls with arbitrary no of arguments for this function definition uses an \* before the parameters name.



def functionname(\[args1, args2, ...] \* var\_args\_tuple):

    function statements

    return \[expression]



Arbitrary keywords arguments (\*\*kw args): (condition:- we do not know how many \*\*kw args will be passed in the function so we add two \* before the parameter name) In this way function will receive a dictionary of arguments.



Default arguments: Python allows user to  specify function arguments that can have default values. That means that a function can be called with fewer arguments than it is defined to have.



Lambda function or anonymous function: It is created using lambda keyword. Lambda function contains only a single line.



Modules: In python modules are simply files with not py extension containing python code that can be imported inside another python program. The module contains the following components:



i) Definition and implementation of classes.

ii) Variables.

iii) Functions that can be used inside another program.



To create a python Module go to 







Case insensitive comparison: While checking the equality in strings the case of the string can be ignored by bringing both the strings in one particular case. i.e. We could bring the string in upper or lower cases and then preform the comparisons. The cases of the strings can be changed using pre inbuilt functions



i)	casefold(): Converts it into lower case

ii)	lower

iii) upper



Difference between casefold() and lower is that casefold() is more aggressive and converts more letters into lowercase than the lower function. It aims to remove all case distinction from caseless matching particularly the non ASCII characters. The casefold() function dares to comprehensive Unicode case folding algorithm as compare to simpler ASCII base lower function.

Tuple - It is another data type supprt by Python. It is different from list in two ways.
i) Tuple is a sequence of immutable object.
ii) Tuple uses () to define its elements. argum

Since tuple is an immutable data structure, you cannot delete value(s) from it. Of course, you can create a new tuple that has all the elements in your tuple except the ones you don't want (those you wanted to be deleted).

Advantages of tuple over list: Tuple store different data type values, whereas list stores single data type. Tuple is immutable so iterating through tuple is faster as compared to list. Tuple can be used as keys for dictionary but list cannot. Tuple are best for storing data as they re write protected. Tuple can be used in place of list where the no. of values are known and small. Multiple values from a funtion can be returned using a tuple. Tuple are used to format strings.  If a tuple is passed as an argument in a function then the potential for unexpected behaviour due to alligning large link get reused

Sets: It is a data set in python. It is similar to list and you do not have to duplicate entries. Sets is a mutable and unordered collections of items. Set is created by placing all the elements inside {} seperated by "," or by using built in function set.

Using list as a stack

Advantages of stack - Stack in python can allocate memory dynamically which cannot be done in the list. List in python take a lot of effort to add a new element or remove an element, whereas it could be easily done in stack.

Using list as queue - It is a data structure which stores element in an ordered manner. In computer system OS make full use of queue in following:- 

i)      Maintaining waiting list for a single shared resource like printer, disc, cpu etc.
ii)     To transfer asynchronuasly between two processes. Ex- pipes, File I/O and sockets(use for communication between two users like Whatsapp).
iii)    As buffers on mp3 player, portable CD players, Ipod, playlist.
iv)     Queue supports 3 basic operations:-  
a) Insert
b) Delete
c) Peep/Peek

v)      Queue can be implemented using "append" method. 
        To insert elements at the end of queue we use "insert" method.
        To delete first elemnt from the quesue at index(0) "pop" method is used.
        To print the elemenet of the last index "slice" operation is used.

# When list is used as queue where 1st element is inserted and retrieved first list is not efficient for this purpose.
# Append and pop at end of the list is faster bu performing insert and pop at the beginning of the list is slow because all the element have to shifted by one.

List comprehension - It helps programmer to create a list in a concise way. It is mainly beneficial to make new list where each element is obtained by applying some operation to each member of another sequence.

Looping in the list

Using enumerate - It is used when you want to print the index as well as the item in the list. The function returns and enumerate object which contains the index and the value of the item in a list as a tuple. The range function is used when you need to print index. 

Using an iterater - It can be created usig built in "iter()" function. It fetches the value and automatically points to the next element in the list when it is used with the "next()" method.

Filter function - It construsts the list from those of the list from for which a function returns true. If a sequence is string, unicode or a tuple. Then the result will be of same type otherwise it will always be a list.

Map function - It applies a particular function of every element of the list after application it returns modified list. The "map()" function calls function(item) for each item in the sequence and returns a list of return values.

Reduce function - It returns a single value generated by calling the function on the first two items of the sequence, then on the result and the next item and so on.

File Handling - It is a collection of data stored on secondary storage device like hard-disk.

File path - File that are stored on a storage medium can be retrieved easily when required. every file is identified by its path which begins from root. The file path is also known as path main. Paths are of two types
i)      Absolute path: Conatins root and complete directory list to specify exact location of the file.
ii)     Relative path: Needs to be combined with another path in order to access the file. It starts with the work of the current working directory and so on (leading with /).Ex - C:\Drivers\Audio\Aispeech

ASCII - A text file is a stream of characters that can be sequencically processed by a computer in forward direction. For this reason it is open for only one kind of operation at a time. 

Binary file - It may contain any type of data encoded in binary form. For computer storage and coding purposes. It is collection of bytesit is also referred as character stream with two essential differences.
i)      Binary file does not require any special processing of the data and each byte of data is transferred to and from the Disk. 
ii)     Python plays no constructs on the file. It may be read from or returned to in any manner the programmer wants, while text file can be processed sequentially binary file can be processed either sequentially or randomly based on the needs of the application. 

Dictonary - It is a data structure in which we store values as pair of key and the values and their key is seperated by(:), The entire item in in a dictonary is enclosed in {}. 

Difference between List and Dictonary - 

i)      It is an ordered set of items but dictonary is used for matching one item with another.
ii)     We can use indexing to access a particular item but index should be a number. We can use any type of value as an index.
iii)    List are used to look up a value whereas Dictonary is used to take a value and look up another value, for these reason Dictionary is known as lookup table.
iv)     Key pair value may not be displayed in order in which they are specified while defining the Dictionary these is because of python complex algorithm called hashing. These make Dictionary prefeable over a list of tuples.

Regular expressions - It is a powerful tool for various kind of string manipulation. These are the text string used for descibing a search pattern to extract information from text such as code, file, log, spreadsheet or even documents. Regular expression are domain specific language present as a library in most of modern programming language besides python. Regular expression are a simple sequence of char that heps to match or find string in another string. In python regular expressions can be accessed iusing re module which comes as a part of standard lib.

Meta Characters - 

Meta Characters                         Descriptions

        \                       Used to drop the special meaning of character following it.

        []                      Represent a character class.

        ^                       Matches the beginning.

        $                       Matches the end.

        .                       Matches any character except the newline.

        |                       Means OR(matches any chars seperated by it).

        ?                       Matches zero or one occurence.

        *                       Any number of occurences(including 0 occurence).

        +                       One or more occurence.

        {}                      Indicate no of occurnence of a precending regex to match.

        ()                      Enclose a group of regex.


backslash '\' - It makes your character treated in a special way because this can considered a way of escaping meta characters. For ex- If you want to search for a '.' in a string then it will be treated as a special char as one of the meta char. To avoid this case a '\' will be use before the '.'.

[] - It represent the character class consisting of set of characters which need to match. For ex- [abc] will match any single character a, b or c. 
A range of characters can be specified using '-' or ',' inside the []. For ex- [0, 3] the range is 0, 1, 2, 3. [a - c] range will be a, b, c.

The carrot class can be inverted using '^' sign. For ex- [^0 - 3] means any number except 0, 1, 2 or 3. [^a - c] means any character except a, b or c.

The carrot(^) matches the beginning of the string that it check if the given character/s or not. For ex- ^g will check if the string starts with g such as glue, globe, garden etc.     ^ge will check if a sentence starts with char ge.

Dollar sign ($) - It checks if the end of the string ends with a given character or not. For ex - s$ will check for the string that ends with s. ks$ will check for string that ends with ks.

Dot(.) - It matches only a single char except the newline char. For ex- a.b will check for the string that contains any char at the place of '.' such as acb, acbd, abbb.       '..' will check if string contains atleast two characters.

OR symbol (|) - It is the next meta character it works as OR operator and check wether the pattern before or after the 'OR' symbol(|) is present in the string or not. For ex-  a|b will match any string that contains a OR b such as acd, bcd, abcd etc. 

"?" - Checks if string before the '?' in the reg x occurs atleast once or not at all. For ex- ab?c will be matched for the string ac, acb, dabc but will not be matched for abbc because there are 2 b's similarly it will not be matched for abdc bcz b is not followed by c 

"*" - It mtches 0 or more occurences of reg x preceeding the '*' symbol. For ex- ab*c will be matched for strings ac, abc, abbbc, babc but will not be matched for abdc bcz b is not followed by c.

"+" - It matches one or more occurence of the reg x preceeding the '+' symbol. For ex- ab+c will be matched for string abc, abbc, dabc but will not be matched for ac, adbc bcz there is no b in ac and d is not followed by c in adbc. 

Braces {n, m} - It matches any repitision preceeding reg x form m to n both inclusive .For ex- a{2, 4} will be matcehd for string aab, baaaac, gaad but will not be matcehd for string like abc, bc bcz there is only one 'a' or no 'a' in both the cases. 

Group () - It is used to group sub patterns. For ex- (a | b)cd will match for string like acd, abcd, gacd

Special sequences - it is "\" followed by one of the characters givevn below which are as follows. 

i)      \A      -       Returns a match if the specified characters are at the beginning of the string.
ii)     \b      -       Returns the match where the specified characters are at the beginning or at the end of a word.
(r in the beginning makes sure the string is a raw string)
iii)    \B      -       Returns a match where the specified characters are present but not at the beginnig of the word.
iv)     \d      -       Returns a match where the string contains digits (0 - 9).
v)      \D      -       Returns a match where the string does not contains digits (0 - 9).
vi)     \s      -       Returns a match where the string contains whitespace characters.
vii)    \S      -       Returns a match where the string does not containa whitespace character.
viii)   \w      -       Returns a match where the string contains any word character(A-Z, 0-9 and underscore char).
ix)     \W      -       Returns a match where the string does not contains any word character.
x)      \Z      -       Returns a match where specified characters are at the end of the string.

match() function - It checks only at the beginning of the string and not the whole string. Matches a pattern to string with optional flags. Syntax - re match(padrin, string, flags = 0). It checks if the given string begins with the word or not. Some flags are - 

i)      re.l    -       Case senitive matching.
ii)     re.M    -       Matches at the end of the line.
iii)    re.X    -       Ignores whitespace characters.
iv)     re.U    -       Interprets letters according to unicode character set. 

Search function - The search function in the re module searches for a pattern anywhere in the string. It syntax can be given as re.search() It searches for the first occurence of the pattern and a match object is returned or none.

finditer function :- 
findall() - It is used to search a string and returns the list of matches of the pattern in the string. If no match is found then returns list is empty. It will find the match pattern as many time it occurs in the string.

Syntax  -        matchList = re.findall(pattern, input_str, flags=0)

sub() function - sub() function in the re module can be used to seacrh a pattern in the string and replace it with another pattern.

Syntax  -       re.sub(pattern, repl, string, max=0)

The sub() function replaces all the occurence of the pattern in the string with repl, substituting all the occurences unless any max value is provided. This method returns a volatile string. 

Procedure oriented programming(POPS)    -   It baasically consists of writing a list of instruction or actions for the computer to follow and organising these instruction into groups knowns as functions. Flow chart is normally used to organise this actions and represent the flow of control from one action to another. More attention or concentration is given to the work is to the development of the function  and very less attention is given to the data that is used by the function
   
i)      Emphasis on algorithm.
ii)     Large program divided into smaller program known as function.
iii)    Most of the function share global data.
iv)     Open movement of data around the system from function to function.
v)      Transformation of data using function.
vi)     Top down approach is applied in the program.

Object oriented programmings(OOPS)      -       Moves/treat data as critical data around the system. It does not allow the data to move freely around the system. It protects accidental modification of the data from outside functions. It allows decomposition of the probelm in multiple entities known as object and built data of function around these objects. The data of an object can be accessed only by the function associated with the object. However function of one object can access the function of other object. It followss bottom-up approach in the program design.

# OOPS is an approach which provide a way of modularising the program by creating partition memory area for both data and function that can be used as template for creating copies of such modules on demand. 

Basic concepts of OOPS - The basic concepts are 
i)      object
ii)     Classes
iii)    Data abstraction and encapsulation
iv)     Inheritance
v)      Poly
vi)     Dynamic binding
vii)    Message passing

Object - They are the basic run-time entities that the program has to handle. It may also represent user defined data such as vector, time and list. When a program is executed object interact by sending msgs to one another. 

Object: Student                                         Student 
---------------------------                            
DATA                                            |   Total   |
        Name
        Date-of-birth
        Marks
        .....                                   |  Average  |
---------------------------                     
FUNCTIONS
        Total
        Average
        Display                                 |  Display  |
        .....

Classes - The entire set of data and code of an object can be made a user defined data type with the help of a class object are the variables of type class. Once a class has been defined any no. of object belonging to that class can be created. Each object id associated with a data of type class from which they are created. A class is thus a collection of object of similar type.
Ex - Fruit Mango;

Data encapsulation - Wrapping up of data and function into a single unit (called class) is known as encapsulation. The data is not accessible to the outside world only the function which are wrapped inside the class can access it. These function provide the interface between the objects data and the program. This insulation of data from direct access by the program is called data hiding or information hiding. 

Data abstraction - It refers to the act of representing essential features without including the background details or explanation. Classes use this concept and are defined as a list of abstract attributes such as size, weitght and cost and function operates on these attributes. The attributes are sometimes called data members and the function that operates on this data are known as methods or member function. Classes are also known as abstract data types. 

Inheritance - It is the process by which object of 1 class acquire the properties of objects of another class. The concept of inheritance provides the idea of reusablility, this means additional feature can be added to an existing class without modifying it. This is possible by deriving the new class from the existing one. The new class will have combine features of both the classes. 

Polymorphism - It play an important role in allowing object having different internal structure to share the same external interface. It says that the general class of operations maybe accessed in the same manner even though specific action associated with each operation may differ. It is also extensively used in implementing inheritance. 

i)      Operators overloading - An operations may exibit different behaviour in different instances. The behaviour depends upon the type of data used in the operation. Ex- Class

ii)     Function overloading - Single function name can be used to handle different numbers and different type of arguments i.e. single function name can perform different types of task.

                                                                                Shape 
                                                                               --------
                                                                                Draw()
                                                                                  ⬇
                                                                                  ↓
                                                                                  ⬇
                                      -----------------                     --------------                    --------------------
                                        Circle object                         Box object                        Triangle object
                                      -----------------                     --------------                    --------------------
                                         Draw(Circle)                          Draw(box)                         Draw(Triangle)
                                      -----------------                     --------------                    --------------------

Dynamic binding - Binding refers to linking of the procedure called to the code to be executed in respond to the call. It is also known as late binding means that code associated with the given procedure call is not known until the time of call at runtime. 

Message passing - Object oriented program consist of set of object that communicate with each other, basic steps are - 
i)      creating classes that define object and behaviour
ii)     Creating object on class definition.
iii)    Establising communication among object.

A message for an object is request of execution of a procedure which will invoke a function in the preceiding object that generate a desired result. It involves the name of the object, name of function and the info to be sent. 

Inheritance - It is the process by which new classes called derived classes are created from existing class called base class. The derived class has all the features of the base class and the programmer can choose to add new features specifically to the newly created derived classes. The idea of inheritance implements "is a relationship". For example - Mammal IS A animal, Dog IS A mammal. Hence, Dog IS A animal.

Features or advantages of Inheritance - 
i)      Reusability of code 
ii)     Saves time and effort
iii)    Faster Development, easier maintanance and easy to extent and maintain
iv)     Capable of expressing the inheritance relationship and its transitive nature which ensures loseness with real world problems.

Capable of expressing the en and its transitivive nature which ensures closesness with real world problems - 

Access control and Inheritance - A dereived class can access all the protected and public members of its base class. It cannot access the private member of the base class.

        Public 
        ------------                    ➡️➡️ can be inherited by the class class
        Protected 
        ------------
        Private                         ➡️➡️ cannot be inherited by the child class

        Members of the base class     ➡️➡️     Private                          Protected                                             Public
        \\\\\\\\\\\\\\\\\\\\\\\\\          
        Inheritance type

                ⬇️
                ⬇️
        
        Private                               Not Inherited         Becomes private to child class                      Becomes private to child class

        Protected                             Not Inherited         Becomes protected members of child class            Becomes protected members of child class

        Public                                Not Inherited         Becomes protected members of child class            Becomes public members of child class

Types of Inheritance - 

        A                                                       A                 B                                                             A               C)Hierarchical
       ⬇️       a) Single Inheritance                          ⬇️               ⬇️           b)Multiple Inheritance                           ⬇️                   Inheritance
        B                                                       ➡️➡️➡️ ⬇️ ⬅️⬅️⬅️                                                ⬇️⬅️⬅️⬅️⬅⬇️➡️➡️➡️➡️⬇️        
                                                                        ⬇️                                                         ⬇️         ⬇️          ⬇️
                                                                         C                                                          B           C           D

        A                                                               A
       ⬇️                                                      ⬅️⬅️⬅️  ➡️➡️➡️
        B       d) Multilevel Inheritance                       B               C              e) Hybrid Inheritence
       ⬇️                                                      ➡️➡️➡️⬇️⬅️⬅️⬅️
        C                                                               D

Multiple Inheritance - Syntax

        class Base1:
                statement block
        class Base2:
                statement block
        class Derived (Base1, Base2):
                statement block

Multi-Level Inheritance - Syntax

        class Base:
                pass
        class Derived1(Base)
                pass
        class Derived2(Derived1)
                Pass

Multi-path Inheritance - 

Polymorphism and Method Overriding - Poly. enables the prograammer to assign different meanings or usage to a variable, function or an object in different context. It is related to methods, it is also applied to function or methods depending on the given parameters, particular form of function that can be selected for excecution. In python, Method Overriding is one of the way to implement poly. 



#  Exception Handling


Error and exception handling - The program when behaves abnormaly or unexpectedly this event is turned as an error. The common types of error are 
i)      Syntax Error - They occur when the programmer violates the rule of any programming languange.
ii)     Logical error - Due to poor understanding of a problem and its solution. It specifies all types of errors in which the program executes but gives incorrect results. It may occur due to wrong algorithm or logic. The logical error sometimes leaves to a runtime error which causes the program to terminate abruptly. These types of runtime errors are known as exceptional. 

The Exceptions are categorised as 
i)      Synchronous like /0, arrays index of bond, etc. after can be controlled by the program.
ii)     Asynchronous like an interuption from the keyboard or hardware malfunction or disk failure are caused by events that are beyound the control of the program.

An "execption" is an event which occurs during excecusion of the program and disrupt the normal flow of the program instruction. When a program encounters a situation it cannot with it raaises an exception. Hence, exception is a python object which represents an error. When a program raises an "exception" it must handle the exception or the program will be immediately terminated. The exception in a program is handled usin "try block and except block". A critical operation which can raise exception is placed inside the try block and the code that handle exception is written in except block. 

The syntax for try and except block is - 
try:
        statements
except ExceptionName:
        statements

        Exception raised     ➡️     If NO     ➡️     Program excecutes normally
                ⬇
        If YES  ⬇
                ⬇
        Handler found?     ➡️     If NO     ➡️     The prgram is terminated and an error message is displayed
                ⬇
        IF YES  ⬇
                ⬇
        Program control is trasferred to handler

Multiple Accept block - Python allows multiple Accept blocks for a single try block, a try block can be asscoiated with more than one except block for multiple exception however only one exception will be executed. Exception handler will only handle exception with occurs with correspondence try block

try:
        operation are done in this block.
        ---------------------------------------------------
except Exception1:
        If there is Exception1, then execute this block.
except Exception2:
        If there is Exception2, then execute this block.
        ---------------------------------------------------

Except block with Exception - Except block can be specified without mentioning an exception such type of excpet block if present should be the last one which would act as a wild card. Sometimes it is difficult to anticipate all types of exception in a large software. Therefore programmer may not be able to write difeerent handler(except block) for every individual type of exception. In such a situation it would be better to write a handler that would catch all types of exception. 

Raising Exception - An exception can be raised delibaretly using the keywoard raise. 
General syntax for raise in 

raise[Exception[], args[], traceback[]]

Exception - It is the name of exception to be raised for ex - TypeError.

Args - Optional and specifies the value for the exception arguments If args is not specified then exception args is none.

Traceback - It is also optional and if present and traceback for objective used for the exception.

Instantiating Exception - Python allows programmer to instantiate an exception first before raising it and at any attribute to it as desire. These attribute can be used for additional information about the errors. To instantiate the exception an accept block will specify a variable after the exception name., the variable then becomes an exception instance with the argumnets showed in instance.args. The exception instance also has the string method (__str__()method) define so that the argument can be printed directly without using instance.args.

Handling exception in Invoked function - 

Syntax:
        function_name(arg list):
        ---------
        ---------
        try:
                ------------
                function_name()
                ------------
        except  ExcecptionName:
                ------------
                Code to handle exception
                ------------

        Throw point 
        Invoke a function that generate an exception
                        ⬇
                        ⬇
                        ⬇
        Try block
                        ⬇
                        ⬇
                        ⬇
        Except block


The finally block - The try block has another optional block call finally which is use to define clean up action which must be executed under all circumstances. The finally block is always executed before leaving the try block. This means that the statement written in finally block are executed irrespective of whether an exception has occured or not. 

Syntax:
        try:
                Write your operations here
                ----------
                Due to exception, operations written here will be skipped
        finally:
                This would be executed.
                ----------

Pre-Defined clean-up action - In python some object define standard clean-up action that are automatically performed when the object is no longer needed. The default clean-up is performed irrespective of whether the operation of using the object succeded or failed. For ex- Operation in file handling, the file is prefer to open "with" keywoard,` so that file is automatically closed when not in use. If the programmer forgets to close the file or the code to close it is skipped because of an exception the file will still be closed.

Assertion in Python - An assertion is a basic check that can be turned on or off when the program is being tested. Using the assert statement an expression is tested and if the result of the expression is false then an exception is raised. Assert statement is intended for debugging statements. It can be seen as abbreviated notion for conditional raised statemnt. In python assertion is implemented using assert statement. It is usually placed at the start of the function to check for valid input and after the function is called it checks for a valid output. When python encounters assert statement exception associated with it is calculated and if the expression is false "assertion error is rasied". 

Syntax -
assert expression[args]

Assertion error exception can be caught and handled like any other exception using try-except block. 

# NumPy

It is an open-source numerical library used for working with mathematical function with multi-dimensional array and matrix data structure. It is commanly used in working with 
Numpy stands for numerical python.

Uses of NumPy:-
        NumPy array uses less memory than normal python list. A normal python list is book of pointers to seperate python object. A NumPy array is designed to be an array of uniform values without using extra memory space for type pointers. This makes it much more efficient and actual use a lot less memory than the normal python list. NumPy can also read read information faster than python array and has lots of convinient broadcasting operation that can be performed across array dimensions.