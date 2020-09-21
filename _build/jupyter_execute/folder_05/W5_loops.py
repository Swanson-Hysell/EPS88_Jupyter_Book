# 5.1 Loops and Conditionals

**Outline:**

* Iterating with `for` or `while` loops
* Exiting a loop with `break` and `continue` statements
* Conditional `if`, `elif`, `else` statements

## Additional Assigned Reading

Data 8 textbook "Computational and Inferential Thinking: The Foundations of Data Science" By Ani Adhikari and John DeNero [Chapter 9 Randomness](https://www.inferentialthinking.com/chapters/09/Randomness.html). This should overlap with your assigned reading for Data 8.


## For Loops

**Watch this tutorial video:**

[![](http://img.youtube.com/vi/OnDr4J2UXSA/0.jpg)](http://www.youtube.com/watch?v=OnDr4J2UXSA "")

For loops can be used to iterate over the elements of a list or array. The syntax for the loop is started with `for element in list_name:` where `element` is a variable name you choose and `list_name` is the object you want to interate through. Then the code you want to perform within the loop is indented 4 spaces. 

import numpy as np
for i in np.arange(0,5):
    print(i)

It's often necessary to _initiate_ i.e. preset variables or arrays you plan to use in your loop. You want arrays to stay the same dimensions and size, and in general you should know the value of the variable before you iterate over it.

# two methods for summing all the elements in a list and an example with setting an array
total=0
total2=0
squares=np.zeros(5)
for i in np.arange(0,5):
    total = total + i
    total2 += i
    squares[i]=i**2

print(total,total2,squares)


## While Loops

`while` loops will repeat as long as the condition you set is `True`. You need to be careful that you are not setting up an infinite loop with a condition that will never be `False`.

count = 0
while count < 5:
    print(count)
    count += 1

## Continue and Break Statements

`continue` will exit the current loop iteration you are in and skip to the next loop step. 

# Print out only odd numbers
for x in range(12):
    # check if x is even, divides by 2 with no remainder
    if x % 2 == 0:
        continue
    print(x)

`break` can be used to exit a `for` or `while` loop. 

# Sum odd numbers and Print out only until the sum is less than 50
total = 0
for x in range(50):
    # check if x is even, divides by 2 with no remainder
    if x % 2 == 0:
        continue
    if total > 50:
        break
    total = total + x
    print(x,total)

## If, elif, else Statements

`if` statements, like loops, are used to control the flow of your code. You write a conditional `if` statement, and if it is met then the indented code within the `if` block will be executed.

![if block](./figures/if_flowchart.png)  

# simple code to test if a number is positive
num = 5

if num >= 0:
    print('Num is positive or zero!')

But if the `if` condition is not met, nothing happens. You can set what happens if the `if` condition is not met with an `else` statement.

![if/else block](./figures/else_flowchart.png)  

# simple code to test if a number is positive
num = -5

if num >= 0:
    print('Num is positive or zero!')
else:
    print('Num is negative. :(')

You can build mulitple conditions into you logic tree with `if`, `elif` (which stands for else-if), `else` statements.

![if/elseif/else block](./figures/elseif_flowchart.png)  

# code to test if a number is positive
num = 0

if num > 0:
    print('Num is positive.')
elif num < 0:
    print('Num is negative.')
else:
    print('Num is zero.')

