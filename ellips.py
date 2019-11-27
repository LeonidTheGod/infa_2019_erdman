c1 = 5
c2 = 6
c3 = 7
a = []
for i in range(1,3+1):
    a.append(locals().get("c"+str(i)))

print(a)

# a = [5, 6, 7]