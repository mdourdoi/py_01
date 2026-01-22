class Plant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth: int):
        """Adds growth to the current size"""
        self.height += growth

    def age_days(self, days: int, growth: int):
        """Adds days to the current age and grow the plant at growth per day"""
        self.age += days
        self.grow(growth)

    def get_info(self):
        """Displays information about the plant"""
        name_cap = self.name.capitalize()
        print(f"{name_cap}: {self.height} cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    rose_growth = 1
    sunflower_growth = 12
    growth_speed = 6
    for i in (1, 7):
        print(f"=== Day {i} ===")
        rose.get_info()
        sunflower.get_info()
        rose.age_days(7, rose_growth)
        sunflower.age_days(7, sunflower_growth)
        if (i == 7):
            print(f"Growth this week: +{rose_growth + sunflower_growth}cm")
