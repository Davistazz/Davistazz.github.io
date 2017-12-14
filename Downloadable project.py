num = int(input('Enter a number: '))
double = num*2
print('Double your number is: ')
print(double)

if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

import turtle
x=turtle.Turtle()
x.speed(0)
for i in range(100):
    x.forward(num)
    x.right(90)


