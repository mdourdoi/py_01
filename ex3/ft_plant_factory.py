class Plant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant"""
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {name.capitalize()} ({height}cm, {age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("rose", 25, 30)
    Plant("oak", 200, 365)
    Plant("cactus", 5, 90)
    Plant("sunflower", 80, 45)
    Plant("Fern", 15, 120)
    print("\nTotal plants created: 5")
