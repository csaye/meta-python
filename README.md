# meta-python

Python written in Python.

Input file is `Input.py`.

## RigidInterpreter.py

Makes assumptions about program styling for compiling simplicity.

### Functionality:
- value printing
- variable assignment and modification
- simple if/else statements
- simple while statements

### Limitations:
- whitespace required around expression elements
- multiple inline statements not supported

### Examples

```py
print('Hello World') # prints 'Hello World'
```
```py
print('He' + 'l' * 2 + 'o World') # prints 'Hello World'
```
```py
print(3 + 4 * (5 - 2)) # prints '15'
```
```py
a = 'Hello World'
b = a
print(b) # prints 'Hello World'
```
```py
a = 3
b = a - 1
c = b * 2
a += b * c
print(a) # prints '11'
```
```py
if 1 < 2:
    print('Hello') # prints 'Hello'
if 1 > 2:
    print('World')
```
```py
i = 0
while i < 10:
    print('Hello World') # prints 'Hello World' 10 times
    i += 1
```
```py
if 1 < 2:
    print('True') # prints 'True'
    if 1 > 2:
        print('False')
    else:
        print('True') # prints 'True'
else:
    print('False')
```
```py
i = 1
while i <= 100: # prints FizzBuzz up to 100
    string = ''
    if i % 3 == 0:
        string += 'Fizz'
    if i % 5 == 0:
        string += 'Buzz'
    if string == '':
        print(i)
    else:
        print(string)
    i += 1
```

## Interpreter.py

Attempts to clone functionality exactly, adhering to stylistic flexibility.

### Functionality:
- value printing
- variable assignment
- parses stray whitespace correctly
- parses inline statements

### Examples
```py
print ( 'Hello World' ) # extra whitespace
```
```py
a = 0; b = 0 # inline statements
```
```py
print(1+2+3) # expression without whitespace
```
