import sys
import json

def hw(afinnfile, tweet_file):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:

        tweet = json.loads(line)
        if(tweet.has_key('text')):
            status = tweet['text']
            words = status.split(' ')
            score = 0
            for word in words:
                if scores.has_key(word):
                    score = score + scores[word]
            print score


def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])

    tweet_file = open(sys.argv[2])
    hw(afinnfile, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
