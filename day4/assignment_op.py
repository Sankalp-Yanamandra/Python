Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # assignment
>>> a=10; b=20
>>> a
10
>>> b
20
>>> # a op= b => a =  a op b
>>> b += a
>>> b
30
>>> b -= a
>>> b
20
>>> b *= a
>>> b
200
>>> b **= a
>>> b
102400000000000000000000
>>> b /= a
>>> b
1.024e+22
>>> b // = a
SyntaxError: invalid syntax
>>> b //= a
>>> b
1.024e+21
>>> b %= a
>>> b
0.0
