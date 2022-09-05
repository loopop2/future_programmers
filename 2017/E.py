# NOT COMPLETED
# كنت اسويه فالحصه بس خلصت الحصه
platforms = int(input("Enter the number of platforms: "))
while platforms < 1 or platforms > 300: platforms = int(input("Enter the number of platforms: "))
platform_values = [int(input(f"Enter the {x+1} value of your platform: ")) for x in range(platforms)]
platform_values.sort()
curr_value = platform_values[0]
jumps = 0
poped = platform_values.pop(0)
for i in platform_values:
    if curr_value >= i - 60 and curr_value <= i + 60:
        curr_value = i

    if i - 60 < curr_value or i + 60 > curr_value:
        jumps+=1
print(jumps)
