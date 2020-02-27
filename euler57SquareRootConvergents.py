'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

2–√=1+12+12+12+…
By expanding this for the first four iterations, we get:

1+12=32=1.5
1+12+12=75=1.4
1+12+12+12=1712=1.41666…
1+12+12+12+12=4129=1.41379…

The next three expansions are 9970, 239169, and 577408, but the eighth expansion, 1393985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
'''

from fractions import Fraction

def squareRootConvergents(n):
    #n expansions
    count = 0
    nume = 1
    deno = 1
    i = 1
    while i <= n:
        i += 1
        nume, deno = 2*deno + nume, deno + nume  #number = 1 +  1/(2+new_number) 
        if len(str(nume)) > len(str(deno)):
            count += 1
    return count
       


# below answer is not able to give proper fractions 
def squareRootConvergents1(n):
    #n expansions
    count = 0
    number = 1
    i = 1
    while i < n:
        i += 1
        new_number = number - 1
        number = 1 +  1/(2+new_number)
        ratio_number = Fraction(number)
        nume = ratio_number.numerator
        deno = ratio_number.denominator
        #print(nume, deno)
        if len(str(nume)) > len(str(deno)):
            count += 1
    return count

final = squareRootConvergents(1000)
print(final)


