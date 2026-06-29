Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# striding

a = 'data science'
a[::]
'data science'
a[::1]
'data science'
>>> a[::-1]
'ecneics atad'
>>> # above is reverse of string
>>> # now inc bby 2
>>> a[::2]
'dt cec'
>>> # now dec by 2 i.e. frm end
>>> a[::-2]
'enisaa'
>>> 
>>> # task by ma'am
>>> A =  'machine learning'
>>> A[::5]
'mnag'
>>> A[::7]
'm n'
>>> A[::2]
'mcielann'
>>> A[::4]
'miln'
>>> A[3:11]
'hine lea'
>>> A[:8]
'machine '
>>> A[9:]
'earning'
>>> A[::10]
'ma'
>>> 
>>> 
>>> B = "cloud computing"
>>> B[2:13:3]
'o mt'
>>> B[6:14:4]
'cu'
>>> B[5:12:2]
' opt'
>>> B[3:9:5]
'um'
