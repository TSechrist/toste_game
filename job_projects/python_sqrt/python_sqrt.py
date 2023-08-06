# sqrt_native
# Square root function that uses native python library to raise input to 0.5: num^(0.5)
# Input: num (float)
# Output: square root of num
def sqrt_native(num):
    return (num ** 0.5)

# sqrt_calculate
# Square root function that uses Newton's method to iteratively calculate the square root.
# Input: num (float)
# Output: square root of num
    # guess = number
    # while abs(guess * guess - number) > epsilon:
    #     guess = 0.5 * (guess + number / guess)
    
    # return guess

def sqrt_calculate(num):
    low, high = 0, max(1, num)
    mid = high
    while high - low > 1e-8:
        mid = 0.5 * (low + high)
        square = mid * mid
        
        if square > num:
            high = mid
        elif square < num:
            low = mid
        else:
            return low
            
    return low

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