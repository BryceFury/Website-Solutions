'''

Codewars Kata - 8 Kyu - 2 + 2 * 2 problem

Description:

Steve loves MS Windows calculator in Standard mode.

He tries to calculate 2 + 2 * 2 in his favorite programming language. But Steve doesn't know about order of operations and he wonders why answers are different. He expects 8 but gets 6.

Help Steve to fix program, so result will be identical to MS Windows calculator.

'''

#This Kata is broken
def calculate(x):
    return ((x + x) * x)
    