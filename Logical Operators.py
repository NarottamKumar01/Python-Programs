Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
3>4 and 5>>3
False
3>2 and 5>1
True
3!=4 and 10<20
True
4>3 or 3<2
True
5 and 4
4
0 and 4
0
3 or 4
3
0 or5
SyntaxError: invalid syntax
0 or 5
5
not 4>3
False
>>> not 5
False
>>> not 0
True
>>> not "narottam"
False
>>> not ''
True
>>> 'ram' and 'shyam'
'shyam'
>>> not 'ram' and 'shyam'
False
>>> 'ram' or 'shyam'
'ram'
>>> 3 and 4>2
True
>>> 3 and 3+4
7
>>> 3 and x=4
SyntaxError: cannot assign to expression
>>> 5/0
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    5/0
ZeroDivisionError: division by zero
>>> 3 or 5/0
3
>>> 3
3
>>> 
>>> 3 and 5/0
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    3 and 5/0
ZeroDivisionError: division by zero
>>> ZeroDivisionError: division by zero
SyntaxError: invalid syntax
>>> 
>>> 3 and 10/0
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    3 and 10/0
ZeroDivisionError: division by zero
>>> 3 and 10/2
5.0
