import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    table = record[0]
    order = record[1]
    mr.emit_intermediate(order, record)

def reducer(order, records):
    # key: word
    # value: list of occurrence counts
    recordHash ={}
    recordHash['line_item'] =[]
    recordHash['order'] =[]
    for record in records:
	if(len(record) == 17 ):
	  recordHash['line_item'].append(record)
        else:
	  recordHash['order'].append(record)
    for line in recordHash['line_item']:
	for order in recordHash['order']:
           value =  order + line
           mr.emit( value)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
