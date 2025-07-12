def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def say_hello(name):
    print("Hello, " + name)

def main():
    sum_result = add_numbers(5, 7)
    print(f"The sum is {sum_result}")

    say_hello("World")

if __name__ == "__main__":
    main()
