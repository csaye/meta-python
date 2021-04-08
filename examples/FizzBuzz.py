i = 1
while i <= 100: # prints FizzBuzz up to 100
    string = ''
    if i % 3 == 0:
        string += 'Fizz'
    if i % 5 == 0:
        string += 'Buzz'
    if string == '':
        print(i)
    if string != '':
        print(string)
    i += 1
