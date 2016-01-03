import sys
import json
import operator

def hw( tweet_file):
	hashCount ={}
	count =0
	for line in tweet_file:
		tweet = json.loads(line)

        if(tweet.has_key('entities')):
		#if(True):
			entities = tweet['entities']
			if entities.has_key('hashtags'):
				hastagsArr = entities['hashtags']
				#print hastagsArr
				for hashtag in hastagsArr:
					hashText = hashtag['text']
					hashVal = len(hashtag['indices'])
					if hashCount.has_key(hashText):
						hashCount[hashText] = hashCount[hashText] + hashVal
					else:
						hashCount[hashText] = hashVal

	sorted_hash = sorted(hashCount.items(), key=operator.itemgetter(1))
	#print sorted_hash
	for tuple in sorted_hash:
		if count < 10:
			print tuple[0], tuple[1]
			count += 1




def lines(fp):
    print str(len(fp.readlines()))

def main():

    tweet_file = open(sys.argv[1])
    hw( tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
