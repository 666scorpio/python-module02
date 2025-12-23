class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems."""
    pass


class WaterError(GardenError):
    """Exception raised when watering fails."""
    pass


class Plant:
    def __init__(self, plant_name, water_level, sunlight_hours):
        self.name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 0

    def add_plant(self, plant_name, water_level, sunlight_hours):
        try:
            if plant_name:
                p = Plant(plant_name, water_level, sunlight_hours)
                self.plants[plant_name] = p
                print(f"Added {plant_name} successfully")
            else:
                raise PlantError("Error adding plant: Plant name cannot be empty!")
        except PlantError as error:
            print(error)

    def fill_tank(self, n):
        self.water_tank += n

    def watering_plants(self):
        print("Opening watering system")
        print("Watering plants...")
        try:
            for plant in self.plants.values():
                if self.water_tank > 0:
                    plant.water_level += 1
                    self.water_tank -= 1
                    print(f"Watering {plant.name} - success")
                else:
                    raise WaterError("Not enough water in tank")
        except GardenError as error:
            print("Caught GardenError:", error)
            print("System recovered and continuing...")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant):
        """Check if a plant's name, water level, and sunlight hours are valid.
        Raises GardenError with a descriptive message for invalid input.
        Returns a success message if all values are valid.
        """
        if not plant.name:
            raise GardenError("plant name cannot be empty!")
        if plant.water_level < 1 or plant.water_level > 10:
            if plant.water_level > 10:
                raise GardenError(f"Water level {plant.water_level} is too high (max 10)")
            else:
                raise GardenError(f"Water level {plant.water_level} is too low  (min 1)")
        if plant.sunlight_hours < 2 or plant.sunlight_hours > 12:
            if plant.sunlight_hours < 2:
                raise GardenError(f"Error: Sunlight hours {plant.sunlight_hours} "
                                 "is too low (min 2)")
            else:
                raise GardenError(f"Error: Sunlight hours {plant.sunlight_hours} "
                             "is too high (max 12)")
        print(f"{plant.name} healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})")


print("=== Garden Management System ===")
print("Adding plants to garden...")

garden = GardenManager()

garden.add_plant("tomato", 5, 8)
garden.add_plant("lettuce", 15, 8)
garden.fill_tank(2)
garden.watering_plants()
try:
    garden.check_plant_health(garden.plants["tomato"])
    garden.check_plant_health(garden.plants["lettuce"])
    
except GardenError as error:
    print("Error checking lettuce:", error)
