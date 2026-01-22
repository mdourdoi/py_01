class Plant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    for i in (rose, sunflower, cactus):
        print(f"{i.name.capitalize()}: {i.height} cm, {i.age} days old")
