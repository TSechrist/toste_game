# sqrt_native
# Square root function that uses native python library to raise input to 0.5: num^(0.5)
# Input: num (float)
# Output: square root of num
def sqrt_native(num):
    return (num ** 0.5)

# sqrt_calculate
# Square root function that uses Newton's method to iteratively calculate the square root.
# Defaults set for 50 iterations at 1e-8 precision
# Input: num (float)
# Output: square root of num
def sqrt_calculate(num):
    num_iterations = 50
    precision = 1e-8
    ret_guess = num
    
    for count in range(num_iterations):
        ret_guess = 0.5 * (ret_guess + num / ret_guess)
        if abs(ret_guess * ret_guess - num) < precision:
            print("Found in " + str(count) + " iterations.")
            return ret_guess
        
    raise ValueError("Square root not found after " + str(num_iterations) + " iterations.")

# Main driver function of program
if __name__ == "__main__":
    input_num = input("Enter a number to square root: ")

    # Input validation to ensure a number was entered
    try:
        input_float = float(input_num)
    except ValueError:
        raise ValueError("Error: Must enter a number.")
    
    # Input validation to check for positive numbers as negative number square root is undefined
    if input_float < 0:
        raise ValueError("Error: Number is less than 0.")

    print("Square root using native python library: ", sqrt_native(input_float))
    print("Square root using iterative calculation: ", sqrt_calculate(input_float))