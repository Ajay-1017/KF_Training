def demo():
    print("Step 1")
    yield "Hello"
    print("Step 2")
gen = demo()
print(next(gen))
print(next(gen))