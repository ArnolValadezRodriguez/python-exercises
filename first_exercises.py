 type(99.9)
<class 'float'>
>>> type("False")
<class 'str'>
>>> type(False)
<class 'bool'>
>>> type('0')
<class 'str'>
>>> type(0)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type("True")
<class 'str'>
>>> type([{}])
<class 'list'>
>>> type({'a': []})
<class 'dict'>

# What data type would best represent:

# - A term or phrase typed into a search box?
string
# - If a user is logged in?
boolean
# - A discount amount to apply to a user's shopping cart?
float
# - Whether or not a coupon code is valid?
boolean
# - An email address typed into a registration form?
dictionary or list
# - The price of a product?
float
# - A Matrix?
list
# - The email addresses collected from a registration form?
dictionary or list
# - Information about applicants to Codeup's data science program?
list? 

>>> '1' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 6 % 4
2
>>> type(6 % 4)
<class 'int'>
>>> type(type(6 % 4))
<class 'type'>
>>> '3 + 4 is ' + 3 + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 0 < 0
False
>>> 'False' == False
False
>>> True == 'True'
False
>>> 5 >= -5
True
>>> True or "42"
True
>>> 6 % 5
1
>>> 5 < 4 and 1 == 1
False
>>> 'codeup' == 'codeup' and 'codeup' == 'Codeup'
False
>>> 4 >= 0 and 1 !== '1'
  File "<stdin>", line 1
    4 >= 0 and 1 !== '1'
                   ^
SyntaxError: invalid syntax
>>> 6 % 3 == 0
True
>>> 5 % 2 != 0
True
>>> [1] + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
>>> [1] + [2]
[1, 2]
>>> [1] * 2
[1, 1]
>>> [1] * [2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'list'
>>> [] + [] == []
True
>>> {} + {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'