#coding=utf8

def mul(x, y):
    if x<10 or y<10 or len(str(x)) % 2!=0 or len(str(y)) % 2!=0:
        return x*y
    length = len(str(x))
    a = long(str(x)[:length/2])
    b = long(str(x)[length/2:])
    c = long(str(y)[:length/2])
    d = long(str(y)[length/2:])
    return pow(10, length) * mul(a,c) + pow(10, length/2) * (mul(a, d) + mul(b, c)) + mul(b, d)

if __name__ == '__main__':
    print mul(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
