def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))            # ✅ Ok: str input
print(greet(f"User {42}"))       # ✅ Ok: f-string is still str
print(greet(str(123)))           # ✅ Ok: explicit str
print(greet("42"))               # ✅ Ok: numeric string
print(greet("😊"))               # ✅ Ok: emoji string

print(greet(42))                 # ❌ Type checker error: int instead of str
print(greet(3.14))               # ❌ Type checker error: float instead of str
print(greet(["Alice", "Bob"]))   # ❌ Type checker error: list instead of str
print(greet(None))               # ❌ Type checker error: NoneType instead of str
print(greet({'name': 'Alice'}))  # ❌ Type checker error: dict instead of str

class BadStr:
    def __str__(self):
        raise ValueError("Cannot convert to string")

obj = BadStr()
# print(greet(obj))  # 🚨 Will raise ValueError: Cannot convert to string


def iterate_over(iterable):
    for i in iterable:
        print(i)

print(iterate_over([1,2,3,4]))
print(iterate_over({1, 2, 3, 4}))
print(iterate_over(1))
