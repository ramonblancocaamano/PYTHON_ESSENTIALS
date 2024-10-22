h = [1,2,3,1,2,3,4,5,5,5,6,6,6,6,6,4,3,3,3]
n = []
for x in h:
    if x not in n:
        n.append(x)

print(n)
print(list(set(h)))

