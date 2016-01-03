import sys
import json

def hw(tweet_file):
	totalTerms = 0
	wordsHash = {}

	# lines(tweet_file)
	#linesList = tweet_file.readlines()
	#print linesList
	for line in tweet_file:
		tweet = json.loads(line)
		textWord = 'text'
		if(tweet.has_key(textWord)):
			status = tweet['text'].strip()
			#print status
			words = status.split(' ')
			for word in words:
				word = word.strip()
				if word != '':
					if(wordsHash.has_key(word)):
						freq = wordsHash[word]
						wordsHash[word] = freq + 1
					else:
						wordsHash[word] =1

	for word in wordsHash:
		totalTerms+=wordsHash[word]

	for word in wordsHash:
		freq = wordsHash[word]/totalTerms
		print word, freq



        #print word, freq


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
