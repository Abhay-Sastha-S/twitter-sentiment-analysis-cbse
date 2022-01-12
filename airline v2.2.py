import pandas as pd

# opening the csv file as a dataframe
raw_data = pd.read_csv("C:/Users/MSI/Desktop/project_twitter_data updated.csv")
# print(raw_data)
fltrd_data = pd.DataFrame()
# extraxt the tweets to a list
raw_data_tweets_list = []
raw_data_tweets_list = raw_data.iloc[:, 0]
# print(raw_data_tweets_list)
# obtain the positive and negative words from the
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


# function to score the positive and negative words in tweets
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


# defining the puntuations and getting rid of punctuations in tweets to be replaces with " "
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def remove_punctuation(str_sentence):
    for charPunct in punctuation_chars:
        str_sentence = str_sentence.replace(charPunct, "")
    return str_sentence


def convert(lst):
    return ([i for i in lst.split()])


def search_in_data_file(searchdatafile, search_word=input('enter search term --')):
    fltrd_data = pd.DataFrame()
    filtered_tweet_list = []
    index_list = []
    count = 0
    for tweet_line in searchdatafile:
        count += 1
        tweet_words_list = convert(tweet_line)
        for tweet in tweet_words_list:
            if search_word in tweet:
                filtered_tweet_list.append(tweet_line)
                index_list.append(count)
    print("No. of search results found - ", len(filtered_tweet_list))
    # fltrd_data = pd.DataFrame(filtered_tweet_list, columns =["tweet_text"])

    print(fltrd_data)
    print(index_list)

    fltrd_df= pd.DataFrame()


    for index_list_value in index_list:
        print(raw_data.iloc[index_list_value-1])
        fltrd_df = pd.DataFrame(raw_data.iloc[index_list_value-1], columns=['tweet_text','retweet_count','reply_count','tweet_id','tweet_coord','tweet_created'])
        #fltrd_df = fltrd_df.append(temp)

    print(fltrd_df)


search_in_data_file(raw_data_tweets_list)
