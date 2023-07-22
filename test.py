import numpy as np

import matplotlib.pyplot as plt
import mpltern
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Calibri'
matplotlib.rcParams['mathtext.it'] = 'Calibri'
matplotlib.rcParams['mathtext.bf'] = 'Calibri'
# matplotlib.rcParams['xtick.major.pad']='5'
# matplotlib.rcParams['ytick.major.pad']='5'
matplotlib.rcParams['axes.linewidth'] = 0.5
# matplotlib.rcParams["toolbar"] = "toolmanager"
# plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

font = {'weight' : 'normal',
        'size'   : 16,
        'family' : "calibri"}
plt.rc('font', **font)


data=np.asarray([[0.19835,	7.90815E-24,	0.80165],
       [1.97470e-01, 2.21700e-02, 7.80360e-01],
       [1.79520e-01, 4.27400e-02, 7.77740e-01],  
       [1.60330e-01, 6.09400e-02, 7.78730e-01],  
       [1.42480e-01, 7.71900e-02, 7.80330e-01],  
       [1.26430e-01, 9.19600e-02, 7.81610e-01],  
       [1.12100e-01, 1.05660e-01, 7.82230e-01],  
       [9.92800e-02, 1.18640e-01, 7.82080e-01],  
       [8.77300e-02, 1.31170e-01, 7.81100e-01],  
       [7.72500e-02, 1.43510e-01, 7.79240e-01],  
       [6.76600e-02, 1.55910e-01, 7.76440e-01],  
       [5.05600e-02, 1.82010e-01, 7.67430e-01],  
       [4.28000e-02, 1.96470e-01, 7.60730e-01],  
       [3.54400e-02, 2.12640e-01, 7.51920e-01],  
       [2.83600e-02, 2.31560e-01, 7.40080e-01],  
       [2.14500e-02, 2.55240e-01, 7.23310e-01],  
       [1.45600e-02, 2.88420e-01, 6.97020e-01],  
       [7.41000e-03, 3.47900e-01, 6.44690e-01],  
       [2.72585e-05, 9.99970e-01, 3.40991e-09],
       [2.72585e-05, 9.99970e-01, 3.40991e-09]])

t0=data[:,1]
l0=data[:,2]
r0=data[:,0]

fig = plt.figure(figsize=(6, 5),dpi=200)
fig.subplots_adjust( wspace=0,hspace=0)
ax = fig.add_axes(projection="ternary",rect=[0.2354,1-0.1016-0.6603,0.6603,0.6603])
ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=False, left=True, right=True, direction="in",length=4, width=0.5)
ax.tick_params(axis="t",pad=10)
ax.tick_params(axis="l",rotation=60,pad=10)
ax.tick_params(axis="r",rotation=-60,pad=12)
dx = 11/72.; dy = 0/72. 
offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# apply offset transform to all x ticklabels.
for label in ax.raxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)
# for tick in ax.raxis.get_majorticklabels():
#     tick.set_verticalalignment("baseline")
pc = ax.plot(t0, l0, r0)
ax.set_tlabel('solvent')
ax.set_llabel('polymer')
rlabel=ax.set_rlabel('API')
rlabel.set_rotation(270)

# ax.taxis.set_ticks_position("tick2")
# ax.laxis.set_ticks_position("tick2")
# ax.raxis.set_ticks_position("tick2")
# ax.laxis.label.set(rotation=180)
# ax.raxis.label.set(rotation=-60)
# plt.fill_between(t0,l0, r0, step="pre", alpha=0.4)
# ax = fig.add_subplot(1, 2, 2, projection="ternary")
# pc = ax.scatter(t0, l0, r0, c=length)

# cax = ax.inset_axes([1.05, 0.1, 0.05, 0.9], transform=ax.transAxes)
# colorbar = fig.colorbar(pc, cax=cax)
# colorbar.set_label("Length", rotation=270, va="baseline")

plt.show()