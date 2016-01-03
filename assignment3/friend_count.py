import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, 1)

def reducer(order, records):
    # key: word
    # value: list of occurrence counts
    friendCount =0
    for record in records:
      friendCount += 1
    value = (order ,  friendCount)
    mr.emit(value)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
