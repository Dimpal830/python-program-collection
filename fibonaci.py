"""Fibonacci series using a loop and recursion."""


def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    try:
        n = int(input("How many terms do you want? "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if n <= 0:
        print("Please enter a number greater than 0.")
        return

    print("Series:", ", ".join(map(str, fibonacci_series(n))))
    print(f"Term {n} (recursive) = {fibonacci_recursive(n - 1)}")


if __name__ == "__main__":
    main()
