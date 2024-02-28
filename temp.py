class Temperature:
    """A class to represent temperature and convert between Celsius and Fahrenheit."""

    def __init__(self, degrees, scale="celsius"):
        """
        Initializes a Temperature object.

        Args:
            degrees (float): The temperature value.
            scale (str, optional): The temperature scale. Defaults to "celsius".
        """

        self.degrees = degrees
        self.scale = scale.lower()

        if self.scale not in ["celsius", "fahrenheit"]:
            raise ValueError(f"Invalid temperature scale: {self.scale}")

    def convert_to_celsius(self):
        """
        Converts the temperature to Celsius and returns the value.

        Returns:
            float: The temperature in Celsius.
        """

        if self.scale == "celsius":
            return self.degrees
        else:
            return (self.degrees - 32) * 5 / 9

    def convert_to_fahrenheit(self):
        """
        Converts the temperature to Fahrenheit and returns the value.

        Returns:
            float: The temperature in Fahrenheit.
        """

        if self.scale == "fahrenheit":
            return self.degrees
        else:
            return (self.degrees * 9 / 5) + 32

# Example usage
temp_celsius = Temperature(25)
print(f"{temp_celsius.degrees} degrees Celsius is equal to {temp_celsius.convert_to_fahrenheit():.2f} degrees Fahrenheit.")

temp_fahrenheit = Temperature(77, "fahrenheit")
print(f"{temp_fahrenheit.degrees} degrees Fahrenheit is equal to {temp_fahrenheit.convert_to_celsius():.2f} degrees Celsius.")
