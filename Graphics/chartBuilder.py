import logging
import traceback
import matplotlib
matplotlib.use('agg')
import pylab as pl
import numpy as np
from Application.settings import Settings


class ChartBuilder():
    color1 = Settings().frontend_mainColor
    color2 = "grey"
    fileName = Settings().charts_fileName

    def buildRadarChart(self, titles, labels, data=None):
        try:
            fig = pl.figure(figsize=(5, 5))
            radar_stat = Radar(fig,
                               titles=labels,
                               labels=[[20, 40, 60, 80, 100],
                                       [20, 40, 60, 80, 100],
                                       [20, 40, 60, 80, 100],
                                       [20, 40, 60, 80, 100],
                                       [20, 40, 60, 80, 100]])

            radar_stat.plot(data[0], "-", lw=2, color=ChartBuilder.color1, alpha=0.8, label=titles[0])
            radar_stat.fill(data[0], colores=ChartBuilder.color1)
            if len(data)>1 and len(titles) > 1:
                radar_stat.plot(data[1], "-", lw=2, color="#424242", alpha=0.8, label=titles[1])
                radar_stat.fill(data[1], colores=ChartBuilder.color2)
            radar_stat.ax.legend()

            fig.savefig(ChartBuilder.fileName)

            return True
        except Exception as e:
            logging.error("searchFields ({0}): {1}".format(e, traceback.format_exc()))
            return False


class Radar(object):
    def __init__(self, fig, titles, labels, rotation=0, rect=None):

        if rect is None:
            rect = [0.05, 0.05, 0.88, 0.88]

        self.n = len(titles)
        self.angles = np.arange(0, 360, 360.0 / self.n)

        self.axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i) for i in range(self.n)]

        self.ax = self.axes[0]
        self.ax.set_thetagrids(self.angles, labels=titles, fontsize=10, fontweight='bold')

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)

        for ax, angle, label in zip(self.axes, self.angles, labels):
            ax.set_rgrids(range(20, 120, 20), angle=angle, labels=label, fontsize=8)
            ax.spines["polar"].set_visible(False)
            ax.set_ylim(0, 100)
            ax.set_theta_offset(np.deg2rad(90))

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)

    def fill(self, values, colores):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.fill_between(angle, values, alpha="0.7", color=colores)

