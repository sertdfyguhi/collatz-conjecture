import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from math import ceil

def add_text(ax, data, fontsize, color):
    ax.text(
        data[0],
        data[1],
        str(round(data[2])),
        fontsize=fontsize,
        fontweight='semibold',
        ha='center',
        va='center_baseline',
        bbox={
            'boxstyle': 'round',
            'ec': color,
            'fc': (*to_rgb(color), 0.7)
        })

class Graph:
    def __init__(self,
        title,
        plots,
        plots_in_row=2,
        single=False,
        text=True,
        auto_text_hiding=True,
        text_limit=50,
        highest_text_only=False,
        fontsize=6,
        figsize=(15, 7.4),
    ) -> None:
        self.fig, self.axs = plt.subplots(
            ceil(plots / plots_in_row) if not single else 1,
            plots_in_row if not single else 1,
            squeeze=False,
            figsize=figsize)
        self.fig.suptitle(title)
        self.nums = []
        self.plots = plots
        self.plots_in_row = plots_in_row
        self.single = single
        self.text = text
        self.auto_text_hiding = auto_text_hiding
        self.text_limit = text_limit
        self.highest_text_only = highest_text_only
        self.fontsize = fontsize
        self.i = 0
        self.i2 = 0
    
    def add_num(self, num):
        self.nums.append(num)

    def plot(self):
        ax = self.axs[self.i, self.i2]
        ln, = ax.plot(self.nums, label=str(self.nums[0]))

        if self.text:
            if self.highest_text_only:
                m = max(self.nums)
                i = self.nums.index(m)
                data = (i, m, m)
                add_text(ax, data, self.fontsize, ln.get_color())
            else:
                for data in zip(*ln.get_data(), self.nums):
                    if self.auto_text_hiding and len(self.nums) > self.text_limit:
                        break

                    add_text(ax, data, self.fontsize, ln.get_color())

        ax.legend()

        if not self.single:
            self.i2 += 1

            if self.i2 != 0 and self.i2 % self.plots_in_row == 0:
                self.i += 1
                self.i2 = 0

        self.nums.clear()

    def remove_empty(self):
        if self.single: return

        for i in range(self.plots_in_row - (self.plots % self.plots_in_row)):
            if self.plots % self.plots_in_row == 0:
                break

            self.fig.delaxes(self.axs[self.i, -(i+1)])