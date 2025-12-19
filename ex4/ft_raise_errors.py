def check_plant_health(plant_name, water_level, sunlight_hours):
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
    tests = [
            ("sunflower", 5, 6),
            ("", 5, 6),
            ("sunflower", 0, 6),
            ("sunflower", 5, 14)
    ]
    for plant_name, water_level, sunlight_hours in tests:
        try:
            result = check_plant_health(plant_name,
                                        water_level, sunlight_hours)
            print(result)
        except ValueError as error:
            print("Error:", error)
