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
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    ps =[
            "tomato",
            "lettuce",
            "carrots",
            ]
    water_plants(ps)
    ps[1] = None
    water_plants(ps)
