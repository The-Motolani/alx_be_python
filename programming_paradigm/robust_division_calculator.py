def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denum = float(denominator)
        result = num / denum
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."