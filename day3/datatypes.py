Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# day 3 : datatypes
# type(var_name) = returns data type of variable

a=10
type(a)
<class 'int'>
b=5.6
>>> type(b)
<class 'float'>
>>> c='hello'
>>> type(c)
<class 'str'>
>>> d="hello"
>>> type(d)
<class 'str'>
>>> e='''hello'''
>>> type(e)
<class 'str'>
>>> valid=True
>>> type(valid)
<class 'bool'>
>>> valid=False
>>> type(valid)
<class 'bool'>
>>> # must be True or False since keywords, else error or a string
>>> f = true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    f = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> f = "True"
>>> type(f)
<class 'str'>
>>> num = 4+7j
>>> type(num)
<class 'complex'>
>>> num = 56j
>>> type(num)
<class 'complex'>
>>> # can't use i or some other letter in place of j (for iota)
>>> h=5+6i
SyntaxError: invalid decimal literal
>>> # only real part : considered as int or float
>>> i=56
>>> type(i)
<class 'int'>
