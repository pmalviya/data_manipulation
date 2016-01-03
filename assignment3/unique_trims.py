import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    nuclea = record[1].strip()
    nuclea = nuclea[:len(nuclea)-10]
    
    mr.emit_intermediate( nuclea.strip(), key)

def reducer(order, records):
    mr.emit(order)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
