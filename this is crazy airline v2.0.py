import pandas as pd

#opening the csv file as a dataframe
raw_data = pd.read_csv("C:/Users/MSI/Desktop/project_twitter_data updated.csv")
#print(raw_data)
fltrd_data = pd.DataFrame()
#extraxt the tweets to a list
raw_data_tweets_list = []
raw_data_tweets_list = raw_data.iloc[:,0]
#print(raw_data_tweets_list)
#obtain the positive and negative words from the
positive_words = []
with open("C:/Users/MSI/Desktop/positive_words.txt") as pos_words_list:
    for lin in pos_words_list:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
negative_words = []
with open("C:/Users/MSI/Desktop/negative_words.txt") as neg_words_list:
    for lin in neg_words_list:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#function to score the positive and negative words in tweets
def get_pos(str_sentences):
    str_sentences = remove_punctuation(str_sentences)
    list_str_sentences = str_sentences.split()
    count = 0
    for word in list_str_sentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count += 1
    return count
def get_neg(str_sentences):
    str_sentences = remove_punctuation(str_sentences)
    list_str_sentences = str_sentences.split()
    count = 0
    for word in list_str_sentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count += 1
    return count

#defining the puntuations and getting rid of punctuations in tweets to be replaces with " "
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def remove_punctuation(str_sentence):
    for charPunct in punctuation_chars:
        str_sentence = str_sentence.replace(charPunct, "")
    return str_sentence

def convert(lst):
    return ([i for i in lst.split()])

def search_in_data_file(searchdatafile, search_word=input('enter search term --')):
    #row_count=0
    index_list = []
    for col in searchdatafile:
        filtered_tweet_list = []
        #row_count += 1
        for tweet_line in searchdatafile:
            #row_count += 1
            #print(tweet_line)
       # index_list.append(raw_data.index[tweet_line])
       # print(index_list)
            tweet_words_list = convert(tweet_line)
        #print(tweet_words_list)
            for tweet in tweet_words_list:
                if search_word in tweet:
                    filtered_tweet_list.append(tweet_line)

    #index_list.append(row_count)
        #index_list.append(row_count)
        #print(filtered_tweet_list)
    #for i in filtered_tweet_list:
    index_list.append(raw_data_tweets_list.index(tweet_line))
    print("No. of search results found - ", len(filtered_tweet_list))
    fltrd_data = pd.DataFrame(filtered_tweet_list, columns =["tweet_text"])
    print(fltrd_data)
        #row_count += 1
        #index_list.append(row_count)
    print(index_list)
    #row_count+=1


    #for fltrd_tweet_line in filtered_tweet_list:







search_in_data_file(raw_data_tweets_list)
