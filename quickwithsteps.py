hull = set()
step_counter = 0

def findSide(p1, p2, p):
    global step_counter
    step_counter += 1
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def lineDist(p1, p2, p):
    global step_counter
    step_counter += 1
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

def quickHull(a, n, p1, p2, side):
    global step_counter
    step_counter += 1
    ind = -1
    max_dist = 0
    for i in range(n):
        step_counter += 1
        temp = lineDist(p1, p2, a[i])
        if (findSide(p1, p2, a[i]) == side) and (temp > max_dist):
            ind = i
            max_dist = temp
            step_counter += 1
    if ind == -1:
        hull.add("$".join(map(str, p1)))
        hull.add("$".join(map(str, p2)))
        step_counter += 2
        return
    quickHull(a, n, a[ind], p1, -findSide(a[ind], p1, p2))
    quickHull(a, n, a[ind], p2, -findSide(a[ind], p2, p1))

def makehull(a, n):
    global step_counter
    step_counter += 1
    min_x = 0
    max_x = 0
    for i in range(1, n):
        step_counter += 1
        if a[i][0] < a[min_x][0]:
            min_x = i
            step_counter += 1
        if a[i][0] > a[max_x][0]:
            max_x = i
            step_counter += 1
    quickHull(a, n, a[min_x], a[max_x], 1)
    quickHull(a, n, a[min_x], a[max_x], -1)

with open("inputsteps.txt", 'r') as file:
    t = int(file.readline().strip())
    for _ in range(t):
        points = []
        n = int(file.readline().strip())
        for _ in range(n):
            x, y = map(int, file.readline().strip().split())
            points.append((x, y))

        makehull(points, n)

        # print("given points:")
        # for point in points:
        #     print(point[0], point[1])
            
        # print("points in Convex Hull:")
        # for element in hull:
        #     x = element.split("$")
        #     print(x[0], x[1])

        # print("\nTotal steps taken by the algorithm:", step_counter)
        print(n,step_counter)
