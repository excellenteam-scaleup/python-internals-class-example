# example.py

def add_numbers(a, b):
  return a+b

def greet(name):
    print(f"Hello, {name}!")

x = add_numbers(1, 2)
y = add_numbers("one", 2)  # Mixing types (will cause pylint warning)
greet("Alice")
