"""
Demonstrates custom garden-related exceptions.
Includes PlantError and WaterError inheriting from GardenError.
"""


class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related problems."""
    pass


def test_custom_errors():
    """Demonstrate raising and catching custom garden errors."""
    print("")
    try:
        print("Testing PlantError...")
        raise PlantError("PlantError: The tomato plant is wilting!")

    except PlantError as error:
        print("Caught", error)

    print("")
    try:
        print("Testing WaterError...")
        raise WaterError("WaterError: Not enough water in the tank!")

    except WaterError as error:
        print("Caught", error)

    print("")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("a garden error: The tomato plant is wilting!")

    except GardenError as error:
        print("Caught", error)

    try:
        raise WaterError("a garden error: Not enough water in the tank!")

    except GardenError as error:
        print("Caught", error)


print("=== Custom Garden Errors Demo ===")
test_custom_errors()
print("\nAll custom error types work correctly!")
