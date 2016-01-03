import sys
import json

def hw(afinnfile, tweet_file):
    scores = {} # initialize an empty dictionary
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    stateScore = {}
    states = dict((v,k) for k,v in states.iteritems())
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
            if(tweet.has_key('place') or tweet.has_key('coordinates') != None):
                place = tweet['place']
                if(place != None and place['country'] == 'United States') :
                    fullName = place['full_name']

                    places = fullName.split(',')
                    state =None
					#
                    if(len(places) == 2 and places[1].strip() == 'USA'):
                        #print fullName, len(places)
                        state = states[places[0]].strip()
                    elif(len(places) == 2):
                        state = places[1].strip()
                    if(state != None):
                        if(stateScore.has_key(state)):
                            stateNum = stateScore[state]
                            stateScore[state] = stateNum + score
                        else:
                            stateScore[state] = score
    happyStateVal = float('-inf')
    happyState = None
    for state in stateScore:
        if(stateScore[state] > happyStateVal):
            happyState = state
            happyStateVal = stateScore[state]
    print happyState







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
