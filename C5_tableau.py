A = "CATAGTG"
B = "GTCAGGT"

n = len (A)
m = len (B)

tbl = {}

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

        insert_cost = tbl[ (i - 1, j) ] + 1
        delete_cost = tbl[ (i, j - 1) ] + 1
        subst_cost  = tbl[ (i - 1, j - 1) ] + subst_ij

        tbl[ (i, j) ] = min (insert_cost, delete_cost, subst_cost)


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

print (tbl)
    
        
