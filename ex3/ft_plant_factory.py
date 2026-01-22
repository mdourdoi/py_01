class Plant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant"""
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {name.capitalize()} ({height}cm, {age} days)")


if __name__ == "__main__":
    names = ["rose", "oak", "cactus", "sunflower", "fern"]
    heights = [25, 200, 5, 80, 15]
    ages = [30, 365, 90, 45, 120]
    plants = []
    print("=== Plant Factory Output ===")
    for i in range(len(names)):
        plants.append(Plant(names[i], heights[i], ages[i]))
    print(f"\nTotal plants created: {len(plants)}")
