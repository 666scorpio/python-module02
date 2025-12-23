"""
Demonstrates using finally block in a garden watering system.
Ensures cleanup happens even if errors occur during watering.
"""


class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems."""
    pass


class WaterError(GardenError):
    """Exception raised when watering fails."""
    pass


def water_plants(plant_list):
    """Water a list of plants, handling invalid plants, always cleaning up."""
    try:
        print("Opening watering system")
        for plant in plant_list:
            try:
                if plant is not None:
                    print("Watering", plant)
                else:
                    raise WaterError(
                            "Error: Cannot water None - invalid plant!")
            except WaterError as error:
                print(error)
                return None
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test normal and error scenarios for the watering system."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    ps = [
            "tomato",
            "lettuce",
            "carrots",
            ]
    water_plants(ps)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    ps[1] = None
    water_plants(ps)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
