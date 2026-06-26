Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# bitwsie op
# & 1&1 = 1, rest all 0
a=5;b=7
bin(5);bin(7)
'0b101'
'0b111'
a&b
5
a=2;b=4
bin(2);bin(4)
'0b10'
'0b100'
a&b
0

# | => 0|1=0;1|0=0;1|1=0;0|0 apply on each pair of corresponding bit of both a and b
a=5;b=7
bin(5);bin(7)
'0b101'
'0b111'
a|b
7
a=2;b=4
bin(2);bin(4)
'0b10'
'0b100'
a|b
6
bin(6)
'0b110'

# ~a == -(a+1)
a=6
~a
-7
a = -7
~a
6


# ^(bitwise xor); odd no of 1s = 1 ; even no of 1s = 0
a=4
b=5
bin(4);bin(5)
'0b100'
'0b101'
a^b # should give 0001 i.e 1
1
a=5
b=7
bin(5);bin(7)
'0b101'
'0b111'
a^b # should give 0010 i.e. 2
2


>>> # left shift (<<) : shift bits by x and append 0s at right end
>>> a = 6
>>> bin(a)
'0b110'
>>> a << 3 # shift bits by 3 places n append 0s at right end
48
>>> bin(a)
'0b110'
>>> a <<= 3
>>> bin(a)
'0b110000'
>>> a = 5
>>> bin(a)
'0b101'
>>> a <<= 3
>>> bin(a)
'0b101000'
>>> a
40
>>> 
>>> 
>>> # right shift (>>) : shift bits by x places right, append 0s at left end
>>> 
>>> a= 2
>>> bin(a)
'0b10'
>>> a = a >> 2 # should give  000 i.e.0
>>> a
0
>>> bin(a)
'0b0'
>>> a = 6
>>> bin(a)
'0b110'
>>> a >>= 1 # should give 0011 i.e. 3
>>> bin(a)
'0b11'
>>> a
3
