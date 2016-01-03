import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(value):
   #value is ("a", i, j, a_ij) or ("b", j, k, b_jk)
    if value[0] == "a":
        i = value[1]
        j = value[2]
        a_ij = value[3]
        for k in range(0,4):
           mr.emit_intermediate((i, k), ("a", j, a_ij))
    else:
        j = value[1]
        k = value[2]
        b_jk = value[3]
	for i in range(0,4): 
           mr.emit_intermediate((i, k), ("b", j, b_jk))

def reducer(order, values):
    list_A = {j: a_ij for (M, j, a_ij) in values if M == "a"}
    list_B = {j: b_jk for (M, j, b_jk) in values if M == "b"}
    mult =0
    for j in range(0,4):
      if j in list_A:
        a = list_A[j]
      else:
	a = 0
      if j in list_B:
        b = list_B[j]
      else:
        b =0
      mult += a * b
    tup =(order, mult)
    mr.emit(tup)
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
