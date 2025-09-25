def perform_operation(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("Both inputs must be numbers.")
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "Cannot divide by zero."
        case _:
            raise ValueError(f"Unsupported operation: {operation}")