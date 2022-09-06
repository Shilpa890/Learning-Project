import pandas as pd
import numpy as np
import random

l1=list(range(97,123))
chars=[chr(x) for x in l1 ]
#print(chars)
def AgentName(n):
    s1=random.sample(chars,n)
    rand_str="".join(s1)
    return rand_str

filesize=1000000
AgentNames=[AgentName(10) for x in list(range(0,filesize))]
#print(AgentNames[1:100])
a1=list(range(0,filesize))
a2=np.random.randint(111111,999999,filesize)
file=pd.DataFrame({'AgentID':a1,'AgentName':AgentNames,'Salary':a2})
# print(len(a1))
# print(len(a2))
# print(len(AgentNames))
# print(a2[1:100])
print(file)
file.to_csv("AWS_File.csv")