
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(str1):
    "this function removes all the punctuation from a string which will be passed in as a parameter"
    for char in str1:
        if char in punctuation_chars:
            str1 = str1.replace(char, '')
    return str1


def get_neg(str1):
    "this function counts the number of negative words in a given string"
    unpunctuated_sentence = strip_punctuation(str1)
    words = unpunctuated_sentence.strip().split()
    number_negative_words = 0
    
    for word in words:
        if word.lower() in negative_words:
            number_negative_words += 1
    return number_negative_words


def get_pos(str1):
    unpunctuated_sentence = strip_punctuation(str1)
    words = unpunctuated_sentence.strip().split()
    number_positive_words = 0
    
    for word in words:
        if word.lower() in positive_words:
            number_positive_words += 1
    return number_positive_words


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            

#opening two files for reading and writing            
with open('project_twitter_data.csv', 'r') as twitter_data, open('resulting_data.csv', 'w') as results_file:
    #checking the headers of the csv file
    lines = twitter_data.readlines()
    print(lines[0])
    working_data = lines[1:]
    
    #creating the headers of the results file
    results_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
    
    #iterating through the tweets dataset and writing the score to the results file
    for line in working_data:
        #each line represents the data for one particular tweet
        tweet, retweets, replies = line.strip().split(',')
        
        #getting the positive and negative scores for the tweets with the earlier defined functions
        pos_score = get_pos(tweet)
        neg_score = get_neg(tweet)
        net_score = pos_score - neg_score     
        
        #writing the data for each particular tweet to the results file
        results_file.write('{},{},{},{},{}\n'.format(retweets, replies, pos_score, neg_score, net_score))