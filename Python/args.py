def sum(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sum(10, 20, 30)

def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display(name="John", age=30, city="New York")