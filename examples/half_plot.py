from pltsci import whole_plot_set, half_plot_set, set_ticks, cm
import matplotlib.pyplot as plt
import numpy as np

# 设置全局绘图参数
whole_plot_set()  # 全宽图片参数设置，即使是用半宽图，也建议先调用此函数设置全局参数
fig, ax = plt.subplots(figsize=(7 * cm, 5 * cm), dpi=300)  # 创建图形 (使用厘米单位)
half_plot_set(ax)  # 半宽图片参数设置

# 创建示例数据
x = np.linspace(0, 10, 100)
y = np.exp(x)

ax.plot(x, y, label="$y=e^x$")

# 设置坐标轴范围和刻度
set_ticks(ax, xrange=(0, 10, 2), yrange=(0, 22000, 5000))

# 添加标签和图例
ax.set_xlabel("x", fontsize=10)
ax.set_ylabel("y", fontsize=10)
ax.legend(frameon=False, fontsize=10)


plt.tight_layout()
fig.savefig("examples/half_plot.svg", bbox_inches="tight", transparent=True)
# fig.savefig("examples/half_plot.jpg", bbox_inches="tight", dpi=1200) # 位图记得设置高分辨率
