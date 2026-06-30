Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # negative striding
>>> a = "python course"
>>> a[-1:-11:-3]
'eu h'
>>> 
>>> a[-2:-12:-4]
'sch'
>>> 
>>> a[-5:-13:-5]
'oh'
>>> 
>>> # empty string => for + striding => startingindex < endingindex
>>> a[8:4:2]
''
>>> a[4:8:2]
'o '
>>> 
>>> # empty string => for - striding => startingindex > endingindex
>>> a[-9:-3:-1]
''
>>> a[-3:-9:-1]
'ruoc n'
>>> 
>>> # reverse of string
>>> a[::-1]
'esruoc nohtyp'
