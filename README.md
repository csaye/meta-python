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
- user input
- simple methods

### Limitations:
- whitespace required around expression elements
- multiple inline statements not supported
- compound boolean statements not supported

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
i = 0
while i < 10:
    print('Hello World') # prints 'Hello World' 10 times
    i += 1
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
```py
i = 2
while i < 100: # prints primes up to 100
    prime = 1
    upper = i ** 0.5 + 1
    j = 2
    while j < upper:
        if i % j == 0:
            prime = 0
        j += 1
    if prime == 1:
        print(i)
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
