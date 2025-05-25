from abc import ABC, abstractmethod

# Abstract base class for all coffee machines
class CoffeeMachine(ABC):
    @abstractmethod
    def make_coffee(self) -> str:
        """Prepare a coffee drink"""
        pass

    def description(self) -> str:
        """Describe the machine"""
        return f"This is a {self.__class__.__name__}."

# Concrete implementation: Filter Coffee Machine
class FilterCoffeeMachine(CoffeeMachine):
    def make_coffee(self) -> str:
        return "Brewing coffee using a paper filter and drip method."

# Concrete implementation: Turkish Coffee Machine
class TurkishCoffeeMachine(CoffeeMachine):
    def make_coffee(self) -> str:
        return "Boiling finely ground coffee with water and sugar in a cezve."

# Concrete implementation: Tasters Choice Coffee Machine
class TastersChoiceCoffeeMachine(CoffeeMachine):
    def make_coffee(self) -> str:
        return "Mixing instant coffee granules with hot water."


class Human:
    def __init__(self, coffee_type: str):
        self.coffee_type = coffee_type.lower()

    def make_coffee(self) -> str:
        if self.coffee_type == "filter":
            return "Brewing coffee using a paper filter and drip method."
        elif self.coffee_type == "turkish":
            return "Boiling finely ground coffee with water and sugar in a cezve."
        elif self.coffee_type == "tasters choice":
            return "Mixing instant coffee granules with hot water."
        else:
            return f"Making {self.coffee_type} coffee in a special way."

# Example usage:
if __name__ == "__main__":
    coffee_makers = [
        FilterCoffeeMachine(),
        TurkishCoffeeMachine(),
        TastersChoiceCoffeeMachine(),
        Human("turkish")
    ]

    for coffe_maker in coffee_makers:
        print(coffe_maker.make_coffee())


    for coffee_machine in coffee_makers:
        print(coffee_machine.description())