import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from math import ceil

class Graph:
	def __init__(self,
		title,
		plots,
		plots_in_row=2,
		single=False,
		text=True,
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
		self.fontsize = fontsize
		self.i = 0
		self.i2 = 0
	
	def add_num(self, num):
		self.nums.append(num)

	def plot(self):
		ax = self.axs[self.i, self.i2]
		ln, = ax.plot(self.nums, label=str(self.nums[0]))

		if self.text:
			for data in zip(*ln.get_data(), self.nums):
				ax.text(
					data[0],
					data[1],
					str(round(data[2])),
					fontsize=self.fontsize,
					fontweight='semibold',
					ha='center',
					va='center',
					bbox={
						'boxstyle': 'round',
						'ec': ln.get_color(),
						'fc': (*to_rgb(ln.get_color()), 0.5)
					})

		ax.legend()

		if not self.single:
			self.i2 += 1

			if self.i2 != 0 and self.i2 % self.plots_in_row == 0:
				self.i += 1
				self.i2 = 0

		self.nums = []

	def remove_empty(self):
		if self.single: return

		for i in range(self.plots_in_row - (self.plots % self.plots_in_row)):
			if self.plots % self.plots_in_row == 0:
				break

			self.fig.delaxes(self.axs[self.i, -(i+1)])