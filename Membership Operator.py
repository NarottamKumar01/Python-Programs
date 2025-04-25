Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="abcd"
>>> "a" in x
True
>>> e in x
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    e in x
NameError: name 'e' is not defined
>>> "d" not in x
False
>>> d in x
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d in x
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> "d" in x
True
>>> "A" not in x
True
>>> x=256
>>> 5 in x
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    5 in x
TypeError: argument of type 'int' is not iterable
>>> x=[10,20,30]
>>> 20 in x
True
>>> =1,2,3,4
SyntaxError: invalid syntax
>>> x=1,2,3,4
>>> 4 in x
True
>>> x="Mysirg.com"
>>> "My" in x
True
