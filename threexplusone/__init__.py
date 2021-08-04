import matplotlib.pyplot as _plt
from .graph import Graph

def _get_num(num):
    if num % 2 == 0:
        return num / 2
    else:
        return (num * 3) + 1

def _plot(num, graph):
    graph.add_num(num)
    n = num

    while n != 1:
        n = _get_num(n)
        graph.add_num(n)

    graph.plot()

def show(
    nums,
    title='3x+1',
    plots_in_row=2,
    figsize=(15, 7.4),
    single=False,
    text=True,
    fontsize=6,
    auto_text_hiding=True,
    text_limit=50,
    highest_text_only=False,
    nowindow=False,
    outfile=None
):
    graph = Graph(
        title,
        len(nums) if type(nums) != int else 1,
        plots_in_row=plots_in_row,
        single=single,
        text=text,
        fontsize=fontsize,
        figsize=figsize,
        auto_text_hiding=auto_text_hiding,
        text_limit=text_limit,
        highest_text_only=highest_text_only
    )

    if type(nums) == list:
        for n in nums:
            _plot(n, graph)
    else:
        _plot(nums, graph)

    graph.remove_empty()

    if not graph.single:
        _plt.tight_layout()

    if outfile:
        _plt.savefig(outfile)

    if not nowindow:
        _plt.show()
