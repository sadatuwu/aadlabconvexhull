import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

# Given points
data= []
n = int(input())
for _ in range(n):
    row = row = list(map(float, input().split())) 
    data.append(row)
points = np.array(data)

data.clear()


data = []
lenhull = int(input())
for _ in range(lenhull):
    row = row = list(map(float, input().split())) 
    data.append(row)

hull_points = np.array(data)


# Calculate the convex hull for visualization
hull = ConvexHull(points)

# Plotting all points
plt.scatter(points[:, 0], points[:, 1], label='Points', color='blue')

# Plotting the points in the convex hull
plt.scatter(hull_points[:, 0], hull_points[:, 1], color='red', label='Convex Hull Points')

# Drawing the convex hull
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

# Adding labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Convex Hull Visualization')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
