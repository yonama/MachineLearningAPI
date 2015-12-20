#!/usr/bin/env python

import sys

sys.path.append("./components/")
from component import component

sys.path.append("./models/")
from model import model

class aprioricompo(component):
    def setup(self):
        self.min_support = 0.24

    def __apriori_gen(self,flst,items_list):
        if len(flst)<len(items_list):addlst=flst
        else:addlst=items_list
        tmp=[]
        for i in flst:
            for j in addlst:
                n=len(i)
                f=set(i).union(set(j))
                if len(f)==n+1 and f not in tmp:
                    tmp.append(f)
        return [ list(t) for t in tmp]

    def __support_func(self,num,idata,xlst):
        isum,usum=set(range(num)),set()
        for x in xlst:
            if x in idata:
                isum=isum.intersection(set(idata[x]))
                usum=usum.union(set(idata[x]))
        lisum,lusum=len(isum),len(usum)
        if lusum==0:lisum=0
        return lisum,lusum


    def __create_idata(self,testdata,items):
        idata={}
        num=len(testdata)
        for i in items:
            for j in range(num):
                if i in testdata[j]:
                    if i in idata:
                        idata[i].append(j)
                    else:
                        idata[i]=[j]
        return idata,num

    def __apriori_func(self,idata,tran_num,f,max_k):
        sol=[]
        k=1
        while f!=[]:
            n_f=[]
            print("f[%d]=%d" % (k,len(f)))
            for x in f:
                isum,usum = self.__support_func(tran_num,idata,x)
                sup=1.0*isum/tran_num
                if sup >= self.min_support:
                    sol.append([ x,sup,(isum,usum) ])
                    n_f.append(x)
            if k==1:f1=n_f[:]
            if max_k<=k: break
            f=self.__apriori_gen(n_f,f1)
            k+=1
        return sol

    def apriori(self,testdata,items,max_k):
        idata,tran_num = self.__create_idata(testdata,items)
        f=[ [i] for i in items]
        return self.__apriori_func(idata,tran_num,f,max_k)
