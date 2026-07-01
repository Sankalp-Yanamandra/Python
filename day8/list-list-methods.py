Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# data types
# 1. list[] : mutable
a = ['a', 10, 45.67,True]
print(a)
['a', 10, 45.67, True]
type(a)
<class 'list'>

# list methods
# 1. .append(ele)
lang = ['python','C', 'java']
print(lang)
['python', 'C', 'java']
lang.append('C#')
print(lang)
['python', 'C', 'java', 'C#']
# can only add 1 at a time
lang.append('Php','html')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    lang.append('Php','html')
TypeError: list.append() takes exactly one argument (2 given)
lang.append(['php','html'])
print(lang)
['python', 'C', 'java', 'C#', ['php', 'html']]
# 2. .extend() : >= 1 at end
lang.extend('css','javascript')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    lang.extend('css','javascript')
TypeError: list.extend() takes exactly one argument (2 given)
lang.extend(['css','javascript'])
print(lang)
['python', 'C', 'java', 'C#', ['php', 'html'], 'css', 'javascript']

# 3. .insert() : insert at a posn/index
lang.insert(1, 'Go')
print(lang)
['python', 'Go', 'C', 'java', 'C#', ['php', 'html'], 'css', 'javascript']
# go  inserted at index 1 above


# 4. .sort()
# if strings => default : sorted lexicograpically frm lowest to highest
lang.sort()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lang.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
lang.sort()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    lang.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
a = ['app', 'server', 'browser', 'web-app']
a.sort()
print(a)
['app', 'browser', 'server', 'web-app']
# numbers : ascending order default
b = [10, 560, 245, 12]

b.sort()

print(b)
[10, 12, 245, 560]


# 5. .reverse()
a.reverse()
print(a)
['web-app', 'server', 'browser', 'app']
print(b)
[10, 12, 245, 560]
b.reverse()
print(b)
[560, 245, 12, 10]


# 6. .pop()
# default : delete frm last
print(lang)
['C', 'C#', 'Go', 'java', 'python', ['php', 'html'], 'css', 'javascript']
lang.pop() # javascript
'javascript'
print(lang)
['C', 'C#', 'Go', 'java', 'python', ['php', 'html'], 'css']
# by index,
lang.pop(1)
'C#'
print(lang)
['C', 'Go', 'java', 'python', ['php', 'html'], 'css']


# 7. .remove()
# delete by ele_name : 1st occurrence only
lang.remove('Go')
>>> print(lang)
['C', 'java', 'python', ['php', 'html'], 'css']
>>> lang.remove(['php', 'html'])
>>> print(lang)
['C', 'java', 'python', 'css']
>>> 
>>> 
>>> # 8. .copy() : shallow copy
>>> a = [10, 20, 30]
>>> b = a.copy()
>>> print(a, b)
[10, 20, 30] [10, 20, 30]
>>> # change in one, reflected in other : shallow copy
>>> b.append(40)
>>> print(a, b)
[10, 20, 30] [10, 20, 30, 40]

>>> # 9. .clear()
>>> b.clear()
>>> print(b)
[]
>>> 
>>> # 10. len() and 11. .count()
>>> print(a)
[10, 20, 30]
>>> len(a)
3
>>> a.count(20)
1
>>> 
>>> # shallow copy()
>>> b = a.copy()
>>> print(a, b)
[10, 20, 30] [10, 20, 30]
>>> # inside ele : shallow copy
>>> b.pop(1)
20
>>> print(a, b)
[10, 20, 30] [10, 30]
