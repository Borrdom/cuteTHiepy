
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
def circular(t,zvec,wtz,Lt=None,instances=6,comp=0,cmap="Blues"):
    L=zvec[-1]
    expansion=Lt[:,None]/L if Lt is not None else np.ones_like(t)
    phi=np.linspace(0,2*np.pi,41)
    Rad,Phi=np.meshgrid(zvec*1E6,phi)
    fig, axes = plt.subplots(2,instances//2, constrained_layout=True,subplot_kw={'projection': 'polar'})
    # axes=[]
    axes=axes.flatten()
    pls=[]
    delt=len(t)//instances
    for i in range(instances):
        axes[i].grid(False)
        # axes.append(fig.add_subplot(2,instances//2,i+1, polar=True))
        pls.append(axes[i].contourf(Phi,Rad*expansion[delt*i],np.meshgrid(wtz[delt*i,comp,:],phi)[0],cmap=cmap,vmin=0, vmax=1))
        axes[i].grid(False)
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_ylim(0, np.max(zvec*1E6*expansion))
        axes[i].spines['polar'].set_visible(False)
        axes[i].set_title(f'{t[delt*i]/60:.2f}'+" min", va='bottom')

    axes=np.asarray(axes)
      
    fig.colorbar(pls[0], ax=axes.ravel().tolist(),orientation="horizontal")
    fig.subplots_adjust(hspace=0,wspace=0)  

class origin_like:
    def subplots():
        matplotlib.rcParams['mathtext.fontset'] = 'custom'
        matplotlib.rcParams['mathtext.rm'] = 'Calibri'
        matplotlib.rcParams['mathtext.it'] = 'Calibri'
        matplotlib.rcParams['mathtext.bf'] = 'Calibri'
        matplotlib.rcParams['xtick.major.pad']='10'
        matplotlib.rcParams['ytick.major.pad']='10'
        matplotlib.rcParams['axes.axisbelow'] = True
        font = {'weight' : 'normal',
                'size'   : 28,
                'family' : "calibri"}
        plt.rc('font', **font)
        fig,axs=plt.subplots(1,2, figsize=(12, 4.5), dpi = 300)
        fig.subplots_adjust(hspace=0, wspace=0.32)
        return fig,axs
    def set_xlabel(ax,xlabel1,xunit1=None):
        ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$ / $\mathrm{{{xunit1}}}$') if xunit1 is not None else ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$ /-') 
    def set_ylabel(ax,ylabel1,yunit1=None):
        ax.set_ylabel(f'\n \n $\mathrm{{{ylabel1}}}$ \n / $\mathrm{{{yunit1}}}$',rotation=0,loc="top",linespacing=1.5) if yunit1 is not None else ax.set_ylabel(f'\n \n $\mathrm{{{ylabel1}}}$ \n / -',rotation=0,loc="top",linespacing=1.5)
    def plot(ax,x,y,color="#99CC00"):
        ax.plot(x,y,color = color , zorder=1,linewidth = 3.0)
    def scatter(ax,x,y,color="#99CC00"):
        ax.scatter(x,y,color = color , s=100, zorder=2,marker="o", linewidth=1.0, edgecolor='k')
    def set_ticks(ax,x0,x1,y0,y1):
        ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=True, left=True, right=True, direction="in",length=6, width=1)
        ax.axis([x0, x1, y0, y1])
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(start, end, 5))
        start, end = ax.get_ylim()
        ax.yaxis.set_ticks(np.linspace(start, end, 5))
        plt.show()