
def factorial_while(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


def factorial_recursive(n):
    if n == 0: # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1) # Kaller på seg selv


def main():

    n = int(input("Enter a nonnegative integer: "))
    print("Factorial of", n, "is", factorial_recursive(n))


    # Factorial = 3
    # 3 * 2 * 1 = 6

    # Factorial = 5
    # 5 * 4 * 3 * 2 * 1 = 120


if __name__ == "__main__":
    main()
