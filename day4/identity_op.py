Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # identity/ identify operators
>>> a = 50
>>> type(a) is int
True
>>> type(a) is not float
True
>>> b = 3.14
>>> type(b) is float
True
>>> type(b) is not float
False
>>> c = 4+5j
>>> type(c) is not complex
False
>>> type(c) is complex
True
>>> d = "hello"
>>> type(d) is not str
False
>>> typpe(d) is str
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    typpe(d) is str
NameError: name 'typpe' is not defined. Did you mean: 'type'?
>>> type(d) is str
True
>>> e = True
>>> type(e) is not bool
False
>>> type(e) is bool
True
