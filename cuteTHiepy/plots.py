import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

class origin_like:
    def subplots(NSubs):
        matplotlib.rcParams['mathtext.fontset'] = 'custom'
        matplotlib.rcParams['mathtext.rm'] = 'Calibri'
        matplotlib.rcParams['mathtext.it'] = 'Calibri'
        matplotlib.rcParams['mathtext.bf'] = 'Calibri'
        matplotlib.rcParams['xtick.major.pad']='5'
        matplotlib.rcParams['ytick.major.pad']='5'
        matplotlib.rcParams['axes.linewidth'] = 0.5
        
        font = {'weight' : 'normal',
                'size'   : 16,
                'family' : "calibri"}
        plt.rc('font', **font)
        plt.tight_layout()
        fig,axs=plt.subplots(NSubs,1, figsize=(3.45 , 3.1), dpi = 300,layout="constrained")
        #fig.subplots_adjust(hspace=0, wspace=0.32)
        return fig,axs
    def set_xlabel(ax,xlabel1,xunit1=None):
        ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$ / $\mathrm{{{xunit1}}}$') if xunit1 is not None else ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$ /-') 
    def set_ylabel(ax,ylabel1,yunit1=None):
        ax.set_ylabel(f'\n \n $\mathrm{{{ylabel1}}}$ \n / $\mathrm{{{yunit1}}}$',rotation=0,loc="top",linespacing=1.5) if yunit1 is not None else ax.set_ylabel(f'\n \n $\mathrm{{{ylabel1}}}$ \n / -',rotation=0,loc="top",linespacing=1.5)
    def plot(ax,x,y,Formatstring,label=None):
        ax.plot(x,y,Formatstring , zorder=1,linewidth = 1.5,label=label)
    def scatter(ax,x,y,Formatstring,label=None):
        ax.plot(x,y,Formatstring,markersize=5.5, zorder=2, linewidth=0.5, markeredgecolor='k',markeredgewidth=0.5,label=label)
    def set_ticks(ax,x0=None,x1=None,y0=None,y1=None):
        ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=True, left=True, right=True, direction="in",length=6, width=0.5)
        if x0 is not None: ax.axis([x0, x1, y0, y1]) 
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(start, end, 5))
        start, end = ax.get_ylim()
        ax.yaxis.set_ticks(np.linspace(start, end, 5))
        plt.show()



df=pd.read_csv("Werte2.txt", encoding = "utf-8", sep=",", header=None)

# Anzahl Subplots = Anzahl x-Achsen
Boolarr=df.values[0,:]=="x"
NSubs=Boolarr.sum()

# Anzahl subplots erstellen
#fig, axs = plt.subplots(NSubs)

fig, axs = origin_like.subplots(NSubs)
# Plotten
k=-1
for i in range(df.columns.size):
    # x achse auslesen
    if (df.values[0,i]=="x"):
        k+=1
        xlabel=df.values[1,i]
        xunit=df.values[2,i]
        x=df.values[5:,i]
    else:    
        ylabel=df.values[1,i]
        yunit=df.values[2,i]
        legend=df.values[3,i]
        Formatstring=df.values[4,i]
        y=df.values[5:,i]
        
        # Plotten mit Formatierung
        ax=axs[k] if (NSubs!=1) else axs
        origin_like.plot(ax,x.astype(float),y.astype(float), Formatstring, label=legend)  
        origin_like.scatter(ax,x.astype(float),y.astype(float), "ro", label=legend)             
        origin_like.set_xlabel(ax,xlabel,xunit)
        origin_like.set_ylabel(ax,ylabel,yunit)
        origin_like.set_ticks(ax)
        ax.legend(loc="upper left")
fig.canvas.draw_idle()
# 
# plt.show()