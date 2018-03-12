"""
Each positive integer can be decomposed into the sum of different positive Fibonacci numbers.
In some cases, this distribution is unequivocal, but generally we can accomplish it in several ways.
For example, the number 12 can be represented as the sum of 8 + 3 + 1 (and only in this way), while the number 15 is
equal to 13 + 2 or 8 + 5 + 2. Write a program that reads an integer N (3 ≤ N ≤ 1000000000) and prints one arbitrarily
chosen distribution of N for the sum of the different positive Fibonacci numbers. For example, for N = 12, your program
should print: 8 3 1
"""


def fib_list(n):
    """
    Returns list of fibonacci numbers
    """
    fibonacci = [0, 1]
    i = 2
    while i <= n:
        k = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(k)
        i = i + 1
    return fibonacci


def decompose(number):
    """
    Decompose integer N (3 ≤ N ≤ 1000000000) into Fibonacci numbers.
    """
    fibonacci = fib_list(45)
    decomposed = []
    n = number
    for i in fibonacci[::-1]:
        if i <= n:
            decomposed.append(i)
            n -= i
        if n == 0:
            break

    print('Number -> {}'.format(number))
    print(decomposed, sum(decomposed))



decompose(324)
