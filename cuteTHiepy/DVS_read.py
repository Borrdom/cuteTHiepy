import pandas as pd

import pandas as pd
from tkinter.filedialog import askopenfilename
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
import xlrd
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.ndimage import median_filter
from numpy import inf
import time

def interparc(x,y,N):
    xmax=np.max(x)/3
    ymax=np.max(y)
    xmin=np.min(x)/3
    ymin=np.min(y)
    x=(x-xmin)/(xmax-xmin)
    y=(y-ymin)/(ymax-ymin)
    data=np.vstack((x,y)).T
    xd = np.diff(x)
    yd = np.diff(y)

    dist = np.sqrt(xd**2+yd**2)
    u = np.cumsum(dist)
    u = np.hstack([[0],u])

    t = np.linspace(0,u[-1],N)
    xn = InterpolatedUnivariateSpline(u, x,k=1)(t)*(xmax-xmin)+xmin
    yn = InterpolatedUnivariateSpline(u, y,k=1)(t)*(ymax-ymin)+ymin
    return xn,yn



class sheet:
    def __init__(self,filename=askopenfilename,sheet_name=0):
        self.filename=filename if not callable(filename) else filename()
        self.Data=pd.read_excel(self.filename,sheet_name=sheet_name,header=None) if ".xlsx" in self.filename else pd.read_csv(self.filename,header=None)

    def getrows(self,*args):
        return tuple([self.getrow(val) for i,val in enumerate(args)])

    def getrow(self,strx):
        boolalpha=any([val.isalpha() for val in strx])
        if boolalpha:
            Datanumberheader=[any(self.Data[val].astype(str).isin([strx]).fillna(False)) for i,val in enumerate(self.Data)]
            ncol=self.Data[self.Data==strx].dropna(how='all').index
            #ncol=self.Data[self.Data.columns[np.asarray(Datanumberheader)]].astype(str).isin([strx]).fillna(False)
            Datanumberheader2=[self.Data[val][ncol[0]+1:].dropna() for i,val in enumerate(self.Data) if Datanumberheader[i]]
            defindex=0
        else:
            Datanumberheader2=[]
            defindex=int(strx)-1
        Datanumberheader2=[self.Data[defindex][1:].dropna()] if Datanumberheader2==[] else Datanumberheader2
        return Datanumberheader2[0].values.astype(float)



def FasterXlrdRead(filename,start,*args):
    book = xlrd.open_workbook(filename, encoding_override = "utf-8")
    sheet = book.sheet_by_index(0)

    col1=sheet.col(0)
    col1arr=np.asarray([val.value for i,val in enumerate(col1)])
    nstart=np.where(col1arr==start)[0][0]+1 if np.where(col1arr==start)[0].size else 0
    nrow=sheet.nrows
    ncol=sheet.ncols
    nrow2=nrow-nstart
    #if any
    class MyException(Exception):
        pass


    header=np.asarray([sheet.cell(nstart-1, i).value for i in range(ncol)])
    soughtrows=np.asarray([np.where(val==header)[0][0] if val in header else -1 for i,val in enumerate(args) ])
    if soughtrows[-1]==-1:
        raise MyException(args[-1]+" not found")
    soughdata=[np.asarray([sheet.cell(i+nstart, valj).value if valj>=0 else 0 for i in range(nrow2)]) for j,valj in enumerate(soughtrows)] # [s]
    return tuple(soughdata)
def CombineKinetikData(strt,strx,filenames):



    def averagelist(lis):
        ave=sum(lis)/len(lis)
        std=(sum([(ave-val)**2 for val in lis])/(len(lis)-1))**0.5
        return ave,std


    t=[]
    x=[]
    tend=[]
    for i,val in enumerate(filenames):
        sheet1=sheet(val)
        t.append(sheet1.getrow(strt))
        x.append(sheet1.getrow(strx))
        tend.append(t[i][-1])
    amin,amax=np.argmin(tend),np.argmax(tend)
    #tvec,xvec=interparc.interparc(t[amin],median_filter(x[amin],100,mode="nearest"),200)
    tvec,xvec=interparc.interparc(t[amin],x[amin],200)
    #tvec,xvec=t[amin],x[amin]
    #tvec=tvec[tvec>0]
    tvec=tvec[tvec>=0]
    #tvec=np.linspace(0,tend[amin]**(1/2))**2
    xvec=[InterpolatedUnivariateSpline(valt,valx)(tvec) for (valt,valx) in zip(t,x)]
    fig,ax=plt.subplots()

    [ax.plot(valt,valx,'x') for (valt,valx) in zip(t,x)]
    [ax.plot(tvec,valx,'o') for valx in xvec]

    xave,xstd=averagelist(xvec)
    ax.errorbar(x=tvec,y=xave,yerr=xstd,fmt='ko')
    return [tvec]*len(xvec),xvec,xave,xstd

def CombineData(strt,strx,filenames):

    t=[]
    x=[]
    tend=[]
    for i,val in enumerate(filenames):
        sheet1=sheet(val)
        t.append(sheet1.getrow(strt))
        x.append(sheet1.getrow(strx))
    Dataheader=tuple([sheet1.Data[val][0] for i,val in enumerate(sheet1.Data)])
    #allrows=sheet1.getrows(*Dataheader)
    return t,x,x[0],np.zeros_like(x[0])

def read_excel_file(filename):


    start_time = time.time()
    # =============================================================================
    nt=300

    stra='Target Partial Pressure (Solvent A) [%]' #if self.solvent=="water" else 'Target Partial Pressure (Solvent B) [%]'
    straa='Actual Partial Pressure (Solvent A) [%]' #if self.solvent=="water" else 'Actual Partial Pressure (Solvent B) [%]'
    straaa='Measured Partial Pressure (Solvent A) [%]' #if self.solvent=="water" else 'Measured Partial Pressure (Solvent B) [%]'
    strt="Time [minutes]"
    strm="m_Korr[mg]"
    strm2="Mass [mg]"
    start="Time [minutes]"
    try:
        a2_exp,a1_exp,a_exp,t_exp,m_exp=FasterXlrdRead(filename,start,straaa,straa,stra,strt,strm) #if self.File==True else self.CreateDummyExperiment()
    except:
        a2_exp,a1_exp,a_exp,t_exp,m_exp=FasterXlrdRead(filename,start,straaa,straa,stra,strt,strm2) #if self.File==True else self.CreateDummyExperiment()
    aa_exp=a2_exp if (a1_exp==np.zeros_like(a1_exp)).all() else a1_exp
    m_exp=m_exp*1E-6
    t_exp=t_exp*60
    Feuchte, indices=np.sort(np.unique(a_exp,return_index=True))
    dRHdt=np.diff(a_exp)
    indch=np.hstack((1,np.where(dRHdt!=0)[0]+1))
    des=dRHdt[indch-1]<=0
    abso=dRHdt[indch-1]>=0
    nJump=indch.shape[0]
    idxdes=np.where(des)[0]
    indices=np.append(indch,-2) #Anfügen des Endes der Messung
    mnull=m_exp[indices[1]] #Masse der Probe vor dem Experiment [mg]
    w_exp=(m_exp-mnull)/m_exp


    wreal=[]
    wanf=[]
    wrealmittel=[]
    Feuchtereal=[]
    mlist=[]
    tlist=[]
    wlist=[]
    key=[]
    wrealdes=[]
    wanfdes=[]
    wrealmitteldes=[]
    Feuchterealdes=[]
    mlistdes=[]
    tlistdes=[]
    wlistdes=[]
    keydes=[]
    Feuchteactual=[]
    Feuchteactualdes=[]
    Feuchteanf=[]
    Feuchteanfdes=[]
    sratel=[]
    srateldes=[]
    def Appending(wreal,wanf,wrealmittel,Feuchtereal,Feuchteactual,Feuchteanf,mlist,tlist,wlist,sratel,key,indices,k,des=False):
            jump=str(a_exp[indices[k]-1])+"_"+str(a_exp[indices[k]]) #if des==False else str(a_exp[indices[k]])+"_"+str(a_exp[indices[k]-1])
            key.append(jump)
            toffset=2
            toffset=toffset
            mapp=m_exp[indices[k]+toffset:indices[k+1]]
            mapp=mapp #if des==False else -mapp
            tapp=t_exp[indices[k]+toffset:indices[k+1]]
            wapp=(mapp-mnull)/mapp #if des==False else (mapp+mnull)/mapp
            mmax=np.max(mapp)
            mpercent=(mapp-mapp[0])/(mmax-mapp[0]) #indmax befor mpercent is better for small masses 10.05.20
            srate=np.gradient(wapp,tapp)
            srate_smooth=median_filter(srate,50,mode="nearest")
            indmmax=-1
            mapp=mapp[0:indmmax]
            tapp=tapp[0:indmmax]
            tapp=(tapp-tapp[0])
            wapp=wapp[0:indmmax]
            srate_smooth=srate_smooth[0:indmmax]
            tapp2, mapp2=interparc(tapp, mapp, nt+1) 
            tapp2=tapp2 
            wapp2=(mapp2-mnull)/mapp2 #if des==False else (mapp2+mnull)/mapp2
            wapp2=np.fmax(wapp2,1E-4)
            mapp2=mapp2 #if des==False else -mapp2
            tlist.append(tapp2)
            mlist.append(mapp2)
            wlist.append(wapp2) #if des==False else wlist.append(-wapp2+wapp2[0]+wapp2[-1])
            wanf.append(wapp2[0]) #if des==False else wanf.append(wapp2[-1])
            wreal.append(wapp2[-1]) #if des==False else wreal.append(wapp2[0])
            srate2=np.gradient(wapp2,tapp2)
            srate2_smooth=median_filter(srate2,50,mode="nearest")
            wrealmittel.append(0.7*wapp2[-1]+0.3*wapp2[0])
            FFeuchte=np.mean(aa_exp[indices[k]+toffset:indices[k+1]-1])*0.01 #if des==False else np.mean(aa_exp[indices[k-1]+toffset:indices[k]-1])*0.01
            Feuchtean=a_exp[indices[k-1]]*0.01
            Feuchte=a_exp[indices[k]]*0.01 #if des==False else a_exp[indices[k-1]]*0.01
            Feuchtereal.append(Feuchte)
            Feuchteanf.append(Feuchtean)
            Feuchteactual.append(FFeuchte)
            sratel.append(srate2_smooth)
            return
    for k in range(1,nJump):
        if all(k!=idxdes):
            Appending(wreal,wanf,wrealmittel,Feuchtereal,Feuchteactual,Feuchteanf,mlist,tlist,wlist,sratel,key,indices,k)
        elif any(k==idxdes) and len(m_exp[indices[k]:indices[k+1]])>0:
            Appending(wrealdes,wanfdes,wrealmitteldes,Feuchterealdes,Feuchteactualdes,Feuchteanfdes,mlistdes,tlistdes,wlistdes,srateldes,keydes,indices,k,des=True)
    result={}
    des=False
    result["nHum"]=len(wreal) if not des==True else len(wrealdes)
    #self.nHumdes=len(wrealdes)
    result["dickeys"]=key if not des==True else keydes
    #endhums=[val.split("_")[1] for i,val in enumerate(self.dictkeys)]
    #self.wrealdes=wrealdes#if not self.des==True else keydes
    #self.wanfdes=wanfdes
    result["wrealmittelref"]=wrealmittel if not des==True else wrealmitteldes
    #self.wrealmitteldes=wrealmitteldes
    #self.Feuchterealdes=Feuchterealdes#[1:]
    for i in range(len(tlist)):
        result[f"tlist{i}"]=tlist[i] if not des==True else tlistdes[i]
        result[f"wlist{i}"]=wlist[i] if not des==True else wlistdes[i]
        result[f"sratel{i}"]=sratel[i] if not des==True else srateldes[i]
    wreal=np.asarray(wreal) if not des==True else np.asarray(wrealdes)
    result["wreal"]=wreal
    result["wanf"]=np.asarray(wanf) if not des==True else np.asarray(wanfdes)
    Feuchtereal=np.asarray(Feuchtereal) if not des==True else np.asarray(Feuchterealdes)
    result["Feuchtereal"]=Feuchtereal

    result["Feuchteactual"]=np.asarray(Feuchteactual) if not des==True else np.asarray(Feuchteactualdes)
    result["mnull"]=mnull
    result["Feuchteanf"]=np.asarray(Feuchteanf) if not des==True else np.asarray(Feuchteanfdes)
    
    Feuchteges=np.hstack((Feuchtereal,Feuchterealdes))
    wges=np.hstack((wreal,wrealdes))
    wges=wges[Feuchteges!=0]
    Feuchteges=Feuchteges[Feuchteges!=0]


    Feuchteiso,idxunique=np.unique(Feuchteges,True)
    result["wiso"]=np.asarray([np.average(wges[Feuchteges==val]) for i,val in enumerate(Feuchteiso)])
    result["Feuchteiso"]=Feuchteiso
    # If Absorbtion and Desorption have differences do not take the average between them even if its the same RH
    Feuchteun,idxun=np.unique(Feuchtereal,True)
    wun=np.asarray([np.average(np.asarray(wreal)[Feuchtereal==val]) for i,val in enumerate(Feuchteun)])
    result["wiso"]=np.asarray([np.average(wun[Feuchteun==val]) if len(wun[Feuchteun==val])>0 else np.average(wges[Feuchteges==val]) for i,val in enumerate(Feuchteiso)])
    Feuchteactualges=np.hstack((Feuchteactual,Feuchteactualdes))
    result["Feuchteiso"]=Feuchteiso
    print("Reading Excel-File took--- %s seconds ---" % (time.time() - start_time))
    
    result["t_exp"]=t_exp
    result["w_exp"]=w_exp
    from pathlib import Path
    pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in result.items() ])).to_excel(Path(filename).stem+"_result.xlsx")
    return

read_excel_file(askopenfilename())