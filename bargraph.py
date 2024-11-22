import matplotlib.pyplot as plt
import numpy as np

# Data given
# n_points = [10, 50, 100, 250, 500]
# steps_graham_scan = [118, 848, 2420, 6644, 15616]
# steps_quick_hull = [285, 2807, 10210, 21034, 51630]


n_points = [20,50,100,200,500] #shormi's data
steps_graham_scan = []
steps_quick_hull = []
for _ in range(5):
    x,y = [int(x) for x in input().split()]
    steps_graham_scan.append(y)
for _ in range(5):
    x,y = [int(x) for x in input().split()]
    steps_quick_hull.append(y)





# Plotting
x = np.arange(len(n_points))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(x - width/2, steps_graham_scan, width, label='Graham Scan', color='skyblue')
bar2 = ax.bar(x + width/2, steps_quick_hull, width, label='Quick Hull', color='lightgreen')

# Labels and title
ax.set_xlabel('Number of Points (n)')
ax.set_ylabel('Steps Taken')
ax.set_title('Steps Comparison Between Graham Scan and Quick Hull')
ax.set_xticks(x)
ax.set_xticklabels(n_points)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
