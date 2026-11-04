A = "CATAGTG"
B = "GTCAGGT"

n = len (A)
m = len (B)

tbl = {}
tcb = {}

# "Cas de base" (version iterative)

for i in range (n + 1):
    tbl[ (i, 0) ] = i

for j in range (m + 1):
    tbl[ (0, j) ] = j

# "Recurrence" (version iterative)

for i in range (1, n + 1):
    for j in range (1, m + 1):

        if A[i - 1] == B[j - 1]:
            subst_ij = 0
        else:
            subst_ij = 1

        cost_up = tbl[ (i - 1, j) ] + 1
        cost_left = tbl[ (i, j - 1) ] + 1
        cost_diag  = tbl[ (i - 1, j - 1) ] + subst_ij

        min_cost = min(cost_up, cost_left, cost_diag)
        tbl[ (i, j) ] = min_cost
        if min_cost == cost_up:
            tcb[(i,j)] = 'W'
        elif min_cost == cost_left:
            tcb[(i,j)] = 'A'
        else:
            tcb[(i,j)] = 'WA'
            


# Affichage du tableau

tmp = "  - "
for j in range (1, m + 1):
    tmp += B[j - 1] + " "
print (tmp)

for i in range (n + 1):
    if i == 0:  tmp = "- "
    else:       tmp = A[i - 1] + " "
    for j in range (m + 1):
        tmp += str (tbl[ (i, j) ]) + " "
    print (tmp)

#print (tbl)

#Suivi du traceback

cell = (n,m)
align_A = ''
align_B = ''

while cell != (0,0):
    i,j = cell
    if tcb[cell] == 'W':
        align_A = A[ i-1 ] + align_A
        align_B = "-" + align_B
        cell = (i-1, j)
    elif tcb[cell] == 'A':
        align_B = B[ j-1 ] + align_B
        cell = (i, j-1)
    else:
        align_A = A[ i-1 ] + align_A
        align_B = B[ j-1 ] + align_B
        cell = (i-1, j-1)
print(align_A)
print(align_B)

# distance d'édition

dist = tbl[(n,m)]
print(f'score: {dist}')
