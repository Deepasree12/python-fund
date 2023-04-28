nums = []
sum = 0
print("Enter the size of list: ", end="")
tot = int(input())
print("Enter", tot, "Elements for the list: ", end="")
for i in range(tot):
    nums.append(int(input()))
    if nums[i]%2 == 0:
        sum = sum + nums[i]
print("\nSum of Even Numbers =", sum)