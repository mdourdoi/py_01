class Plant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant with secured data"""
        self.__name = name
        self.__type = "plant"
        self.__last_growth = 0
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

    def get_type(self):
        """Secures the access to the type"""
        return (self.__type)

    def get_last_growth(self):
        """Secures the access to the last_growth"""
        return (self.__last_growth)

    def set_type(self, kind: str):
        """Securely sets the height of the plant"""
        self.__type = kind

    def set_height(self, hgt: int, flag=0):
        """Securely sets the height of the plant"""
        if (hgt >= 0):
            self.__height = hgt
            if flag:
                print("Height validation test: True")
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

    def grow(self, growth: int):
        """Adds growth to the current size"""
        if growth >= 0:
            self.set_height(self.get_height() + growth)
            self.__last_growth = growth
            print(f"{self.get_name()} grew {growth} cm")
        else:
            print(f"Invalid operation attempted : grow {growth} cm [REJECTED]")
            print("Security : Negative growth rejected")

    def get_info(self, display=1, kind="plant"):
        name = self.__name.capitalize()
        ret = f"{name}: {self.__height}cm"
        if (display):
            print(ret)
        return (ret)


class FloweringPlant(Plant):
    """Represents a flowering plant"""

    def __init__(self, name, height, age, color: str, bloom: bool):
        """Initializes the flower with secured data"""
        super().__init__(name, height, age)
        self.set_type("flowering plant")
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

    def get_info(self, display=1):
        """Displays info about the flowering plant"""
        color = self.get_color()
        kind = self.get_type().capitalize()
        if (self.get_bloom()):
            ret = f"{super().get_info(0, kind)} {color} (bloomed)"
            if (display):
                print(ret)
            return (ret)
        else:
            ret = f"{super().get_info(0, kind)}, {color} (blooming)"
            if (display):
                print(ret)
            return (ret)


class PrizeFlower(FloweringPlant):
    """Represents a flowering plant with a prize"""

    def __init__(self, name, height, age, color, bloom, prize: int):
        """Initializes the prized flower with secured data"""
        super().__init__(name, height, age, color, bloom)
        self.set_type("prize flower")
        if (prize >= 0):
            self.__prize = prize
        else:
            print(f"Invalid initialization attempted : prize {prize}")
            self.__prize = 0
            print("Security : prize can't be negative, set to 0")

    def get_prize(self):
        """Securely gets the prize of the prize flower"""
        return (self.__prize)

    def set_prize(self, prize: int):
        """Securely sets the prize of the prize flower"""
        if (prize >= 0):
            self.__prize = prize
        else:
            print("Security : Negative prize rejected")

    def get_info(self, display=1):
        """Displays info about the prize flower"""
        prize = self.get_prize()
        ret = f"{super().get_info(0)}, Prize points: {prize}"
        if display:
            print(ret)
        return (ret)


class Garden:
    """Represents a garden with plants"""

    def __init__(self, name: str, *plants: Plant):
        """Initializes the garden with secured data"""
        self.__name = name
        self.__plants = {}
        for plant in plants:
            self.add_plant(plant)

    def get_plants(self):
        """Securely gets the list of plants"""
        return (self.__plants)

    def has_plant(self, plant: Plant):
        """Checks if the plant is in the garden"""
        if (isinstance(plant, Plant)):
            key = plant.get_name()
            if (key in self.get_plants()):
                return (True)
        return (False)

    def add_plant(self, plant: Plant):
        """Securely adds a plant to the garden"""
        if (isinstance(plant, Plant)):
            if (self.has_plant(plant)):
                print("There is already a plant with this name in the garden")
            else:
                self.__plants[plant.get_name()] = plant
        else:
            print("Invalid input, please input a plant")

    def remove_plant(self, plant: Plant):
        """Securely removes a plant from the garden"""
        if (isinstance(plant, Plant)):
            if (self.has_plant(plant)):
                self.__plants.pop(plant.get_name())
            else:
                print("The plant is not in the garden")
        else:
            print("Invalid input, please input a plant")

    def get_name(self):
        """Secures the access to the name"""
        return (self.__name)

    def grow_garden(self, growth: int):
        """Grow every plant in the garden"""
        for plant in self.get_plants().values():
            plant.grow(growth)


class GardenManager:
    """Represent a Garden manager with its informations"""

    @staticmethod
    def is_plant(obj):
        """Check if the object is a plant"""
        return (isinstance(obj, Plant))

    @staticmethod
    def is_flowering(obj):
        """Check if the object is a FloweringPlant"""
        return (isinstance(obj, FloweringPlant))

    @staticmethod
    def is_prize(obj):
        """Check if the object is a PrizeFlower"""
        return (isinstance(obj, PrizeFlower))

    @staticmethod
    def is_garden(obj):
        """Check if the object is a garden"""
        return (isinstance(obj, Garden))

    def __init__(self, *gardens: Garden):
        """Initializes the manager with secured data"""
        self.__gardens = {}
        for garden in gardens:
            self.add_garden(garden)

    def get_gardens(self):
        """Securely gets the list of gardens"""
        return (self.__gardens)

    def has_garden(self, garden: Garden):
        """Checks if the garden is already in the manager"""
        if (self.is_garden(garden)):
            key = garden.get_name()
            if (key in self.get_gardens()):
                return (True)
        return (False)

    def add_garden(self, garden: Garden):
        """Securely adds a garden"""
        if (self.is_garden(garden)):
            if (self.has_garden(garden)):
                print("Manager already has a garden with this name")
            else:
                self.__gardens[garden.get_name()] = garden
        else:
            print("Invalid input, please input a garden")

    def add_plants_to_garden(self, garden: Garden, *plants: Plant, flag=0):
        """Adds a plant to the garden"""
        for plant in plants:
            if (self.is_garden(garden) and self.is_plant(plant)):
                if (self.has_garden(garden)):
                    key = garden.get_name()
                    target = self.__gardens[key]
                    target.add_plant(plant)
                    name = plant.get_name()
                    garden_name = target.get_name()
                    if flag:
                        print(f"Added {name} to {garden_name}'s garden")
                else:
                    print("The garden is not in the manager")
                    return
            else:
                print("At least one input is invalid")
                return

    def grow_garden(self, garden: Garden, growth: int):
        """Grow every plant in the selected garden"""
        if self.has_garden(garden):
            target = self.__gardens[garden.get_name()]
            print(f"{target.get_name()} is helping all plants grow...")
            for plant in target.get_plants().values():
                plant.grow(growth)

    class GardenStats:
        """Helps to calculate metrics for your garden"""

        def __init__(self, garden: Garden):
            """Initializes the garden to get metrics from"""
            self.__garden = garden

        def count_plants(self):
            """Gets the number of plants in the garden"""
            return (len(self.__garden.get_plants()))

        def total_prize_point(self):
            """Get the sum of the point of each Prize Flower"""
            ret = 0
            for plant in self.__garden.get_plants().values():
                if GardenManager.is_prize(plant):
                    ret += plant.get_prize()
            return (ret)

        def avg_height(self):
            """Get the average height of the plants"""
            ret = 0
            for plant in self.__garden.get_plants().values():
                ret += plant.get_height()
            nb = self.count_plants()
            if nb == 0:
                return (0)
            return (ret / nb)

        def avg_age(self):
            """Get the average age of the plants"""
            ret = 0
            for plant in self.__garden.get_plants().values():
                ret += plant.get_age()
            nb = self.count_plants()
            if nb == 0:
                return (0)
            return (ret / nb)

        def avg_prize(self):
            """Get the average prize of the PrizeFlowers in the garden"""
            ret = 0
            nb = 0
            for plant in self.__garden.get_plants().values():
                if GardenManager.is_prize(plant):
                    ret += plant.get_prize()
                    nb += 1
            if nb == 0:
                return (0)
            return (ret / nb)

        def breakdown(self):
            """Gets a dictionnary counting each type of plant"""
            ret = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in self.__garden.get_plants().values():
                if GardenManager.is_prize(plant):
                    ret["prize"] += 1
                elif GardenManager.is_flowering(plant):
                    ret["flowering"] += 1
                elif GardenManager.is_plant(plant):
                    ret["regular"] += 1
            return (ret)

        def last_growth(self):
            """Get the total last growth of the garden"""
            ret = 0
            for plant in self.__garden.get_plants().values():
                ret += plant.get_last_growth()
            return (ret)

    def print_garden_report(self, garden: Garden):
        """Get metrics from a specific garden"""
        if self.is_garden(garden):
            if self.has_garden(garden):
                target = self.__gardens[garden.get_name()]
                stats = GardenManager.GardenStats(target)
                print(f"=== {target.get_name()}'s Garden Report ===")
                print("Plants in garden:")
                for plant in target.get_plants().values():
                    ret = f"- {plant.get_info(0)}"
                    print(ret)
                count = stats.count_plants()
                last_growth = stats.last_growth()
                ret = f"Plants added: {count}, Total growth: {last_growth}cm"
                print(f"\n{ret}")
                ret = stats.breakdown()
                print("Plant types: ", end="")
                print(f"{ret['regular']} regular, ", end="")
                print(f"{ret['flowering']} flowering, ", end="")
                print(f"{ret['prize']} prize flower(s)")
            else:
                print("The garden is not in the manager")
        else:
            print("Please input a garden")

    def print_global_report(self):
        """Get metrics from all managed gardens"""
        garden_pool = self.get_gardens()
        total_gardens = len(garden_pool)
        if total_gardens > 0:
            print("Garden scores - ", end="")
            parts = []
            for garden in garden_pool.values():
                stats = GardenManager.GardenStats(garden)
                points = stats.total_prize_point()
                parts.append(f"{garden.get_name().capitalize()}: {points}")
            print(", ".join(parts))
            print(f"Total gardens managed: {total_gardens}")
        else:
            print("The manager has no garden")

    @classmethod
    def create_garden_network(cls, *gardens: Garden):
        """Create a manager with all the gardens passed as arguments"""
        network = cls()
        for garden in gardens:
            if cls.is_garden(garden):
                network.add_garden(garden)
        return (network)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice = Garden("Alice")
    bob = Garden("Bob")

    # Manager (via classmethod)
    manager = GardenManager.create_garden_network(alice, bob)

    # Plants building
    oak = Plant("Oak Tree", 100, 30)
    rose = FloweringPlant("Rose", 25, 12, "red flowers", False)
    sunflower = PrizeFlower("Sunflower", 50, 14, "yellow flowers", False, 218)
    orchid = PrizeFlower("Orchid", 60, 20, "blue flowers", True, 46)
    tulip = PrizeFlower("Tulip", 10, 5, "gold flowers", True, 46)

    # Add to Alice's garden
    manager.add_plants_to_garden(alice, oak, rose, sunflower, flag=1)
    manager.add_plants_to_garden(bob, orchid, tulip)
    print()

    # Grow Alice's garden
    manager.grow_garden(alice, 1)
    print()

    # Alice report
    manager.print_garden_report(alice)
    print()

    # Height validation test
    oak.set_height(100, 1)

    # Global report (scores)
    manager.print_global_report()
