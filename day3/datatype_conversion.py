Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# datatype conversion : TYPECASTING
# int()
int(9)
9
int(89.08)
89
int("dfdgf")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("dfdgf")
ValueError: invalid literal for int() with base 10: 'dfdgf'
int(5+6j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(False)
0
int(True)
1

# float()
float(45)
45.0
float(45.78)
45.78
float(4+5j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

float("abc")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float("abc")
ValueError: could not convert string to float: 'abc'


# str()
str(1)
'1'
str('76.89')
'76.89'
str("hello")
'hello'
>>> str(5+6j)
'(5+6j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> 
>>> # complex()
>>> complex(5)
(5+0j)
>>> complex(5.6)
(5.6+0j)
>>> complex(5+98j)
(5+98j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> 
>>> # bool()
>>> bool(5)
True
>>> bool(9.8)
True
>>> bool("hello")
True
>>> bool(4+6j)
True
>>> bool(True)
True
>>> bool(False)
False
