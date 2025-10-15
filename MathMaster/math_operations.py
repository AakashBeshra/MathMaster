"""
MathOperations - Core mathematical operations for MathMaster
"""

import math

class MathOperations:
    """Handles all mathematical operations"""
    
    @staticmethod
    def add(a, b):
        """Addition operation"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtraction operation"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiplication operation"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Division operation with zero division check"""
        if b == 0:
            raise ValueError("Division by zero is not allowed!")
        return a / b
    
    @staticmethod
    def modulus(a, b):
        """Modulus operation with zero division check"""
        if b == 0:
            raise ValueError("Modulus by zero is not allowed!")
        return a % b
    
    @staticmethod
    def power(base, exponent):
        """Power operation"""
        return math.pow(base, exponent)
    
    @staticmethod
    def square_root(x):
        """Square root operation with validation"""
        if x < 0:
            raise ValueError("Square root of negative number is not real!")
        return math.sqrt(x)
    
    @staticmethod
    def trig_functions(angle):
        """Calculate trigonometric functions"""
        return {
            'sin': math.sin(angle),
            'cos': math.cos(angle),
            'tan': math.tan(angle)
        }
    
    @staticmethod
    def logarithm(x):
        """Natural logarithm with validation"""
        if x <= 0:
            raise ValueError("Logarithm is only defined for positive numbers!")
        return math.log(x)
    
    @staticmethod
    def factorial(n):
        """Factorial calculation with validation"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        if not isinstance(n, int):
            raise ValueError("Factorial requires an integer!")
        if n > 1000:
            raise ValueError("Number too large for factorial calculation!")
        return math.factorial(n)
    
    @staticmethod
    def absolute(x):
        """Absolute value"""
        return abs(x)
    
    @staticmethod
    def round_number(x, decimals=2):
        """Round number to specified decimal places"""
        return round(x, decimals)
    
    @staticmethod
    def percentage(value, total):
        """Calculate percentage"""
        if total == 0:
            raise ValueError("Total cannot be zero for percentage calculation!")
        return (value / total) * 100
    
    @staticmethod
    def is_infinity(x):
        """Check if number is infinite"""
        return math.isinf(x)
    
    @staticmethod
    def gcd(a, b):
        """Greatest Common Divisor"""
        return math.gcd(int(a), int(b))
    
    @staticmethod
    def lcm(a, b):
        """Least Common Multiple"""
        try:
            return math.lcm(int(a), int(b))
        except AttributeError:
            # Fallback for older Python versions
            gcd_val = math.gcd(int(a), int(b))
            return abs(a * b) // gcd_val if gcd_val != 0 else 0