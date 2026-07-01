Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # concatenation +
>>> a='code'
>>> b='gnan'
>>> print(a+b)
codegnan
>>> a='python'
>>> b='course'
>>> print(a+' '+b)
python course
>>> 
>>> # usecase : print first name and last name of a person
>>> fname = 'john'
>>> lname = 'mattews'
>>> # together without spaces
>>> print(fname + lname)
johnmattews
>>> # want space
>>> print(fname + " " + lname)
john mattews
>>> # want 1st letter of each word caps
>>> print(fname.title() + ' ' + lname.title())
John Mattews
>>> # better way
>>> print( (fname + ' ' + lname).title() )
John Mattews
