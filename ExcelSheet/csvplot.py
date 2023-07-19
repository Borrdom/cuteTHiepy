import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("Werte2.txt", encoding = "utf-8", sep=",", header=None)

# Anzahl Subplots = Anzahl x-Achsen
Boolarr=df.values[0,:]=="x"
NSubs=Boolarr.sum()

# Anzahl subplots erstellen
fig, axs = plt.subplots(NSubs)

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
        if (NSubs==1):
            axs.plot(x.astype(float),y.astype(float), Formatstring, label=legend)          
            axs.set_xlabel(xlabel + "/" +xunit)
            axs.set_ylabel(ylabel + "/" +yunit)
            axs.legend(loc="upper left")
        else:            
            axs[k].plot(x.astype(float),y.astype(float), Formatstring, label=legend)
            axs[k].set_xlabel(xlabel + "/" +xunit)
            axs[k].set_ylabel(ylabel + "/" +yunit)
            axs[k].legend(loc="upper left")



plt.show()