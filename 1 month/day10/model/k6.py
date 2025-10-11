nums = []

for i in range(5):
    n = int(input(f"Enter number #{i+1}: "))
    nums.append(n)

print("Highest:",max(nums))
print("Lowest",min(nums))