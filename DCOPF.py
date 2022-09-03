# -*- coding: utf-8 -*-
"""
Created on Wed sep 03 08:17:16 2022

@author: ladan
"""
from pyomo.environ import *
import pandas as pd

df2 = pd.read_excel('opfthreebus.xlsx', sheet_name='bus_num')
bus_num=df2.size
data = DataPortal()

model = AbstractModel()
#index
model.I=Set()
model.J=Set()
#Parameters
model.a =Param(model.I)
#model.g =Param(model.I)
model.Pmax = Param(model.I) 
model.Pmin = Param(model.I) 
model.imp = Param(model.I,model.J) 
model.Pd = Param(model.I) 
# the next line declares a variable indexed by the set J
model.p = Var(model.I, domain=NonNegativeReals)
model.teta = Var(model.I, domain=Reals)
#definition of cost function and constraints
def obj_rule(model):
    return sum(model.a[i]*(model.p[i]) for i in model.I)
model.obj = Objective(rule=obj_rule)

def Try_rule(model,i):
        return model.p[i]-model.Pd[i] == sum((model.teta[i]-model.teta[j])/model.imp[i,j] for j in model.J if i!=j)
model.con = Constraint(model.I,rule=Try_rule)
def cons1(model,i):
        return(model.p[i] <=model.Pmax[i])
model.cons1 = Constraint(model.I, rule=cons1)
def cons2(model,i):
         return(model.teta[0]==0)
model.cons2 = Constraint(rule=cons2)
def cons3(model):
        return((model.teta[0]-model.teta[2])/model.imp[0,2])<=0.4
model.cons3 = Constraint(rule=cons3)
def cons4(model,i):
         return(model.p[2]==0)
model.cons2 = Constraint(rule=cons4)
# the next line creates data object for inputs
data.load(filename="opfthreebus.xlsx", range="ladan", format="set", set=model.I)
data.load(filename="opfthreebus.xlsx", range="ladan", format="set", set=model.J)
data.load(filename="opfthreebus.xlsx", range="a",param='a',index=model.I)
data.load(filename="opfthreebus.xlsx", range="pmax",param='Pmax',index=model.I)
data.load(filename="opfthreebus.xlsx", range="loadone",param='Pd',index=model.I)
data.load(filename="opfthreebus.xlsx", range="imptwo",param='imp',format='array')
#Solve
instance = model.create_instance(data)
results = SolverFactory("ipopt").solve(instance)
results.write()
instance.solutions.load_from(results)
instance.pprint()
