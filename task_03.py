x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

tup1 = (x1,y1)
tup2 = (x2,y2)

#√((x2-x1)² + (y2-y1)²)
distance = ((tup2[0] - tup1[0])**2 + (tup2[1] - tup1[1])**2) ** 0.5

print(f"{distance:.2f}")
