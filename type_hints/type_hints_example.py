from typing import List, Dict, Tuple, Union, Optional, Any, Sequence, Callable, TypeVar, Generic

# Basic typing

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

def get_coordinates() -> Tuple[float, float]:
    return (32.1, 34.8)

def get_settings() -> Dict[str, Union[str, int]]:
    return {"theme": "dark", "timeout": 30}

# Type Aliases (Custom Types)

UserId = int
UserData = Dict[str, Union[str, int]]

def get_user(user_id: UserId) -> UserData:
    return {"name": "Alice", "age": 30}

# Optional and Union

def parse_value(value: Union[int, str]) -> str:
    return str(value)

def find_user(name: str) -> Optional[Dict[str, Any]]:
    if name == "Alice":
        return {"name": "Alice", "age": 30}
    return None

# Any and Sequence

def process_items(items: Sequence[Any]) -> None:
    for item in items:
        print(f"Processing item: {item}")

# Callable with Decorator

def logger(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a: int, b: int) -> int:
    return a + b






from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Product:
    name: str
    price: float
    tags: Optional[List[str]] = None
    in_stock: bool = True

    def display(self) -> str:
        return f"{self.name}: ${self.price}"

# Usage example
item = Product(name="Laptop", price=999.99, tags=["electronics", "computer"])
print(item.display())
print(item.tags)







T = TypeVar("T")

def repeat(item: T, times: int) -> list[T]:
    return [item for _ in range(times)]

# Usage
numbers = repeat(42, 3)        # Inferred as list[int]
strings = repeat("hello", 2)   # Inferred as list[str]


Number = TypeVar("Number", int, float)

def add_numbers(a: Number, b: Number) -> Number:
    return a + b


# Generics

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

    def get_content(self) -> T:
        return self.content

int_box = Box(42)
str_box = Box("Hello")

# Usage examples

if __name__ == "__main__":
    print(greet("Bob", 25))
    print(get_coordinates())
    print(get_settings())
    print(get_user(101))
    print(parse_value("hello"))
    print(parse_value(42))
    print(find_user("Alice"))
    print(find_user("Bob"))
    process_items([1, "two", 3.0])
    add(2, 3)
    print(int_box.get_content())
    print(str_box.get_content())
