from fractions import Fraction


ja = [ 2, 1, 1, 7, 6, 5, 8]
mo = [ 8, 6, 4, 2, 3, 3, 4]

f = Fraction()
f2 = [ "", "" ]

print(f)

for j, m in reversed(list(zip(ja, mo))):
    f = (j)/(m + f)
    f2 = [ str(j) + f2[0], str(m) + f2[1]]
    f2f = Fraction( int(f2[0]), int(f2[1]))
    print(f)
    print(f2f)
    print(float(f - f2f))
    print("-------------")
    

def confrac(ja, mo):    
    f = Fraction()
    for j, m in reversed(list(zip(ja, mo))):
        f = (j)/(m + f)
    return f

for i in range(1, len(ja)+1):
    ja_, mo_ = ja[:i], mo[:i]    
    f = confrac(ja_, mo_)
    f2 = Fraction( int( "".join([ str(j) for j in ja_]) ), 
                   int( "".join([ str(m) for m in mo_]) ) )
    print(f, f2, "%e"%(float(f-f2)), f-f2)
