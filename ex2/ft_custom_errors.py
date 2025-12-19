class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def thefuckingfunction():
    try:
        raise PlantError("PlantError: The tomato plant is wilting!")

    except PlantError as error:
        print("Caught", error)

    try:
        raise WaterError("WaterError: Not enough water in the tank!")

    except WaterError as error:
        print("Caught", error)

    try:
        raise GardenError("a garden error: The tomato plant is wilting!")

    except GardenError as error:
        print("Caught", error)

    try:
        raise GardenError("a garden error: Not enough water in the tank!")

    except GardenError as error:
        print("Caught", error)


thefuckingfunction()
