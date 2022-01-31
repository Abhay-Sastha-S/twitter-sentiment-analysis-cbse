import pandas as pd

project_data_file_raw = open("C:/Users/MSI/Desktop/project_twitter_data updated.csv", 'r+')
results_data_file = open("C:/Users/MSI/Desktop/resulting_data.csv", 'w+')
project_data_file = open("C:/Users/MSI/Desktop/project_twitter_data_filtered.csv", 'w+')

#--------------SEARCH-------------------------------
#read lines from raw
#create for loops
#put if search word in search content



def search_and_write(project_data_filtered, search_term = "search term --"):

    lines_project_data_file_raw = project_data_file_raw.readlines()
    print(lines_project_data_file_raw)
    hearder = lines_project_data_file_raw.pop(0)
   # header_dont_use_raw = lines_project_data_file_raw.pop(0)

    project_data_filtered.write(
        "Tweet Text, Number of Retweets, Number of Replies, Tweet ID, Location Coord, Created On")
    project_data_filtered.write("\n")

    for line_project_data_file_raw in lines_project_data_file_raw:
        list_project_data_file_raw = line_project_data_file_raw.strip().split(',')
        print(list_project_data_file_raw)
        for word_tweet_data_raw in list_project_data_file_raw :
            if search_term == word_tweet_data_raw:
                project_data_filtered.write(
                    f"{list_project_data_file_raw[0]}, {list_project_data_file_raw[1]}, {list_project_data_file_raw[2]}, {list_project_data_file_raw[3]}, {list_project_data_file_raw[4]}, {list_project_data_file_raw[5]}")
                project_data_filtered.write("\n")

search_and_write(project_data_file)

#-----------------------------------------------------------------------------------------------------------------------
csv1 = pd.read_csv("C:/Users/MSI/Desktop/project_twitter_data updated.csv")
print(csv1.head())
#-----------------------------------------------------------------------------------------------------------------------

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
#-----------------------------------------------------------------------------------------------------------------------

positive_words = []
with open("C:/Users/MSI/Desktop/positive_words.txt") as pos_words_list:
    for lin in pos_words_list:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(str_sentences):
    str_sentences = remove_punctuation(str_sentences)
    list_str_sentences = str_sentences.split()
    count = 0
    for word in list_str_sentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count += 1
    return count
#-----------------------------------------------------------------------------------------------------------------------

negative_words = []
with open("C:/Users/MSI/Desktop/negative_words.txt") as neg_words_list:
    for lin in neg_words_list:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(str_sentences):
    str_sentences = remove_punctuation(str_sentences)
    list_str_sentences = str_sentences.split()

    count = 0
    for word in list_str_sentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count += 1
    return count
#-----------------------------------------------------------------------------------------------------------------------

def remove_punctuation(str_word):
    for charPunct in punctuation_chars:
        str_word = str_word.replace(charPunct, "")
    return str_word
#-----------------------------------------------------------------------------------------------------------------------

def write_in_data_file(resultingdatafile, pos_count=0, neg_count=0, neut_count = 0, tweet_count = 0):
    resultingdatafile.write(
        "Tweet ID, Tweet Text, Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score, "
        "Sentiment, Created On, Location Coord")
    resultingdatafile.write("\n")

    search_and_write(project_data_file)

    lines_project_data_file = project_data_file.readlines()
    header_dont_used = lines_project_data_file.pop(0)

    print(header_dont_used)
    print("\n", "Sample Data of Tweets", '\n', lines_project_data_file, "\n")

    for lines_tweet_data in lines_project_data_file:
        list_tweet_data = lines_tweet_data.strip().split(',')
        print("TWEET TEXT--", list_tweet_data[0], "\n", "-- Retweet Count", list_tweet_data[1], "-- Reply Count",
              list_tweet_data[2])
        # create a variable to store the tweet text, list_tweet_data[0] is the tweet text
        tweettext = list_tweet_data[0]
        tweetlocation = list_tweet_data[4]
        tweetcreated = list_tweet_data[5]
        tweetid = list_tweet_data[3]
        net_score = get_pos(list_tweet_data[0]) - get_neg(list_tweet_data[0])
        x = 0
        tweet_count += 1

        if net_score > 0:
            x = "positive"
            pos_count += 1
        elif net_score < 0:
            x = "negative"
            neg_count += 1
        elif net_score == 0:
            x = "neutral"
            neut_count += 1

        resultingdatafile.write(
            f"{tweetid}, {tweettext}, {list_tweet_data[1]}, {list_tweet_data[2]}, {get_pos(list_tweet_data[0])}, {get_neg(list_tweet_data[0])}, {(get_pos(list_tweet_data[0]) - get_neg(list_tweet_data[0]))}, {x}, {tweetcreated}, {tweetlocation}")
        resultingdatafile.write("\n")

    print("\n", "total no of tweets -", tweet_count, "\n", "no of positive tweets -", pos_count, "\n", "no of negative counts -", neg_count, "\n", "no of neutral tweets -", neut_count, "\n")
    print("\n", "Percentage of postive tweets -", ((pos_count/tweet_count)*100),"%", "\n", "Percentage of negative tweets -", ((neg_count/tweet_count)*100),"%", "\n", "Percentage of neutral tweets -", ((neut_count/tweet_count)*100),"%", "\n")
write_in_data_file(results_data_file)
# -----------------------------------------------------------------------------------------------------------------------

    ##graphing

#-----------------------------------------------------------------------------------------------------------------------

project_data_file.close()
results_data_file.close()

csv2 = pd.read_csv("C:/Users/MSI/Desktop/resulting_data.csv")
print("\n", "Sample Result Data of Tweets-- ", '\n', csv2.head(), "\n")



