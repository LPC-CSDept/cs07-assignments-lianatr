import numpy as np
rows = int(input("how many rows?"))
columns = int(input("how many columns?"))
a = np.random.rand(rows,columns)
print(a)
for i in range(rows):
    rsumlist = []
    rsum = 0
    for j in range(columns):
        rsum += a[i][j]
        rsumlist.insert(0,rsum)
    print ("The summation of row {0} is {1}".format(i, rsum))
for i in range(columns):
    csumlist = []
    csum = 0
    for j in range(rows):
        csum += a[j][i]
        csumlist.insert(0,csum)
    print ("The summation of column {0} is {1}".format(i, csum))
row_max = max(rsumlist)
column_max = max(csumlist)
print ("The row with the greatest summation value is row", rsumlist.index(row_max))
print ("The column with the greater summation value is column", csumlist.index(column_max))
