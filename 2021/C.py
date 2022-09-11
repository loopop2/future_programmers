n,k = [int(x) for x in input("Enter: ").split(" ")]
loc = [int(x) for x in input("Locations: ").split(" ")]
loc.sort()
base=loc[0]
curr=loc[0]
needed=[]
for i in loc:
    if i >= curr and i <= base + k:
        curr = i
    else:
        needed.append(i)
        base=i

print(needed)
