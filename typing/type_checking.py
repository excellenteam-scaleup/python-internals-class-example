from typing import get_type_hints
from duck_typing_potential_bugs import Human, TastersChoiceCoffeeMachine, TurkishCoffeeMachine, FilterCoffeeMachine, CoffeeMachine

if __name__ == "__main__":
    h1 = Human("turkish")
    h2 = Human("filter")

    # Check type with isinstance
    print(isinstance(h1, Human))  # True
    print(isinstance(h1, object)) # True (because everything is an object in Python)

    # Check exact type with type()
    print(type(h1) == Human)      # True
    print(type(h1) == object)     # False

    # issubclass example
    print(issubclass(Human, object))  # True

    # hasattr: Does Human have a 'make_coffee' method?
    print(hasattr(h1, 'make_coffee'))  # True

    # getattr: Get the method itself
    coffee_method = getattr(h1, 'make_coffee')
    if callable(coffee_method):
        print(coffee_method())  # Calls the method

    # Use typing functions
    annotations = get_type_hints(Human.__init__)
    print(annotations)  # {'coffee_type': <class 'str'>, 'return': <class 'NoneType'>}

    # Check if an attribute is callable (a function or method)
    print(callable(h1.make_coffee))  # True
    print(callable(h1.coffee_type))  # False

    # Dynamic attribute access and safety
    if hasattr(h1, 'nonexistent_attribute'):
        print(getattr(h1, 'nonexistent_attribute'))
    else:
        print("This attribute doesn't exist.")

    # Type name introspection
    print(type(h1).__name__)  # 'Human'


