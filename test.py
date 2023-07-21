import matplotlib
import tkinter as tk
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
# from matplotlib import style
from matplotlib.backends._backend_tk import FigureCanvasTk, NavigationToolbar2Tk
from matplotlib.figure import Figure


class GraphPage(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.title_label = tk.Label(self, text="Graph Page Example")
        self.title_label.pack()
        self.pack()

    def add_mpl_figure(self, fig):
        self.mpl_canvas = FigureCanvasTk(fig, self)
        plt.show()
        self.mpl_canvas.show()
        self.mpl_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.mpl_canvas, self)
        self.toolbar.update()
        self.mpl_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class MPLGraph(Figure):

    def __init__(self):
        Figure.__init__(self, figsize=(5, 5), dpi=100)
        self.plot = self.add_subplot(111)
        self.plot.plot([1, 2, 3, 4, 5, 6, 7], [4, 3, 5, 0, 2, 0, 6])


fig = MPLGraph()

root = tk.Tk()
graph_page = GraphPage(root)
graph_page.add_mpl_figure(fig)

root.mainloop()