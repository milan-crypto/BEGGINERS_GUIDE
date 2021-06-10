with open("/Users/milancosgrove/Desktop/ADVENT OF CODE/DAY 1.txt", "r") as fp:
    num = fp.readlines()
# print(num)
num = [int(i.split("\n")[0]) for i in num]
print("Solution: 1\n")
# solution 1
for i in num:
    if 2020 - i in num:
        print(i, 2020 - i, i * (2020 - i))

print("Solution: 2\n")

# solution 2
for i in num:
    for j in num:
        if (2020 - i - j) in num:
            print(2020 - i - j, i, j)
