def is_fibonacci_number(num):
    import math
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)
a=int(input("Enter the number : "))
print(f"Check whether the given statement is true or false. \n Statement : The number {a} is a Fibonacci Number. \n Answer : ", is_fibonacci_number(a))