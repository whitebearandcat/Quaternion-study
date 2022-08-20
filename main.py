"""
Quaternionで3次元空間を回転する
https://qiita.com/shirokumaneko/private/399d20a2652fe333a346
"""

import numpy as np
from numpy import pi
from matplotlib import pyplot as plt

from transformation import quaternion_rotate,to_quaternion

## 座標軸上の点

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.grid(False)
ax.axis("off")

# 座標軸
ax.quiver([0,0,0], [0,0,0], [0,0,0], [3,0,0], [0,3,0], [0,0,3], arrow_length_ratio=0.1, color="black")
ax.text(3.5, 0, 0, "x")
ax.text(0, 3.5, 0, "y")
ax.text(0, 0, 3.5, "z")

# 回転軸
ax.plot([0,1.5], [0,1.5], [0,1.5], color="black", linewidth=1)
ax.text(1.6, 1.6, 1.6, "q = (1,1,1)")

ax.set_box_aspect((1,1,1))
ax.set_xlim(-1,4)
ax.set_ylim(-1,4)
ax.set_zlim(-1,4)

# 座標軸上の点
a = np.array([1,0,0])
b = np.array([0,1,0])
c = np.array([0,0,1])

ax.plot(a[0], a[1], a[2], marker="o", markersize=10)
ax.plot(b[0], b[1], b[2], marker="s", markersize=10)
ax.plot(c[0], c[1], c[2], marker="^", markersize=10)

plt.show()


## 60°回転

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.grid(False)
ax.axis("off")

# 座標軸
ax.quiver([0,0,0], [0,0,0], [0,0,0], [3,0,0], [0,3,0], [0,0,3], arrow_length_ratio=0.1, color="black")
ax.text(3.5, 0, 0, "x")
ax.text(0, 3.5, 0, "y")
ax.text(0, 0, 3.5, "z")

# 回転軸
ax.plot([0,1.5], [0,1.5], [0,1.5], color="black", linewidth=1)
ax.text(1.6, 1.6, 1.6, "q = (1,1,1)")

ax.set_box_aspect((1,1,1))
ax.set_xlim(-1,4)
ax.set_ylim(-1,4)
ax.set_zlim(-1,4)

q = to_quaternion([1,1,1], pi/3)
a = quaternion_rotate(a, q)
b = quaternion_rotate(b, q)
c = quaternion_rotate(c, q)

ax.plot(a[0], a[1], a[2], marker="o", markersize=10)
ax.plot(b[0], b[1], b[2], marker="s", markersize=10)
ax.plot(c[0], c[1], c[2], marker="^", markersize=10)

plt.show()
