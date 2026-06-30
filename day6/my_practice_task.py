Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> TASK A : Data Extraction (slicing)
SyntaxError: invalid syntax
>>> #TASK A : Data Extraction (slicing)
>>> 
>>> raw_data = "INFO-SEMICONDUCTOR-8459"
>>> # SEMICONDUCTOR using +ive slcing
>>> raw_data[5:18]
'SEMICONDUCTOR'
>>> 
>>> # 8459 using -ive indexing
>>> raw_data[-4:-1] # last letter 9 missed
'845'
>>> raw_data[-4:] # correct way
'8459'
>>> 
>>> # TASK 2 : The decoder(Striding & Indexing)
>>> secret_code = "cdoepmupteirn g"
>>> 
>>> # extracting code word using stride 2
>>> secret_code[::2]
'coputing'
>>> # reverse string using -ive indexing
>>> secret_code[-1::-1]
'g nrietpumpeodc'
