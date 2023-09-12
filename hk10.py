a = eval(input())
from sympy import *
x = symbols('x')
solve(x*x*x-a,x)