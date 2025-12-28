from pltsci import whole_plot_set, set_ticks, cm
import matplotlib.pyplot as plt
import numpy as np

# 设置全局绘图参数
whole_plot_set()  # 全宽图片参数设置
fig, ax = plt.subplots(figsize=(15 * cm, 10 * cm), dpi=300)  # 创建图形 (使用厘米单位)

# 创建示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y, label="$y=\\sin(x)$")

# 设置坐标轴范围和刻度
set_ticks(ax, xrange=(0, 10, 2), yrange=(-1.5, 1.5, 0.5))

# 添加标签和图例
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.legend(frameon=False, fontsize=12)

plt.tight_layout()
fig.savefig("examples/whole_plot.svg", bbox_inches="tight", transparent=True)
# fig.savefig("examples/whole_plot.jpg", bbox_inches="tight", dpi=1200) # 位图记得设置高分辨率