import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    value = (person, friend)
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend , person)

def reducer(order, records):
    # key: word
    # value: list of occurrence counts
    friendsHash ={}
    for record in records:
      if record in friendsHash :
	friendsHash[record] = 2
      else:
        friendsHash[record] = 1
    
    for key in friendsHash.keys():
	if friendsHash[key] ==1:
	   tup =(order, key)  
           mr.emit(tup)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
