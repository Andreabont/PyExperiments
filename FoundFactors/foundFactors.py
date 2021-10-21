def foundDivisors(x):
     for i in range(1,abs(x)+1):
         if x % i == 0:
             yield i

def foundFactors(x, n, found=[]):
     if n <= 1:
         return [found+[x]]
     ret = []
     for d in foundDivisors(x):
         ret += foundFactors(int(x/d), n-1, found+[d])
     return ret
