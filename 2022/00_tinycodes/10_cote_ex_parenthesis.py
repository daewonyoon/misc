# catalan
# C(n) = 2nCn / (n+1)

l = ["()"]
for i in range(2, 13):
    ll = set()
    for e in l:
        e = list(e)
        for j in range(len(e) + 1):
            ee = str("".join(e[:j])) + "()" + str("".join(e[j:]))
            ll.add(ee)
    l = list(ll)
    print(i, len(l))
    for k, s in enumerate(sorted(l)):
        print(k, s)
    input()

