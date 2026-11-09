
"""
Light Class with On/Off State Toggle

This program demonstrates state management
using a Python class and instance attributes.
"""


class Light:
    """A class to control a light's ON/OFF state."""

    def __init__(self):
        """Initialize the light as OFF."""
        self.is_on = False

    def turn_on(self):
        """Turn the light ON."""
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        """Turn the light OFF."""
        self.is_on = False
        print("Light is OFF")

    def status(self):
        """Display the current light status."""
        if self.is_on:
            print("Current status: ON")
        else:
            print("Current status: OFF")


# Create a Light object
light = Light()

# Turn ON and check status
light.turn_on()
light.status()

# Turn OFF and check status
light.turn_off()
light.status()
