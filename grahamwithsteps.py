import math

step_counter = 0

def customsort(points):
    global step_counter
    pivot = min(points, key=lambda p: (p[1], p[0]))
    step_counter += len(points)

    def polar_angle(p):
        global step_counter
        step_counter += 1
        return math.atan2(p[1] - pivot[1], p[0] - pivot[0])

    def distance(p):
        global step_counter
        step_counter += 1
        return (p[0] - pivot[0]) ** 2 + (p[1] - pivot[1]) ** 2

    points = sorted(points, key=lambda p: (polar_angle(p), distance(p)))
    step_counter += len(points) * math.ceil(math.log2(len(points)))
    return points

def cross_product(o, a, b):
    global step_counter
    step_counter += 1
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

with open("inputsteps.txt", 'r') as file:
    t = int(file.readline().strip())
    for _ in range(t):
        points = []
        n = int(file.readline().strip())
        for _ in range(n):
            x, y = map(int, file.readline().strip().split())
            points.append((x, y))
            step_counter += 1

        points = customsort(points)
        hull = []

        for point in points:
            step_counter += 1
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], point) <= 0:
                hull.pop()
                step_counter += 1
            hull.append(point)
            step_counter += 1

        # print("given points:")
        # for point in points:
        #     print(point[0], point[1])

        # print("points in Convex Hull:")
        # for point in hull:
        #     print(point[0], point[1])

        # print("\nTotal steps taken by the algorithm:", step_counter)
        print(n,step_counter)