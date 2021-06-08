car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

list_CarParts = {"wheels", "doors", "exhaust"}
print(set(list_CarParts))

a = [1,2,2,3,3]
print(len(a)==len(set(a)))

(car_parts.add("windows"))
print(car_parts)

car_parts.remove("doors")
print(car_parts)

car_parts.discard("windows")
print(car_parts)

x = frozenset([1,2,3,4])
print(x)


