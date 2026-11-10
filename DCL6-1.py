s1 = {10, 20, 30, 40, 60, 70}
s2 = {"fruit", "Veggies", "cookies", "chips"}
print(s1)
# discard removes the object from the set if obj not present it will not give any error
s1.discard(30)
print(s1)
s1.discard(300)
print(f"Discard after removing non existent(300) element: {s1}")
print(s2)
s2.clear()  # removes/clears the all elements from set
print(f"After using Clear: {s2}")
s3 = {10, 20, 50}
s4 = {10, 20, 40}
# subset returns true if all the elements of 1st set is availabel in 2nd set
bol_1 = s3.issubset(s1)
bol_2 = s4.issubset(s1)
print(f"Subset Verification s3,s1: {bol_1}")
print(f"Subset Verification s4,s1: {bol_2}")
# superset returns true if all the elements of 2nd set is availabel in 1st set
bol_3 = s1.issuperset(s3)
bol_4 = s1.issuperset(s4)
print(f"Superset Verification s1,s3: {bol_3}")
print(f"Superset Verification s1,s4: {bol_4}")
s5 = {1, 2, 3, 4, 5}
# disjoint it returns false when there is atleast one element is common between both sets
bol_5 = s1.isdisjoint(s4)
bol_6 = s1.isdisjoint(s5)
print(f"Disjoint Verification s1,s4: {bol_5}")
print(f"Disjoint Verification s1,s5: {bol_6}")
# Union it returns a new set that contains unique elements of both sets together
us = s1.union(s5)
print(f"Union fun of set s1,s5: {us}")
# Intersection it returns a new set that contains only common elements of both sets
Is = s1.intersection(s4)
print(f"Intersect fun of set s1,s4: {Is}")
# Difference it returns a new set where in all the elements of 1st set that are not present in set 2
Ds = s1.difference(s4)
print(f"Difference of sets s1,s4: {Ds}")
# Symmmetric_difference it returns  a new set that contains the uncommon elements of both sets
sd = s1.symmetric_difference(s3)
print(f"Symmetric Difference of sets s1,s3: {sd}")
