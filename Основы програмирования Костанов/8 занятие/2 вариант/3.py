from math import sqrt

a = int(input())

def s_triangle(a):
    s = (sqrt(3)*(a^2))/4
    return s



print(s_triangle(a)*6)