import math

def gcd_lcm():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    gcd_val = math.gcd(num1, num2)
    lcm_val = math.lcm(num1, num2) 
    
    print(f"The GCD of {num1} and {num2} is {gcd_val}")
    print(f"The LCM of {num1} and {num2} is {lcm_val}")

gcd_lcm()