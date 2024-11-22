import math
def customsort(points):
    pivot = min(points, key=lambda p: (p[1], p[0]))
    def polar_angle(p):
        return math.atan2(p[1] - pivot[1], p[0] - pivot[0])
    def distance(p):
        return (p[0] - pivot[0]) ** 2 + (p[1] - pivot[1]) ** 2
    points = sorted(points, key=lambda p: (polar_angle(p), distance(p)))
    return points

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

points = []
with open("input.txt", 'r') as file:
    n = int(file.readline().strip())
    for _ in range(n):
        x, y = map(int, file.readline().strip().split())
        points.append((x, y))

points = customsort(points)
hull = []

for point in points:
    while len(hull) >= 2 and cross_product(hull[-2], hull[-1], point) <= 0:
        hull.pop()
    hull.append(point)

# print("given points:")
print(len(points))
for point in points:
    print(point[0], point[1])

# print("points in Convex Hull:")
print(len(hull))
for point in hull:
    print(point[0], point[1])