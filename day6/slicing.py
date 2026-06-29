Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# slicing : getting a part from whole eg. in strings
a ='time is very precious'
a[8:12]# 12 not included
'very'
a[13:] # 13 to end
'precious'
a[:4] # starting to (4-1) = 3
'time'

b = 'work until you succeed'
>>> b[14:]
' succeed'
>>> b[15:]
'succeed'
>>> b[5:10]
'until'
>>> b[:4]
'work'
>>> b[11:14]
'you'
>>> 
>>> 
>>> c = 'vizag is city of destiny'
>>> c[-15:-11:-1]
''
>>> c[-15:-11]
'city'
>>> c[-7:]
'destiny'
>>> c[:-19]
'vizag'
>>> 
>>> d = 'hi hello how are you'
>>> a[:-18]
'tim'
>>> d[:-18]
'hi'
>>> d[-17:-12]
'hello'
>>> d[-11:-8]
'how'
>>> d[-7:-4]
'are'
>>> d[-3:0]
''
>>> d[-3:]
'you'
>>> d[-3:-1]
'yo'
