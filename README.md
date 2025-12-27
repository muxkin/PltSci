# PltSci

一个用于简化 matplotlib 绘图参数设置的 Python 工具库。

## 特性

- 🎨 快速设置科学绘图风格（Times New Roman 字体，内向刻度线等）
- 📏 厘米到英寸的便捷转换工具
- 🎯 简洁的坐标轴范围和刻度设置接口
- ✨ 适用于学术论文和科学报告的图表制作

## 安装

```bash
pip install pltsci
```

## 快速开始

```python
from pltsci import whole_plot_set, set_ticks, half_plot_set, cm
import matplotlib.pyplot as plt
import numpy as np

# 设置全局绘图参数
whole_plot_set()

# 创建示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图形 (使用厘米单位)
fig, ax = plt.subplots(figsize=(cm(12), cm(8)))
ax.plot(x, y, label='sin(x)')

# 设置坐标轴范围和刻度
set_ticks(ax, xrange=(0, 10, 2), yrange=(-1, 1, 0.5))

# 应用精细的轴样式
half_plot_set(ax)

# 添加标签和图例
ax.set_xlabel('x')
ax.set_ylabel('y') 
ax.legend()

plt.tight_layout()
plt.show()
```

## API 参考

### `whole_plot_set(font=None, math_font="stix")`
设置全局绘图参数，包括字体、刻度方向、图例样式等。

- `font`: 字体列表，默认为 `["Times New Roman", "SimSun"]`
- `math_font`: 数学公式字体，默认为 `"stix"`

### `set_ticks(ax, xrange=None, yrange=None)`
设置坐标轴范围和刻度。

- `ax`: matplotlib 轴对象
- `xrange`: x轴范围，格式为 `(xmin, xmax, xstep)`
- `yrange`: y轴范围，格式为 `(ymin, ymax, ystep)`

### `half_plot_set(ax)`
设置坐标轴线宽和刻度样式，适用于密集布局的图表。

- `ax`: matplotlib 轴对象

### `cm` / `cm_to_inch`
厘米到英寸转换工具。

```python
# 两种使用方式
fig, ax = plt.subplots(figsize=(cm(12), cm(8)))
# 或者
fig, ax = plt.subplots(figsize=(cm_to_inch(12), cm_to_inch(8)))
```

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！
