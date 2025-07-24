# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:24:26 2025

@author: anura
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation, PillowWriter

# Define nodes (x, y, label)
nodes = {
    "Overview": (3, 9, "Overview"),
    "Sales Analysis": (3, 3, "Sales Analysis"),
    "Property Details": (10, 3, "Property Details"),
    "Remarks & Insights": (10, 9, "Remarks & Insights"),
    "Data Quality": (17, 9, "Data Quality")
}

# Define edges (connections)
edges = [
    ("Overview", "Sales Analysis"),
    ("Sales Analysis", "Property Details"),
    ("Property Details", "Remarks & Insights"),
    ("Remarks & Insights", "Data Quality"),
]

fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim(0, 25)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title("Flow Animation (Power BI)", fontsize=14, weight='bold', pad=20)

# Draw nodes (boxes)
for key, (x, y, label) in nodes.items():
    rect = patches.FancyBboxPatch((x - 2.5, y - 0.6), 5.0, 1.0,                                  boxstyle="round,pad=0.2",
                                   edgecolor="black", facecolor="lightyellow")
    ax.add_patch(rect)
    ax.text(x, y, label, ha="center", va="center", fontsize=12, weight = "bold", wrap=True)

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
ani.save("C:/Users/anura/OneDrive/Desktop/Real Estate Data/Python Program files/Flow_chart_Animation_Program (Power BI)/Flow Animation (Power BI).gif", writer=PillowWriter(fps=1))
print("✅ Animation saved as 'Flow Animation (Power BI)'")
