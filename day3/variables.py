Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# day 3 : Variables
print(3+8)
11
a=10
print(a)
10
b=20
print(b)
20
# case-senstive
x=10
print(X)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
10
# can't assign a value to another value
3=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3 = 10
print(a3)
10
# can't start with no
3s=10
SyntaxError: invalid decimal literal
b23423=40
print(b23423)
40
# except _, no other spl char allowed
$=70
SyntaxError: invalid syntax
df$f = 400
SyntaxError: invalid syntax
dffd_sdgt = 100
print(dffd_sdgt)
100
_ = 200
print(_)
200
# whitespacce not allowed
 =550
 
SyntaxError: unexpected indent
# cn't use a keyword
return = 49
SyntaxError: invalid syntax
# initializing >1 variables
a=10,b=90
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=10;b=90
print(a,b)
10 90
# another way instead of ;
a,b=10,90
print(a,b)
10 90
# Can we assign >1 value to a single var ? Yes, stored as TUPLE
age = 10,20,30
print(age)
(10, 20, 30)
# can we assign 1 value to >1 var ?
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
# right way
a=b=c=10
print(a,b,c)
10 10 10
# muliple value to multiple var ? Yes, ensure count remains same
a,b,b = (10,20,30)
print(a,b)
10 30
# above is called : TUPLE UNPACKING
# below not allowed, since count not mtching
A,B,C = 10,20,30,40,50,60,70
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    A,B,C = 10,20,30,40,50,60,70
ValueError: too many values to unpack (expected 3)
# instead of space use _ btwn >1 words
first name = "amy"
SyntaxError: invalid syntax
first_name = "amy"
>>> print(first_name)
amy
>>> firstname = "amy"
>>> print(firstname)
amy
>>> # string concatenation
>>> fname="amy"
>>> lname="jackson"
>>> print(fname + " " + lname)
amy jackson
>>> print(fname, lname)
amy jackson
>>> # var name can be > 1 letter
>>> name = "arun"
>>> age=56
>>> print(name, age)
arun 56
>>> # string : any character enclosed btwn "" or '' => can't be a variable
>>> address = "bglr"
>>> print(address)
bglr
>>> print("address")
address
>>> # del keyword -> to delete var from memory n deallocate memory assigned to this var
>>> del address
>>> print(address)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(address)
NameError: name 'address' is not defined
>>> # case-sensitive
>>> CITY = "surat"
>>> print(CITY)
surat
>>> City = "manipal"
>>> city = "delhi"
>>> print(CITY, City, city)
surat manipal delhi
