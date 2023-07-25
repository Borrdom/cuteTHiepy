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
       [2.72585e-05, 9.99970e-01, 3.40991e-09],
       [2.72585e-05, 9.99970e-01, 3.40991e-09],
       [1, 0, 0]])

t0=data[:,1]
l0=data[:,2]
r0=data[:,0]

fig = plt.figure(figsize=(6, 5),dpi=200)
fig.subplots_adjust( wspace=0,hspace=0)
ax = fig.add_axes(projection="ternary",rect=[0.18,1-0.1416-0.6603,0.6803,0.6803])
ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=False, left=True, right=True, direction="in",length=4, width=0.5,labelrotation='horizontal')
ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=False, left=True, right=True, direction="in",length=2, width=0.5,labelrotation='horizontal',which="minor")
ax.tick_params(axis="t",pad=10)
ax.tick_params(axis="l",pad=10)
ax.tick_params(axis="r",pad=10)
ax.taxis.set_label_rotation_mode( 'horizontal')
ax.laxis.set_label_rotation_mode( 'horizontal')
ax.raxis.set_label_rotation_mode( 'horizontal')
ax.text(s="mass fractions / -",x=470, y=80)
ax.text(s="T = 298.15 K \np = 1 bar",x=50, y=700)

# pc = ax.plot(t0, l0, r0,color="#FF8500",linewidth=1)
ax.set_tlabel('solvent')
ax.set_llabel('polymer')
ax.set_rlabel('API')


from matplotlib.ticker import MultipleLocator, AutoMinorLocator
ax.taxis.set_minor_locator(AutoMinorLocator(2))
ax.laxis.set_minor_locator(AutoMinorLocator(2))
ax.raxis.set_minor_locator(AutoMinorLocator(2))
# ax.tricontourf(t0, l0, r0, np.ones_like(r0))
# ax.fill(t0, l0, r0, alpha=0.2,color="#FF8500")
# ax.raxis.set_minor_locator(AutoMinorLocator(5))



LB=np.asarray([[0.19153, 0.17689, 0.63158],
       [0.27531, 0.13522, 0.58947],
       [0.33872, 0.11391, 0.54737],
       [0.39555, 0.09919, 0.50526],
       [0.44881, 0.08803, 0.46316],
       [0.54923, 0.07182, 0.37895],
       [0.5975 , 0.06566, 0.33684],
       [0.64488, 0.06038, 0.29474],
       [0.69157, 0.0558 , 0.25263],
       [0.73769, 0.05178, 0.21053],
       [0.78336, 0.04822, 0.16842],
       [0.82865, 0.04503, 0.12632],
       [0.87361, 0.04218, 0.08421],
       [0.9183 , 0.03959, 0.04211],
       [0.96273, 0.03727, 0.     ]])
LBt=LB[:,1]
LBl=LB[:,2]
LBr=LB[:,0]


RB=np.asarray([[0.14961    , 0.20589, 0.64449],
       [1.03200e-01, 2.53210e-01, 6.43580e-01],
       [7.16700e-02, 3.00820e-01, 6.27510e-01],
       [5.08900e-02, 3.46180e-01, 6.02930e-01],
       [3.62700e-02, 3.91370e-01, 5.72360e-01],
       [1.80500e-02, 4.84940e-01, 4.97010e-01],
       [1.25100e-02, 5.34440e-01, 4.53050e-01],
       [8.53000e-03, 5.86300e-01, 4.05170e-01],
       [5.72000e-03, 6.40800e-01, 3.53480e-01],
       [3.78000e-03, 6.98160e-01, 2.98060e-01],
       [2.45000e-03, 7.58520e-01, 2.39020e-01],
       [1.57000e-03, 8.21920e-01, 1.76510e-01],
       [9.98524e-04, 8.88280e-01, 1.10720e-01],
       [6.29206e-04, 9.57370e-01, 4.20000e-02],
       [1.27811e-07, 9.99960e-01, 3.60797e-05]])
RBt=RB[:,1]
RBl=RB[:,2]
RBr=RB[:,0]

# B1 = ax.plot(LBt,LBl,LBr,"-k",linewidth=1)

# B2 = ax.plot(RBt,RBl,RBr,"-k",linewidth=1)




def filled_line(ax,x,y,z,Formatstring):
       p=ax.plot(x, y, z,Formatstring,linewidth=1)
       color = p[0].get_color()
       ax.fill(x, y, z, alpha=0.2,color=color)

def conodes(ax,RBx,RBy,RBz,LBx,LBy,LBz,Formatstring):
       ax.plot(RBx,RBy,RBz,Formatstring,linewidth=1)
       ax.plot(LBx,LBy,LBz,Formatstring,linewidth=1)
       for rt,rl,rr,lt,ll,lr in zip(RBx,RBy,RBz,LBx,LBy,LBz):
              ax.plot([rt,lt],[rl,ll],[rr,lr],Formatstring,linewidth=0.5)


Formatstring1="-r"
Formatstring2="-k"
filled_line(ax,t0,l0,r0,Formatstring1)
conodes(ax,RBt,RBl,RBr,LBt,LBl,LBr,Formatstring2)
plt.show()