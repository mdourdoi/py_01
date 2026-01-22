def ft_garden_intro(plant: str, height: int, age: int):
    """Displays informations about the plant"""
    print("Plant:", plant.capitalize())
    print(f"Height: {height} cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    name = "rose"
    height = 25
    age = 30
    ft_garden_intro(name, height, age)
    print("\n=== End of Program ===")
