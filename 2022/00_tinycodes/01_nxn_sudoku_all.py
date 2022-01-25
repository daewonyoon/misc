import itertools as it
from pprint import pprint

for p in it.permutations([1, 2, 3, 4]):
    print(p)

all_permutations = list(it.permutations([1,2,3,4]))
length = len(all_permutations)

def check_selected(perm_sel):
    len_selected = len(perm_sel)
    for es in zip(*perm_sel):
        if len(set(es)) != len_selected:
            return False
    return True

perm_sel = []
sudoku_sol = []

for i in range(length):
    perm_sel = []
    perm_sel.append(all_permutations[i][:])
    if not check_selected(perm_sel):
        perm_sel = perm_sel[:-1]
        continue

    for j in range(i+1, length):
        perm_sel.append(all_permutations[j][:])
        if not check_selected(perm_sel):
            perm_sel = perm_sel[:-1]
            continue

        #print(perm_sel)

        for k in range(j+1, length):
            perm_sel.append(all_permutations[k][:])
            if not check_selected(perm_sel):
                perm_sel = perm_sel[:-1]
                continue

            for l in range(k+1, length):
                perm_sel.append(all_permutations[l][:])
                if not check_selected(perm_sel):
                    perm_sel = perm_sel[:-1]
                    continue
                sudoku_sol.append(perm_sel)
                pprint(perm_sel)

print(len(sudoku_sol))