def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0
        #print better
    return approx
    
def print_triangular_numbers(n):
    i=1
    j=0
    while i<=n:
        j=i+j
        print i, '\t', j
        i+=1

def is_prime(n):
    """
      >>> is_prime(3)
      True
      >>> is_prime(4)
      False
      >>> is_prime(5)
      True
      >>> is_prime(23)
      True
      >>> is_prime(144)
      False
    """  
    
    i=2
    t=True
    while i<sqrt(n)+1:
        if n%i==0:
            t=False and t
        else: t=True and t
        i+=1
    return t
        
        
def num_digits(n):
    """
      >>> num_digits(12345)
      5
      >>> num_digits(0)
      1
      >>> num_digits(-12345)
      5
    """
    count = 0
    n=abs(n)
    if n==0:
        return 1
    else:
        while n:
            count = count + 1
            n = n / 10
        return count
        
def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    count = 0
    n=abs(n)
    if n==0:
        return 1
    else:
        while n:
            nn=n % 10
            if nn %2 ==0:
                count = count + 1
            n = n / 10
        return count    
        
def print_digits(n):
    """
      >>> print_digits(13789)
      9 8 7 3 1
      >>> print_digits(39874613)
      3 1 6 4 7 8 9 3
      >>> print_digits(213141)
      1 4 1 3 1 2
    """
    n=abs(n)
    if n==0:
        print n
    else:
        while n:
            nn=n % 10
            print nn, 
            n = n / 10
 
def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(1)
      1
      >>> sum_of_squares_of_digits(9)
      81
      >>> sum_of_squares_of_digits(11)
      2
      >>> sum_of_squares_of_digits(121)
      6
      >>> sum_of_squares_of_digits(987)
      194
    """
    n=abs(n)
    S=0
    if n==0:
        return
    else:
        while n:
            nn=n % 10
            S+=nn*nn
            n = n / 10
        return S
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()