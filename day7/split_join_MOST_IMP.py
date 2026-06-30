Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # split() : string to list
>>> 
>>> lang = 'python C java'
>>> lang.split()
['python', 'C', 'java']
>>> lang.split(',')
['python C java']
>>> b = 'I am in class 10'
>>> b.split()
['I', 'am', 'in', 'class', '10']
>>> ['I', 'am', 'in', 'class', '10']
['I', 'am', 'in', 'class', '10']
>>> 
>>> # join()
>>> b = 'vja', 'hyd', 'vzg'
>>> ''.join(b)
'vjahydvzg'
>>> ' '.join(b)
'vja hyd vzg'
>>> 'k'.join(b)
'vjakhydkvzg'
>>> c='python'
>>> 'k'.join(c) # while joining, separte using k
'pkyktkhkokn'
>>> v = [abc, bcd, cda]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    v = [abc, bcd, cda]
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
>>> v = [10,20,30]
>>> ''.join(v)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ''.join(v)
TypeError: sequence item 0: expected str instance, int found
>>> v = ['a', 'b', 'c']
''.join(v)
'abc'
','.join(v)
'a,b,c'
