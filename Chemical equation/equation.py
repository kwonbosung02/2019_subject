import sys,re
from sympy.solvers import solve
from sympy import Symbol

from fractions import gcd   #최대공약수
from collections import defaultdict

Ls=list('abcdefghijklmnopqrstuvwxyz')

print("Example = C7H16+O2->CO2+H2O ")
eq= input("화학방응식을 입력하세요 : ")

first_OBJ = defaultdict(list)
second_OBJ = Ls[:]
Get = []
a = 1
i = 1

#print(first_OBJ)
#print(second_OBJ)

for p in eq.split('->'):
 for k in p.split('+'):
    c = [Ls.pop(0), 1]
    #print(c)
    for e,m in re.findall('([A-Z][a-z]?)([0-9]*)',k):
  
        if m =='':
            m = 1

        a = a*int(m)

        d=[c[0],c[1]*int(m)*i]

        first_OBJ[e][:0] = [d]
        
        #print(first_OBJ)
        Get[:0] = [[e,d]]
        #print(Get)
      
    i=-1


prop=dict((s,eval('Symbol("'+s+'")')) for s in second_OBJ if s not in Ls)


prop2=[eval('+'.join('%d*%s'%(int(c[1]),c[0]) for c in first_OBJ[s]),{},prop) 
    for s in first_OBJ]+[prop['a']-a]
    
k=solve(prop2,*prop)

#print(k)

if k:
    N=[k[prop[s]] for s in sorted(prop)]
    g=N[0]

    for a1, a2 in zip(N[0::2],N[1::2]):
        g=gcd(g,a2)

    N=[i/g for i in N]
    #print(c)
    if c[1] != 1:
        c[1] = c
    if c[1] == 1:
        c[1] = ''
    #print(c)
    lamb=lambda c: str(c) if c != 1 else ''
    
    Answer = '->'.join('+'.join(lamb(N.pop(0))+str(t) for t in p.split('+')) for p in eq.split('->'))
    Answer = Answer.replace('-',"").replace('>','->')
    #print(Answer[0])
    if Answer[0] == '1':
        Answer = Answer[1:]
    #print(type(Answer))
    print("="*50)
    print(Answer)
   
else:
    print ('ERROR')