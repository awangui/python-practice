def dynamic_calculator(*args, **kwargs):
        if not args:
            raise ValueError("At least one number must be provided")
        
        operation = kwargs.get("operation")
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            raise ValueError("Invalid operation. Supported operations are: add, subtract, multiply, divide")
        
        reverse = kwargs.get("reverse", False)
        if reverse:
            args = tuple(reversed(args))
        
        result = args[0]
        if operation == 'add':
            for num in args[1:]:
                result += num
        elif operation == 'subtract':
            for num in args[1:]:
                result -= num
        elif operation == 'multiply':
            for num in args[1:]:
                result *= num
        elif operation == 'divide':
            for num in args[1:]:
                if num == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                result /= num
        
        return result

    # Test cases
if __name__ == "__main__":
    print(dynamic_calculator(1, 2, 3, operation="add"))  # Output: 6
    print(dynamic_calculator(10, 2, 1, operation="subtract", reverse=True))  # Output: -7
    print(dynamic_calculator(2, 3, 4, operation="multiply"))  # Output: 24
    print(dynamic_calculator(20, 5, 2, operation="divide"))  # Output: 2.0