def sqrt_native(num):
    if num < 0:
        print("Error: number is less than 0")
        return
    else:
        return (num ** 0.5)

def sqrt_calculate(num):
    if num < 0:
        print("Error: number is less than 0")
        return
    else:
        return (num ** 0.5)

if __name__ == "__main__":
    input_num = int(input("Enter a number to square root: "))
    print(sqrt_native(input_num))