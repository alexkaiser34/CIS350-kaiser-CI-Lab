def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def divide_numbers(a, b):
    return a / b

def multiply_numbers(a, b):
    return a * b

def divide_and_floor_numbers(a,b):
    return a // b

def modulus_numbers(a, b):
    return a % b

if __name__ == "__main__":
    print("Adding:", add_numbers(2,4))
    print("Subtracting:", subtract_numbers(9,2))
    print("Dividing:", divide_numbers(11,2))
    print("Multiplying:", multiply_numbers(9,2))
    print("Divide and floor:", divide_and_floor_numbers(11,2))
    print("Modulus:", modulus_numbers(10,3))

