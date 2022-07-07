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
    
