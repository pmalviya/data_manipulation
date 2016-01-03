import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    doc_id = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, doc_id)

def reducer(word, list_of_values):
    # key: word
    # value: list of occurrence counts
    docHash = {}
    for v in list_of_values:
      docHash[v] =1
    docList = docHash.keys()
    mr.emit((word, docList))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
