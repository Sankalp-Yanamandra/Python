Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# .isupper()
a='python'
a.isupper()
False
# .islower()

a.islower()
True
# .isalpha()
a.isalpha()
True
b = 'python course'
# .isalpha() : false since space
b.isalpha()
False
b = 'pythoncourse'
b.isalpha()
True
# .isdigit()
d = 1234
# not a string, so error
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> d = '1234'
>>> d.isdigit()
True
>>> # isalnum()
>>> a.isalnum()
True
>>> e = 'pooja1234'
>>> e.isalnum()
True
>>> f = 'abc@123'
>>> # isalnum() : false since spl char : @
>>> f.isalnum()
False
>>> 
>>> 
>>> # .startswith(substr)
>>> a ='java'
>>> a.startswith('p')
False
>>> a.endswith('a')
True
>>> 
>>> 
>>> # strip : remove whitepaces
>>> a = '   hello world   '
>>> a.strip()
'hello world'
>>> # remove only on left side
>>> a = '   hello  world   '
>>> a.lstrip()
'hello  world   '
>>> # remove only on right side
>>> a = '    hello   world    '
>>> a.rstrip()
'    hello   world'
