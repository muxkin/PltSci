# 测试使用示例
from pltsci import whole_plot_set, set_ticks, half_plot_set, cm
import matplotlib.pyplot as plt
import numpy as np

# 设置全局绘图参数
whole_plot_set()

# 创建示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图形
fig, ax = plt.subplots(figsize=(cm(12), cm(8)))
ax.plot(x, y, label='sin(x)')

# 设置坐标轴
set_ticks(ax, xrange=(0, 10, 2), yrange=(-1, 1, 0.5))
half_plot_set(ax)

# 添加标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

plt.tight_layout()
plt.show()