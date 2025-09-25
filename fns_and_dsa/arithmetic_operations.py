def perform_operation(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("Both inputs must be numbers.")
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        try:
            return num1 / num2
        except ZeroDivisionError:
            if num2 == 0:
                return "Cannot divide by zero."
    else:
        raise ValueError(f"Unsupported operation: {operation}")