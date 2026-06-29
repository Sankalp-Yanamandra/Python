Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # my practice task
>>> # 1. product name, price, discount percent
>>> product_name, price, discount_pcent  = "SandalWood body wash", 343.89, 40
>>> # check values once
>>> print(product_name, price, discount_pcent)
SandalWood body wash 343.89 40
>>> # 2. final price = price - discounted_amt
>>> discounted_amt = price * (discount_pcent/100)
>>> # check value of discounted_amt value
>>> print(discounted_amt)
137.556
>>> # calculating the final price
>>> final_price = price - discounted_amt
>>> # check final price
>>> print(final_price)
206.33399999999997
>>> # 3. print final output
>>> # before that final price must not contain any decimals
>>> truncated_final_price = int(final_price)
>>> # check value
>>> print(truncated_final_price)
206
>>> # 3. final o/p
>>> print(f'{product_name} : ₹{truncated_final_price}')
SandalWood body wash : ₹206
