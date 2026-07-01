Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # formatting
>>> a=3
>>> b=24
>>> print(a+b)
27
>>> # more user friendly
>>> print('sum of',a,'and',b,'=',a+b)
sum of 3 and 24 = 27
>>> city='moscow'
>>> print('I live in',city)
I live in moscow
>>> 
>>> # format() method
>>> guy1 = 'motu'
>>> guy2 = 'patlu'
>>> print('we are {}{}'.format(a,b))
we are 324
>>> print('we are {}{}'.format(guy1,guy2))
we are motupatlu
>>> # want space
>>> print('we are {} {}'.format(guy1, guy2))
we are motu patlu
>>> # want separately
>>> print("I am {}, I am {}".format(guy1, guy2))
I am motu, I am patlu
>>> 
>>> 
>>> # f-strings
>>> a='daniel'
>>> b = 'craig'
>>> print(f'We are {a}{b}')
We are danielcraig
>>> print(f'we are {a} {b}')
we are daniel craig
>>> print(f'I am {a}, and I am {b}')
I am daniel, and I am craig
