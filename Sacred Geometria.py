from itertools import
from random import
def f(s,r):
 p=[];n=1;k=1;P=1;d=choices('123456',k=r);D=permutations(d,r);O=product('+-*/',repeat=r-1)
 while-~s*3>n:p+=P%k*[k];n,k,P=n+P%k,k+1,P*k*k
 return any(n in{eval('int(%s)'%'%s'.join(i)%o)for i in D for o in O}for n in p[-4:-1])

 # замечательная формула для счёта абилки из пф