print('Write two numbers and I\'ll print all numbers between them including yours.')
a = int(input ('First number: '))
print('***Remember that second number must be bigger or equal to first.***')
b = int(input ('Second number: '))
print('My answer is:')

c = [i for i in range(a,b+1)]
print(c)
