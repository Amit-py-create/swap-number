# Function to swap two numbers using arithmetic operations
def swap_arithmetic(a, b):
    print("Before Swap: a =", a, ", b =", b)
    a = a + b
    b = a - b
    a = a - b
    print("After Swap: a =", a, ", b =", b)

# Example usage
if __name__ == "__main__":
    x = 5
    y = 10
    swap_arithmetic(x, y)
