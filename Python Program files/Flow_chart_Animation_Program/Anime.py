import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation, PillowWriter

# Define nodes (x, y, label)
nodes = {
    "main": (8, 5, "main.py"),
    "raw_data": (8, 9, "Real estate\n(RAW DATA)"),
    "split": (4, 7, "splitting.py"),
    "read_dfs": (4, 3, "read_dfs.py"),
    "dateconv": (12, 7, "dateconversion.py"),
    "datatype": (2, 5, "datatype_utils.py"),
    "sql_gen": (12, 3, "sql_generator.py"),
    "database": (15, 5, "Database (MySQL)"),
    "powerbi": (20, 5, "Power BI"),
    "dashboard": (21, 3, "Dashboard"),
}

# Define edges (connections)
edges = [
    ("raw_data", "main"),
    ("main", "split"),
    ("main", "datatype"),
    ("main", "read_dfs"),
    ("main", "dateconv"),
    ("main", "sql_gen"),
    ("main", "database"),
    ("database", "powerbi"),
    ("powerbi", "dashboard"),
]

fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim(0, 25)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title("ETL Pipeline - Flow Animation", fontsize=14, weight='bold', pad=20)

# Draw nodes (boxes)
for key, (x, y, label) in nodes.items():
    rect = patches.FancyBboxPatch((x - 1.2, y - 0.6), 4.0, 1.0,                                  boxstyle="round,pad=0.2",
                                   edgecolor="black", facecolor="lightyellow")
    ax.add_patch(rect)
    ax.text(x, y, label, ha="center", va="center", fontsize=10, wrap=True)

# Initialize arrows
arrows = []

def init():
    return arrows

# Animate arrows one by one
def animate(i):
    if i < len(edges):
        start, end = edges[i]
        x1, y1, _ = nodes[start]
        x2, y2, _ = nodes[end]
        arrow = ax.annotate("",
                            xy=(x2, y2), xycoords='data',
                            xytext=(x1, y1), textcoords='data',
                            arrowprops=dict(arrowstyle="->", lw=2, color="blue"))
        arrows.append(arrow)
    return arrows

ani = FuncAnimation(fig, animate, frames=len(edges), interval=5, repeat=False)
ani.save("C:/Users/anura/OneDrive/Desktop/Real Estate Data/etl_diagram_flow.gif", writer=PillowWriter(fps=1))
print("✅ Animation saved as 'etl_diagram_flow.gif'")
