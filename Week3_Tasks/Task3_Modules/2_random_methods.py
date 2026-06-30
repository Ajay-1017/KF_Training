# 2) Generate random numbers and perform statistical operations.

import random

# ============================================================================

# 1) random() -> returns value between 0 to 1 (excludes) in float

print(f"{random.random():.2f}")


# 1.a) uniform(1,6) -> returns value between 1 to 6 (excludes) in float

print(f"{random.uniform(1,6):.2f}")

# ============================================================================

# 2) randint(1,6) -> return values between 1 to 6 (includes) in integer

print(random.randint(1,6))

# ============================================================================

# 3) choice(lst) -> returns only one random value from the iterables

fruits = ["banana","apple","orange","mango","pine apple"]
print(random.choice(fruits))


# 3.a) choices(lst,weights=[18,18,2],k=10) -> returns values accorinding to the k value

# weights -> giving weights to the elements in iterable(higher weights -> higher chances, lower weights -> lower chances)
# k -> how many random values should be generated 

colors =['red','yellow','green']
print(random.choices(colors ,[18,18,4], k=5 ))


# ============================================================================

# 4) shuffle(iterable) -> shuffle the list in-place

deck = list(range(1,53))
print(deck)
random.shuffle(deck)
print(deck)

# ============================================================================

# 5) sample(iterable,key=[]) -> shuffle the list uniquely and with k value 
# k -> how many random values should be generated 

deck = list(range(1,53))
print(random.sample(deck,k=5))

# ============================================================================
