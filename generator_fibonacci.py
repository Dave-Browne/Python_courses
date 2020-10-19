def fibonacci(num):
    '''
    A Fibonacci number is the sum of the 2 preceding Fibonacco numbers. Fn = F(n-1) + F(n-2) for n>1
    The beginning of a Fibonacci sequence is thus: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
    '''
    a = 0
    b = 1
    for i in range(num):
        yield a
        a_orig = a
        a = b
        b += a_orig


if __name__=="__main__":
    for item in fibonacci(10):
        print(item)
