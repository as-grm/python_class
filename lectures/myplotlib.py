# Python module/package
#
# Author: aleksander.grm@fpp.uni-lj.si
# Date: 24/11/2021
#
# Module contains basic function for diagrams plotting.
#

import matplotlib.pyplot as mplp

# MatPlotLib set LaTeX font
mplp.rcParams['text.usetex'] = True
mplp.rcParams['text.latex.preamble'] = r'\usepackage{siunitx}'

def my_plot(x, y, tit, xl, yl, fn):
    fig, ax = mplp.subplots()
    fig.suptitle(tit)
    
    ax.plot(x,y)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.grid()
    fig.savefig('{:s}.pdf'.format(fn))
