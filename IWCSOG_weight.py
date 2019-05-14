#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:31:05 2019

@author: kingpc
"""
from PsfBuild import *
import numpy as np
from photutils import centroid_com, centroid_1dg, centroid_2dg
import time

def compareW(PSF):
    x1, y1 = centroid_com(PSF)
    x2, y2 = centroid_1dg(PSF)
    x3, y3 = centroid_2dg(PSF)
    errx1=cx-1-x1
    erry1=cy-1-y1
    errx2=cx-1-x2
    erry2=cy-1-y2
    errx3=cx-1-x3
    erry3=cy-1-y3
    err1=((errx1)**2+(erry1)**2)**0.5
    err2=((errx2)**2+(erry2)**2)**0.5
    err3=((errx3)**2+(erry3)**2)**0.5    
#    print("%.2e,%.2e,%.2e,%.2e,%.2e,%.2e," % ( errx1,erry1,errx2,erry2,errx3,erry3))

    # Weighted
    Weight=GaussianFunc(sig,accd,cx,cy)
    PSFW=PSF*Weight
    x1, y1 = centroid_com(PSFW)
    x2, y2 = centroid_1dg(PSFW)
    x3, y3 = centroid_2dg(PSFW)
    errx12=cx-1-x1
    erry12=cy-1-y1
    errx22=cx-1-x2
    erry22=cy-1-y2
    errx32=cx-1-x3
    erry32=cy-1-y3
    err12=((errx12)**2+(erry12)**2)**0.5
    err22=((errx22)**2+(erry22)**2)**0.5
    err32=((errx32)**2+(erry32)**2)**0.5    
#    print("%.2e,%.2e,%.2e,%.2e,%.2e,%.2e," % ( errx12,erry12,errx22,erry22,errx32,erry32))
    return  err1,err2,err3,err12,err22,err32


if __name__=='__main__':   
    start =time.perf_counter()
    nsample=10
    accd=40
    erra1=np.zeros([nsample,1])
    erra2=np.zeros([nsample,1])    
    erra3=np.zeros([nsample,1])
    erra4=np.zeros([nsample,1])
    erra5=np.zeros([nsample,1])
    erra6=np.zeros([nsample,1])
    
    for isample in range(0,nsample):
        cx=accd/2+np.random.rand(1,1)
        cy=accd/2+np.random.rand(1,1)
        sig=4
        PSF=GaussianFunc(sig,accd,cx,cy)
        #PSF=MoffatFunc(accd,20,2.5,cx,cy)
        ree80=sig*1.794;
        #PSF=AiryFunc(ree80,accd,cx,cy)
        nosemg=0.001;
        NOSE=10*nosemg*np.random.rand(accd,accd)+nosemg*PSF*np.random.rand(accd,accd)
        PSF=PSF+NOSE
        [a,b,c,d,e,f]=compareW(PSF)
        erra1[isample,0]=a
        erra2[isample,0]=b
        erra3[isample,0]=c
        erra4[isample,0]=d
        erra5[isample,0]=e
        erra6[isample,0]=f
    
    print("%.2e,%.2e,%.2e,%.2e,%.2e,%.2e," % ( np.mean(erra1),np.mean(erra2),
                                              np.mean(erra3),np.mean(erra4),np.mean(erra5),np.mean(erra6)))    
    
    
    
    
    
    
    
    

    seconds=time.perf_counter()-start
    print('It took {:.2f} seconds.'.format(seconds))
