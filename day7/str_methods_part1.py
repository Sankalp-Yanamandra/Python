Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# STRING METHODS

# 1. len() : returns no of char in the string
a = 'python'
len(a)
6
b='machine learning'
len(b)
16
# empty string => len = 0
c=''
len(c)
0
# space also counted in len
c = ' '
len(c)
1

# 2. strname.count(substr) : returns freq of occurrence of a character/word i.e. substring
a='twinkle twinkle little star'
# its a string method Not a built-in mtd
count('twinkle')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    count('twinkle')
NameError: name 'count' is not defined. Did you mean: 'round'?
# must be associated with a string
a.count('twinkle')
2
a.count('k')
2
a.count('t')
5
a.count(' ') # count no of spaces
3
b = 'twinkletwinkle'
b.count('twinkle')
2
b.count('twinkletwinkle')
1
c = 'twinkle.twinkle'
c.count('twinkle.twinkle')
1
c.count('twinkle')
2


# 3. find a substr => returns 1st occurrence if found, else -1
a = 'python'
a[2]
't'
# get index of t
a.find('t')
2
a.find('tho') # finding a grp of letters
2
# returns starting index of that grp
a.find('n')
5
b='hello'
b.find('l') # reutrns 1st occurennce
2
# get 2 occurrences using slicing
b[2:4]
'll'



# esscape sequence : backslash \n, \t


a = 'name:mary joseph\nmobileno:102030405967\t\temail:abc@yahoo.com\n\ncllg:ABC cllg\tbranch:IT"
SyntaxError: unterminated string literal (detected at line 1)
a = 'name:mary joseph\nmobileno:102030405967\t\temail:abc@yahoo.com\n\ncllg:ABC cllg\tbranch:IT'
print(a)
name:mary joseph
mobileno:102030405967		email:abc@yahoo.com

cllg:ABC cllg	branch:IT
>>> 
>>> 
>>> # 4. strname.replace()
>>> 
>>> a='I love java'
>>> a.replace('java', 'python')
'I love python'
>>> a = 'wait until you succeed.'
>>> a.replace('wait', 'work')
'work until you succeed.'
>>> 
>>> 
>>> # 5. .upper(), .lower(), .capitalize(), .title()
>>> a='hello'
>>> a.upper()
'HELLO'
>>> b='Hi'
>>> b.lower()
'hi'
>>> c='python'
>>> # want 1st letter caps
>>> c.upper('p')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    c.upper('p')
TypeError: str.upper() takes no arguments (1 given)
>>> c[0].upper() # only gives 1st letter, not right
'P'
>>> c.capitalize()
'Python'
>>> # want 1st letter of all words caps
>>> d = 'i am in class'
>>> d.title()
'I Am In Class'
>>> # v/s .capitalize()
>>> d.capitalize()
'I am in class'
