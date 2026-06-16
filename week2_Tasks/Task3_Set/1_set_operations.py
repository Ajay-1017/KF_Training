s1 = {1,1,1,2,2,3,4}

s2 = {4,5,6,7,8}

s1.add(5)

s1.discard(6)

s1.remove(3)

print(s1)
print(s2)

# UNION (COMBINE VALUES)
print(s1|s2)
print(s1.union(s2))


#INTERSECTION (COMMON VALUES)
print(s1&s2)
print(s1.intersection(s2))


#DIFFERNCE (ONLY BELONGS S1 )
print(s1-s2)
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))


# SYMETRIC DIFFERENCE (NOT COMMON VALUES)
print(s1^s2)
print(s1.symmetric_difference(s2))


print(set((1,2,2,3,4,5,5,6)))