#coding=utf8
from decimal import *
#针对浮点型的四舍五入的方法
def floatRound(a, n):
    x = a
    getcontext().rounding = ROUND_HALF_UP
    length = len(a[a.find('.'):])
    if length >= (n + 1):
        string = '{:.' + str(n) + 'f}'
        x = string.format(Decimal(a))
    return x


if __name__ == "__main__":
    a = '238.345'
    n = 2
    t = floatRound(a, n)
    print type(t), t
