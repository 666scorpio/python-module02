"""
Demonstrates raising and handling errors for plant health checks.
Validates plant name, water level, and sunlight hours.
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check if a plant's name, water level, and sunlight hours are valid.
    Raises ValueError with a descriptive message for invalid input.
    Returns a success message if all values are valid.
    """
    if not plant_name:
        raise ValueError("plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        else:
            raise ValueError(f"Water level {water_level} is too low  (min 1)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too low (min 2)")
        else:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Test check_plant_health with various valid and invalid scenarios.

    Demonstrates raising and catching ValueError for different error cases.
    """
    print("=== Garden Plant Health Checker ===")
    tests = [
            ("good values", ("sunflower", 5, 6)),
            ("empty plant name", ("", 5, 6)),
            ("bad water level", ("sunflower", 15, 6)),
            ("bad sunlight hours", ("sunflower", 5, 0))
    ]
    for description, (plant_name, water_level, sunlight_hours) in tests:
        try:
            print(f"\nTesting {description}...")
            result = check_plant_health(plant_name,
                                        water_level, sunlight_hours)
            print(result)
        except ValueError as error:
            print("Error:", error)
    print("\nAll error raising tests completed!")


test_plant_checks()
