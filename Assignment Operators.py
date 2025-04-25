Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=4
>>> 4=x
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 3=4
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> y=y+3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    y=y+3
NameError: name 'y' is not defined
>>> x=5
>>> x+=3
>>> x
8
>>> x/=2
>>> x
4.0
>>> x=5
>>> x*=3+4
>>> x
35
>>> x=x*3+4
>>> x
109
>>> 35
35
>>> 
>>> x=5
>>> x=x*3+4
>>> x
19
