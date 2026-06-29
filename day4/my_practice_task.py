Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # my practice task for day 4
>>> 
>>> # creating a tuple of authorized users
>>> users = 101,102,103,104
>>> # check tuple
>>> print(users)
(101, 102, 103, 104)
>>> # 2. current user
>>> current_user = 105
>>> # 3. check if valid user
>>> print(current_user in users)
False
>>> # 4. verify if uer's ID follows certain condtions
>>> print(current_user > 100 and current_user != 102)
True
