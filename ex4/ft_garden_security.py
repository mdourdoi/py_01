class SecurePlant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant with secured data"""
        self.__name = name
        if (height >= 0):
            self.__height = height
        else:
            print(f"Invalid initialization attempted : height {height}cm")
            self.__height = 0
            print("Security : height can't be negative, set to 0")
        if (age >= 0):
            self.__age = age
        else:
            print(f"Invalid initialization attempted : age {age}")
            self.__age = 0
            print("Security : age can't be negative, set to 0")

    def get_name(self):
        """Secures the access to the name"""
        return (self.__name)

    def get_height(self):
        """Secures the access to the height"""
        return (self.__height)

    def get_age(self):
        """Secures the access to the age"""
        return (self.__age)

    def set_height(self, hgt: int):
        """Securely sets the height of the plant"""
        if (hgt >= 0):
            self.__height = hgt
            print(f"Height updated: {hgt} cm [OK]")
        else:
            print(f"Invalid operation attempted : height {hgt}cm [REJECTED]")
            print("Security : Negative height rejected")

    def set_age(self, age: int):
        """Securely sets the height of the plant"""
        if (age >= 0):
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted : age {age} days [REJECTED]")
            print("Security : Negative age rejected")

    def get_info(self):
        """Displays information about the plant"""
        name = self.__name.capitalize()
        print(f"Current plant: {name} ({self.__height}cm, {self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("rose", 20, 30)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.set_age(-5)
    print()
    rose.get_info()
