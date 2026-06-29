Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# indexing
word = "vishakapatnam"
# +ive indexing
word[0]
'v'
word[1]
'i'
# get first 6  letters since starting frm 0 : 0 to 5 indices
word[0] + word[1] + word[2] + word[3] + word[4] + word[5]
'vishak'
sentence = "I am learning Python."
# space also consumes a character, so space also counted in indexing
sentence[0]
'I'
sentence[1]
' '
# getting 'am'
sentence[2] + sentence[3]
'am'
# getting 'learning' using CONCATENATION (+)
sentence[5] + sentence[6] + sentence[7] + sentence[8] + sentence[9] + sentence[10] + sentence[11] + sentence[12]
'learning'
# simple task given by ma'am
a = 'simple is better than complex'
# 'better'
>>> a[9] + a[10] + a[11] + a[12] + a[13] + a[14]
' bette'
>>> a[9] + a[10] + a[11] + a[12] + a[13] + a[14] + a[15]
' better'
>>> # 'simple'
>>> a[0] + a[1] + a[2] + a[3] + a[4] + a[5]
'simple'
>>> # 'complex'
>>> a[22] + a[23] + a[24] + a[25] + a[26] + a[27] + a[28]
'complex'
>>> b = 'codegnan it solutions'
>>> # 'codegnan'
>>> b[0] + b[1] + b[2] + b[3] + b[4] + b[5]+ b[6]+ b[7]
'codegnan'
>>> # 'solutions'
>>> b[11] + b[12] + b[13] + b[14] + b[15] + b[16]+ b[17]+ b[18] + b[19]
' solution'
>>> b[12] + b[13] + b[14] + b[15] + b[16]+ b[17]+ b[18] + b[19] + b[20]
'solutions'
>>> 
>>> # ive indexing
>>> a = 'I am learning Python'
>>> #'learn'
>>> a[-15] + a[-14] + a[-13] + a[-12] + a[-11]
'learn'
>>> # 'python'
>>> # task given by mam
>>> a = 'python fullstack
SyntaxError: unterminated string literal (detected at line 1)
>>> a = 'python fullstack'
>>> # 'full'
>>> a[-9] + a[-8] + a[-7] + a[-6]
'full'
>>> # 'stack'
>>> a[-5] + a[-4] + a[-3] + a[-2] + a[-1]
'stack'
>>> # 'python'
>>> a[-16] + a[-15] + a[-14] + a[-13] + a[-12] + a[-11]
'python'
