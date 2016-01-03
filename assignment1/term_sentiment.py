import sys
import json

def hw(afinnfile, tweet_file):
    scores = {} # initialize an empty dictionary
    textTweets = {}
    newWords = {}
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    count =0
    for line in tweet_file:

        tweet = json.loads(line)
        if(tweet.has_key('text')):
            status = tweet['text']
            words = status.split(' ')
            score = 0
            newWordsHash = {}
            for word in words:
                if scores.has_key(word):
                    score = score + scores[word]
                else:
                    newWordsHash[word] = 1
            for key in newWordsHash.keys():
                if newWords.has_key(key):
                    tweetList = newWords[key]
                    tweetList.append(count)
                    newWords[key] = tweetList
                else:
                    li =[]
                    li.append(count)
                    newWords[key] =li
            textTweets[count] = score
            count+=1

            # print newWords
    #Get score for new words
    count =0
    for word in newWords:
        newWordScore = 0
        tweets = newWords[word]
        for num in tweets:
            newWordScore = newWordScore + textTweets[num]
        #if(count< 10):
        print word, newWordScore
        #count+=1


def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(afinnfile, tweet_file)

if __name__ == '__main__':
    main()
