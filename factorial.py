"""Factorial calculator using a loop and recursion."""


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    try:
        n = int(input("Enter a non-negative integer: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    print(f"{n}! (iterative) = {factorial_iterative(n)}")
    print(f"{n}! (recursive) = {factorial_recursive(n)}")


if __name__ == "__main__":
    main()