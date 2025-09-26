fahrenheit_to_celsius = (5/9)
celsius_to_fahrenheit = (9/5)

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * fahrenheit_to_celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * celsius_to_fahrenheit) + 32

while True:
    try:
        to_be_converted = float(input("Enter the temperature to convert:  "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
while True:
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if scale == 'C':
        converted = convert_to_fahrenheit(to_be_converted)
        print(f"{to_be_converted}°C is {converted:.2f}°F")
        break
    elif scale == 'F':
        converted = convert_to_celsius(to_be_converted)
        print(f"{to_be_converted}°F is {converted:.2f}°C")
        break
    else:
        print("Invalid temperature. Please enter a numeric value.")