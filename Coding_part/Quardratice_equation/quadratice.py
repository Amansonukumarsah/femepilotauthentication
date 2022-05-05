import math
def findRoots(a, b, c,val):
    if a == 0:
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
 
    if d > 0:
        val.append((-b + sqrt_val)/(2 * a))

        val.append((-b - sqrt_val)/(2 * a))

    elif d == 0:
        val.append(-b / (2*a))
    else: 
        val.append(- b / (2*a), " + i", sqrt_val)
        val.append(- b / (2*a), " - i", sqrt_val) 
 

t=int(input())
while t:
    a,b,c=map(int,input().split())
    val=[]
    findRoots(a, b, c,val)
    val=tuple(val)
    print(val)
    t=t-1
