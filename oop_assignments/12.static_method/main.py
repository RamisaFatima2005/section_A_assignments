# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

temp_in_celsius = int(input("Enter temp in celcius: "))
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)

print(f"{temp_in_celsius}°C = {temp_in_fahrenheit}°F")