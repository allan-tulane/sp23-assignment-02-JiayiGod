"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time
import math

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
    xvec = x.binary_vec
    yvec = y.binary_vec
    if  len(xvec) <=1 and len(yvec) <= 1:
        return x.decimal_val*y.decimal_val
    xvec, yvec = pad(xvec, yvec)
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)
    xLyL=subquadratic_multiply(x_left, y_left)
    xRyR=subquadratic_multiply(x_right, y_right)
    xLyR_xRyL=subquadratic_multiply(BinaryNumber(x_left.decimal_val+x_right.decimal_val), BinaryNumber(y_left.decimal_val+y_right.decimal_val))-xLyL-xRyR
    res=bit_shift(BinaryNumber(xLyL),len(xvec)).decimal_val+bit_shift(BinaryNumber(xLyR_xRyL),len(xvec)//2).decimal_val+xRyR
    return res
    pass
    ###

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(10), BinaryNumber(1)) == 10*1
    assert subquadratic_multiply(BinaryNumber(100), BinaryNumber(100)) == 100*100
    assert subquadratic_multiply(BinaryNumber(7475), BinaryNumber(2454)) == 7475*2454
    assert subquadratic_multiply(BinaryNumber(201), BinaryNumber(2142)) == 201*2142
    assert subquadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1*1
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(2)) == 0*2

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    f(x,y)
    return (time.time() - start)*1000


print(time_multiply(BinaryNumber(int(math.pow(2,500))), BinaryNumber(int(math.pow(2,500))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,450))), BinaryNumber(int(math.pow(2,450))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,400))), BinaryNumber(int(math.pow(2,400))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,350))), BinaryNumber(int(math.pow(2,350))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,300))), BinaryNumber(int(math.pow(2,300))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,250))), BinaryNumber(int(math.pow(2,250))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,200))), BinaryNumber(int(math.pow(2,200))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,150))), BinaryNumber(int(math.pow(2,150))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,100))), BinaryNumber(int(math.pow(2,100))),subquadratic_multiply))
print(time_multiply(BinaryNumber(int(math.pow(2,50))), BinaryNumber(int(math.pow(2,50))),subquadratic_multiply))
