class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            try:
                if plant != None:
                    print("Watering", plant)
                else:
                    raise WaterError("Error: Cannot water None - invalid plant!")
            except WaterError as error:
                print(error)
                return None
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    ps =[
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
