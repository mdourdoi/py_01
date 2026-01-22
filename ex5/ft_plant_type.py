class Plant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant with secured data"""
        self.__name = name
        if (height >= 0 and age >= 0):
            self.__height = height
            self.__age = age
            self.__type = "plant"
        else:
            if (height < 0):
                print(f"Invalid initialization attempted : height {height}cm")
                self.__height = 0
                print("Security : height can't be negative, set to 0")
            if (age < 0):
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

    def get_type(self):
        """Secures the access to the type"""
        return (self.__type)

    def set_type(self, type: str):
        """Securely sets the height of the plant"""
        self.__type = type

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

    def get_info(self, display=1, type="plant"):
        name = self.__name.capitalize()
        ret = f"{name} ({type}): {self.__height}cm, {self.__age} days"
        if (display):
            print(ret)
        return (ret)


class Flower(Plant):
    """Represents a flower, which is a subspecy of plant"""

    def __init__(self, name, height, age, color: str, bloom: bool):
        """Initializes the flower with secured data"""
        super().__init__(name, height, age)
        self.set_type("flower")
        self.__color = color
        self.__bloom = bloom

    def get_color(self):
        """Secures the access to the color"""
        return (self.__color)

    def set_color(self, color: str):
        """Securely sets the color of the flower"""
        self.__color = color
        print(f"Color updated: {color} [OK]")

    def get_bloom(self):
        """Secures the access to the bloom status"""
        return (self.__bloom)

    def bloom(self):
        """Blooms the flower"""
        name = self.get_name().capitalize()
        if (self.get_bloom()):
            print(f"{name} already bloomed!")
        else:
            self.__bloom = True
            print(f"{name} is blooming beautifully!")

    def get_info(self):
        """Displays info about the flower"""
        color = self.get_color()
        type = self.get_type().capitalize()
        print(super().get_info(0, type), f"{color} color")


class Tree(Plant):
    """Represents a tree, which is a subspecy of plant"""

    def __init__(self, name: str, height: int, age: int, diameter: int):
        """Initializes the tree with secured data"""
        super().__init__(name, height, age)
        self.set_type("tree")
        if (diameter > 0):
            self.__trunk_diameter = diameter
        else:
            print(f"Invalid initialization attempted : diameter {diameter}cm")
            self.__diameter = 0
            print("Security : diameter can't be negative, set to 0")

    def get_trunk_diameter(self):
        """Secures the access to the diameter"""
        return (self.__trunk_diameter)

    def set_trunk_diameter(self, diameter: int):
        """Securely sets the diameter of the tree"""
        if (diameter > 0):
            self.__trunk_diameter = diameter
        else:
            print(f"Invalid input attempted : diameter {diameter}cm")
            print("Security : Negative diameter rejected")

    def produce_shade(self, area: int):
        """Casts a correct amount of shade"""
        if (area >= 0):
            print(f"{self.get_name} provides {area} square meters of shade")
        else:
            print(f"Invalid input : cast {area} square meters of shade")
            print("Security : Can't cast a negative area of shade")

    def get_info(self):
        """Displays info about the tree"""
        diameter = self.get_trunk_diameter()
        type = self.get_type().capitalize()
        print(super().get_info(0, type), f"{diameter}cm diameter")


class Vegetable(Plant):
    """Represents a vegetable, which is a subspecy of plant"""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initializes the vegetable with secured data"""
        super().__init__(name, height, age)
        self.set_type("vegetable")
        self.__nutritional_value = nutritional_value
        if (harvest_season in ("summer", "spring", "winter", "autumn")):
            self.__harvest_season = harvest_season
        else:
            print(f"Invalid input : harvest season set at {harvest_season}")
            self.__harvest_season = "summer"
            print("Security : Unrecognized season, set to summer")

    def get_nutritional_value(self):
        """Secures the access to the nutritional value"""
        return (self.__nutritional_value)

    def get_harvest_season(self):
        """Secures the access to the harvest season"""
        return (self.__harvest_season)

    def set_nutritional_value(self, nutritional_value: str):
        """Securely sets the nutritional value of the vegetable"""
        self.__nutritional_value = nutritional_value

    def set_harvest_season(self, harvest_season: str):
        """Securely sets the harvest season of the vegetable"""
        if (harvest_season in ("summer", "spring", "winter", "autumn")):
            self.__harvest_season = harvest_season
        else:
            print(f"Invalid input : harvest season set at {harvest_season}")
            print("Security : Can't set an unrecognized season")

    def get_info(self):
        """Displays info about the vegetable"""
        season = self.get_harvest_season()
        type = self.get_type().capitalize()
        name = self.get_name().capitalize()
        value = self.get_nutritional_value()
        print(super().get_info(0, type), f"{season} harvest")
        print(f"{name} is rich in {value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("rose", 25, 30, "red", False)
    violet = Flower("violet", 10, 20, "purple", True)
    oak = Tree("oak", 500, 1825, 50)
    birch = Tree("birch", 200, 1500, 25)
    tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    carrots = Vegetable("carrots", 10, 50, "summer", "vitamin A")
    rose.get_info()
    rose.bloom()
    print()
    violet.get_info()
    violet.bloom()
    print()
    oak.get_info()
    birch.get_info()
    print()
    tomato.get_info()
    carrots.get_info()
